import json

def run(method, headers, body):
    print(f"Received webhook with method: {method}")
    print(f"Headers: {headers}")
    print(f"Body: {json.dumps(body)}")

