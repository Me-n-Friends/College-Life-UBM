def linear_search(arr, size, target):
    size = len(arr)
    for i in range(size):
        if arr[i] == target:
            return i
    return -1

def main():
    arr = [9, 1, 0, 2]
    target = 2
    size = len(arr)
    query = linear_search(arr, size, target)
    
    if (query == -1):
        print('Data is not found')
    else:
        print(query)