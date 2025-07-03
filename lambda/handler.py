import json
import boto3
import os
from datetime import datetime

# Initialize DynamoDB client using environment variable
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DATA_TABLE_NAME'])  # renamed for clarity

def persist_data(data):
    # Use ISO timestamp as a simple sortable ID
    data['id'] = datetime.utcnow().isoformat()
    table.put_item(Item=data)
    return data

def lambda_handler(event, context):
    try:
        payload = json.loads(event["body"])
        saved_item = persist_data(payload)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Data saved', 'item': saved_item})
        }
    except Exception as e:
        # If something fails, send back a structured error
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

