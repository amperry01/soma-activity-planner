import json

def load_oura_data(filepath: str) -> dict:
    """
    Load Oura data from a JSON file.
    
    Args:
        filepath (str): Path to the JSON file containing Oura data.
        
    Returns:
        dict: Parsed Oura data.
    """
    with open(filepath, 'r') as file:
        data = json.load(file)

    # TODO: process and return cleaned data as needed
    return data