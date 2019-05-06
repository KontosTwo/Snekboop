#
def reverse(data):

    changed = []
    for datum in data:
        changed.append(datum[::-1].capitalize())
    return changed
