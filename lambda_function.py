import json
import requests
import os
import random

print('Loading function')

LINE_API_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'

LINE_API_HEADERS = {
    'Authorization': 'Bearer ' + os.environ['LINE_CHANNEL_ACCESS_TOKEN'],
    'Content-type': 'application/json'
}

def lambda_handler(event, context):
    body = event['body']
    json_body = json.loads(body)
    reply_token = json_body['events'][0]['replyToken']
    message = json_body['events'][0]['message']

    payload = {
        'replyToken': reply_token,
        'messages': []
    }
    
    payload['messages'].append({
        'type': 'text', 'text': message
    })

    response = requests.post(LINE_API_ENDPOINT, headers=LINE_API_HEADERS, data=json.dumps(payload))
    print(response.status_code)
