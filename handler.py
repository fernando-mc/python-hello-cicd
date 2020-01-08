import json

import requests

def hello(event, context):
    print(event)
    result = requests.get('https://fernandomc.com').text
    print(result)
    body = {"result": result}
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
