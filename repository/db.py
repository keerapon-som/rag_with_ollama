import psycopg2

dbname = "your_database"
user = "your_username"
password = "your_password"
host = "localhost"
port = "5432"

def getListTable():
    # Database connection parameters
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = connection.cursor()
        # Query to get the list of tables
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public';
        """)
        tables = cursor.fetchall()
        return [table[0] for table in tables]
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        if connection:
            connection.close()

def clearAllData():
    # Database connection parameters
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = connection.cursor()
        # Clear all data from the table
        cursor.execute("DELETE FROM document_db;")
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()

def createVectorTable(vectorDimention:int):
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = connection.cursor()

        # Ensure the pgvector extension is available
        cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")

        # Create table using pgvector type
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS document_db (
                id SERIAL PRIMARY KEY,
                document TEXT NOT NULL,
                embed_model TEXT NOT NULL,
                vector_document VECTOR({vectorDimention}) NOT NULL  -- Specify the vector dimension
                
            );
        """)
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()
            



def appendListData(listData):
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = connection.cursor()

        for data in listData:
            cursor.execute("""
                INSERT INTO document_db (document, vector_document, embed_model)
                VALUES (%s, %s, %s);
            """, (data["document"], data["vector_document"], data["embed_model"]))

        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()

def searchClosestVector(vector, embedingModel, limit=5):
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = connection.cursor()

        # Perform the search using the pgvector distance function
        cursor.execute("""
            SELECT document, vector_document, embed_model
            FROM document_db
            WHERE embed_model = %s
            ORDER BY vector_document <-> %s::VECTOR
            LIMIT %s;
        """, (embedingModel, vector, limit))

        results = cursor.fetchall()
        formatted_results = [
            {
                "document": row[0],
                "vector_document": row[1],
                "embed_model": row[2]
            }
            for row in results
        ]
        return formatted_results
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    # Example usage
    # tables = getListTable()
    # print("Tables in the database:", tables)
    
    # # Create a vector table with a specified vector length
    # vectorLength = 1536  # Example vector length
    # createVectorTable(vectorLength)
    # print(f"Vector table created with vector length {vectorLength}.")
    listData = [
        {
            "document": "Sample document 1",
            "vector_document": [0.1, 0.2, 0.3, 0.4, 0.5],
            "embed_model": "model1"
        },
        {
            "document": "Sample document 2",
            "vector_document": [0.6, 0.7, 0.8, 0.9, 1.0],
            "embed_model": "model2"
        },
        {
            "document": "Sample document 3",
            "vector_document": [1.1, 1.2, 1.3, 1.4, 1.5],
            "embed_model": "model3"
        }
    ]
    appendListData(listData)
    print("Data appended to the vector table.")
    clearAllData()
