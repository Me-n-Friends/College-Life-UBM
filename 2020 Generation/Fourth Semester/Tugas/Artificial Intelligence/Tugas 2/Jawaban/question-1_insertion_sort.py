def insertion_sort(arr, size):
    for i in range(size):
        temp = arr[i]
        hole = i
        while hole > 0 and arr[hole-1] > temp:
            arr[hole] = arr[hole-1]
            hole -= 1
        arr[hole] = temp

def print_arr(arr, size):
    size = len(arr)
    print('Sorted array: ', end=' ')
    for i in range(size):
        print(arr[i], end=', ')
        
def main():
    # arr = [5, 9, 1, 3, 7, 2, 4, 8, 6, -1, 0, -100, -99, 88, 30]
    arr = ['lemon tea', 'asian green', 'mojito']
    size = len(arr)
    insertion_sort(arr, size)
    print_arr(arr, size)

main()