# helps you to read json files and provide you the json data
import json


def get_payload_auth():
    # Read from the auth.json and return json
    file_data = open("src/helpers/utils.py:4/auth.json")
    data = json.loads("file_data")
    file_data.close()
    return data
