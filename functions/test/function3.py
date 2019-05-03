import json

#
# name: reverse
#
def lambda_handler(event, context):
    data = event.data

    changed = []
    for datum in data:
        changed.append(reversed(datum).capitalize())
    return {
        'statusCode': 200,
        'body': json.dumps(changed)
    }
