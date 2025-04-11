


def readJsonFile(filePath: str) -> dict:
    """
    Reads a JSON file and returns its contents as a dictionary.

    Args:
        filePath (str): The path to the JSON file.

    Returns:
        dict: The contents of the JSON file.
    """
    import json

    with open(filePath, 'r') as file:
        data = json.load(file)

    return data