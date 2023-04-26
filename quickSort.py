from ccsv import getArray
import time
def partition(array, low, high):
    global partition_count, comparison_count
    partition_count += 1
    pivot = array[low]
    i = low - 1

    for j in range(low, high):
        comparison_count += 1
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quicksort(array):
    
    stack = [(0, len(array)-1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(array, low, high)
            stack.append((low, pivot_index-1))
            stack.append((pivot_index+1, high))
    return array

def hoare_partition(array, low, high):
    global partition_count, comparison_count
    partition_count +=1
    
    pivot = array[low]
    i = low - 1
    j = high + 1
    while True:
        i+=1
        while array[i]<pivot:
            i += 1
            comparison_count+=1
        j -= 1
        while array[j] > pivot:
            j -= 1
            comparison_count+=1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


# Driver code
arr = getArray('OnlineNewsPopularity.csv', 40)
unsorted = [i for i in arr]
n = len(arr) -1 
partition_count = 0
comparison_count = 0
start_time = time.time()
quicksort(arr)
end_time = time.time()
# print("Number of times partition is called:", partition_count)
# print("Number of comparisons made:", comparison_count)
# print("Sorted array is:", arr)






print('Quicksort ran successfully')
print(len(arr))
print(len(unsorted))
with open('output.txt', 'a') as file:
        file.write('Input array: {}\n'.format(unsorted))
        for _ in range(5):
            file.write('\n')
        file.write('Sorted array: {}\n'.format(arr))
        file.write('Number of partitions: {}\n'.format(partition_count))
        file.write('Number of comparisons: {}\n'.format(comparison_count))
        file.write('Execution Time: {}\n'.format(end_time - start_time))

