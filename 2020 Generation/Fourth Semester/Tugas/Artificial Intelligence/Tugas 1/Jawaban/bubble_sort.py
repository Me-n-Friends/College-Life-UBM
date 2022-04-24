def swap(el, i, j):
    el[i], el[j] = el[j], el[i]

# Ascending bubble sort
# If you want to apply in descending order
# change the > to < in the if statement

# This is an unoptimized bubble sort
# Which takes the time complexity of O(n^2)
def bubble_sort(arr, size):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# This is an optimized bubble sort
# Which takes the time complexity at its best
# is Omega(n)
# The algorithms perform minimum number of execution
# because we put a flag to indicate that the elements
# is sorted or not
def opt_bubble_sort(arr, size):
    size = len(arr)
    for i in range(size - 1):
        isSorted = 0
        for j in range(size - i - 1):
            if arr[j] > arr[j+1]:
                # swap(arr[j], arr[j+1])
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSorted = 1
        if isSorted == 0:
            break

def print_arr(arr, size):
    size = len(arr)
    print('Sorted array: ', end=' ')
    for i in range(size):
        print('%d' % arr[i], end=' ')
            
def main():
    arr = [3, 2, 9, 10, 29, 1, -1, 0]
    opt_bubble_sort(arr, len(arr))
    print_arr(arr, len(arr))
    
main()