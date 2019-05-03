import json

#
# name: sort_find
#
def lambda_handler(event, context):

    data = event["data"]
    bubbleSort(data)
    keywords = ["asdfvawe","as","gar","wtav","vatwetb","vwaetwea","awervawet","awetoavwte","vuaw4uho"]
    changed = []
    for datum in data:
        for keyword in keywords:
            if keyword in datum:
                changed.append(datum)

    return {
        'statusCode': 200,
        "headers": {"Content-Type": "application/json"},
        'body': changed
    }


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]