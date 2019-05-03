import json

#
# name: reverse
#
def lambda_handler(event, context):

    data = event["data"]

    changed = []
    for datum in data:
        changed.append(datum[::-1].capitalize())
    return {
        'statusCode': 200,
        "headers": {"Content-Type": "application/json"},
        'body': changed
    }
