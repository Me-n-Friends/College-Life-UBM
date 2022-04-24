def insertion_sort(arr, size):
    for i in range(size):
        temp = arr[i]
        hole = i
        while hole > 0 and arr[hole-1] > temp:
            arr[hole] = arr[hole-1]
            hole -= 1
        arr[hole] = temp

def print_arr(arr, size):
    for i in range(size):
        print(arr[i], end=' ')
        
def main():
    arr = [3, 2, 8, 1, 19, -1, -20, 0]
    size = len(arr)
    insertion_sort(arr, size)
    print_arr(arr, size)
    
main()