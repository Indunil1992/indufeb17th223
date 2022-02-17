import boto3
kinesis = boto3.client("kinesis")

def handler(event, context):
    try:
        data = kinesis.put_record(
            StreamName="INDUU",
            Data="12121",
            PartitionKey="ID"
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
