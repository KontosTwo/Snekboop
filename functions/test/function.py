import json


def lambda_handler(event, context):
    data = event.data

    changed = []
    for datum in data:
        reverse_capitalized = datum[::-1].upper();
        length = 1000
        final = (reverse_capitalized * (int(length / len(reverse_capitalized)) + 1))[: length]
        changed.append(final)
    return {
        'statusCode': 200,
        'body': json.dumps(changed)
    }
