from ccsv import getArray
import time
def dualPivotQuickSort(arr, low, high):
	if low < high:
		
		lp, rp = partition(arr, low, high)
		
		dualPivotQuickSort(arr, low, lp - 1)
		dualPivotQuickSort(arr, lp + 1, rp - 1)
		dualPivotQuickSort(arr, rp + 1, high)
		
def partition(arr, low, high):
	global partition_count, comparison_count
	partition_count+=1
	if arr[low] > arr[high]:
		arr[low], arr[high] = arr[high], arr[low]
		
	# p is the left pivot, and q is the right pivot.
	j = k = low + 1
	g, p, q = high - 1, arr[low], arr[high]
	
	while k <= g:
		
		# If elements are less than the left pivot
		if arr[k] < p:
			comparison_count+=1
			arr[k], arr[j] = arr[j], arr[k]
			j += 1
			
		# If elements are greater than or equal
		# to the right pivot
		elif arr[k] >= q:
			comparison_count+=1
			while arr[g] > q and k < g:
				g -= 1
				
			arr[k], arr[g] = arr[g], arr[k]
			g -= 1
			
			if arr[k] < p:
				arr[k], arr[j] = arr[j], arr[k]
				j += 1
				
		k += 1
		
	j -= 1
	g += 1
	
	# Bring pivots to their appropriate positions.
	arr[low], arr[j] = arr[j], arr[low]
	arr[high], arr[g] = arr[g], arr[high]
	
	# Returning the indices of the pivots
	return j, g

# Driver code

# dualPivotQuickSort(arr, 0, 7)
arr = getArray('OnlineNewsPopularity.csv', 40)
unsorted = [i for i in arr]
n = len(arr) -1 
partition_count = 0
comparison_count = 0
start_time = time.time()
dualPivotQuickSort(arr, 0, n)
end_time = time.time()


print('Dual Pivot Quicksort ran successfully')
print(len(arr))
print(len(unsorted))
with open('output2.txt', 'a') as file:
        file.write('Input array: {}\n'.format(unsorted))
        for _ in range(5):
            file.write('\n')
        file.write('Sorted array: {}\n'.format(arr))
        file.write('Number of partitions: {}\n'.format(partition_count))
        file.write('Number of comparisons: {}\n'.format(comparison_count))
        file.write('Execution Time: {}\n'.format(end_time - start_time))

	