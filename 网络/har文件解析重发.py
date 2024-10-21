import json
import requests


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


# 使用示例
har_file_path = 'SchoolNetworkConnection.har'
resend_requests_from_har(har_file_path)
