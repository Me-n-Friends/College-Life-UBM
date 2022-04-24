def opt_bubble_sort(arr, size):
    size = len(arr)
    for i in range(size - 1):
        isSorted = 0
        for j in range(size - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSorted = 1
        if isSorted == 0:
            break

def print_arr(arr, size):
    size = len(arr)
    print('Sorted array: ', end=' ')
    for i in range(size):
        print(arr[i], end=', ')
            
def main():
    # arr = [5, 9, 1, 3, 7, 2, 4, 8, 6, -1, 0, -100, -99, 88, 30]
    arr = ['lemon tea', 'asian green', 'mojito']
    opt_bubble_sort(arr, len(arr))
    print_arr(arr, len(arr))

main()