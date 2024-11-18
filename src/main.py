import boto3

# AWS CloudWatch integration for monitoring
def log_transaction(transaction_id, status):
    cloudwatch = boto3.client('cloudwatch', region_name='us-west-2')
    cloudwatch.put_metric_data(
        Namespace='TransactionMonitoring',
        MetricData=[
            {
                'MetricName': 'TransactionStatus',
                'Dimensions': [{'Name': 'TransactionID', 'Value': transaction_id}],
                'Value': 1 if status == 'Success' else 0,
                'Unit': 'Count'
            }
        ]
    )
    print(f"Logged {transaction_id} with status {status}")

if __name__ == "__main__":
    # Example: Logging transactions
    transactions = [
        {"id": "txn_001", "status": "Success"},
        {"id": "txn_002", "status": "Failure"}
    ]
    for txn in transactions:
        log_transaction(txn["id"], txn["status"])