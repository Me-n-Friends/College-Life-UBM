from bisect import bisect_left

class Sort(object):
    def __init__(self, arr, size):
        self.arr = arr
        self.size = len(self.arr)
    
    # Ascending bubble sort
    # If you want to apply in descending order
    # change the > to < in the if statement
    
    # This is an optimized bubble sort
    # Which takes the time complexity at its best
    # is Omega(n)
    # The algorithms perform minimum number of execution
    # because we put a flag to indicate that the elements
    # is sorted or not
    def bubble_sort(self, arr, size):
        self.size = len(arr)
        for i in range(self.size - 1):
            is_sorted = 0
            for j in range(self.size - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    is_sorted = 1
            if is_sorted == 0:
                break 

    def insertion_sort(self, arr, size):
        self.size = len(arr)
        for i in range(self.size):
            temp = arr[i]
            index = i
            while index > 0 and arr[index-1] > temp:
                arr[index] = arr[index-1]
                index -= 1
            arr[index] = temp

class Search(object):
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target
        
    def binary_search(self, arr, target):
        i = bisect_left(self.arr, self.target)
        if i != len(self.arr) and arr[i] == self.target:
            return i
        return -1
    
def print_arr(arr, size):
    size = len(arr)
    for i in range(size):
        print(arr[i], end=' ')
            
            
def main():
    arr = [3, 2, 8, 1, 19, -1, -20, 0]
    size = len(arr)
    
    print('Unsorted array: ', end='')
    print_arr(arr, size)
    
    sort = Sort(arr, size)
    
    # Uncomment the function below you want to use
    sort.bubble_sort(arr, size)
    # sort.insertion_sort(arr, size)
    
    print('\n\nSorted array: ', end='')
    print_arr(arr, size)
    
    find = int(input('\nEnter a number you want to search: '))
    search = Search(arr, find)
    query = search.binary_search(arr, find)
    if query == -1:
        print('{} not found'.format(find))
    else:
        print('{} found at index {} in element {}'.format(find, query, query+1))
    
if __name__ == '__main__':
    main()