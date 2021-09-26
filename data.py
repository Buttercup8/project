import requests

def get_data(url, headers):
    """Function to return data from spotify request"""
    res = requests.get(url=url, headers=headers)

    return res.json()
