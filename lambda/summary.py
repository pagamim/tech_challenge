import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DATA_TABLE_NAME'])
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get all items from the table
    scan_result = table.scan()
    total = len(scan_result.get('Items', []))

    # Structure summary object
    summary = {
        'summary_time': datetime.utcnow().isoformat(),
        'total_items': total
    }

    # Save report to S3 with timestamped filename
    key = f"summaries/summary_{datetime.utcnow().strftime('%Y-%m-%d')}.json"
    s3.put_object(
        Bucket=os.environ['SUMMARY_BUCKET'],
        Key=key,
        Body=json.dumps(summary),
        ContentType='application/json'
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Summary saved to S3', 'key': key})
    }

