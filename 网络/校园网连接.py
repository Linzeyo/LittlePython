import json
import requests
import os
import shutil

def resend_requests_from_har(har_file_path):
    with open(har_file_path, 'r', encoding='utf-8') as file:
        har_data = json.load(file)

    for entry in har_data['log']['entries']:
        request = entry['request']
        method = request['method']
        url = request['url']
        headers = {header['name']: header['value'] for header in request['headers']}
        post_data = request.get('postData', {}).get('text', None)

        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=post_data)
        # Add handling for other HTTP methods if needed

        print(f"Re-sent {method} request to {url} with status code: {response.status_code}")

har_file_path = 'C:\\LinZeyoProject\\SchoolNetworkConnection.har'
directory = 'C:\\LinZeyoProject\\'

if not os.path.exists(directory):
    os.makedirs(directory)

if not os.path.exists(har_file_path):
    user_input_path = input("Please enter the path to your HAR file: ")
    shutil.copy(user_input_path, har_file_path)

resend_requests_from_har(har_file_path)