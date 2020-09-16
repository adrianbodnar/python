# Python3 Optimized implementation 
# of Bubble sort 
  
# An optimized version of Bubble Sort 
def bubbleSort(arr): 
    n = len(arr) 
   
    # Traverse through all array elements 
    for i in range(n): 
        swapped = False
  
        # Last i elements are already 
        #  in place 
        for j in range(0, n-i-1): 
   
            # traverse the array from 0 to 
            # n-i-1. Swap if the element  
            # found is greater than the 
            # next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
  
        # IF no two elements were swapped 
        # by inner loop, then break 
        if swapped == False: 
            break
           
# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 
   
bubbleSort(arr) 

print(arr)

# Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.

# Best Case Time Complexity: O(n). Best case occurs when array is already sorted.

# Auxiliary Space: O(1)

# Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.

# Sorting In Place: Yes

# Stable: Yes

# Due to its simplicity, bubble sort is often used to introduce the concept of a sorting algorithm.
# In computer graphics it is popular for its capability to detect a very small error (like swap of just two elements) 
# in almost-sorted arrays and fix it with just linear complexity (2n). For example, it is used in a polygon filling algorithm,
#  where bounding lines are sorted by their x coordinate at a specific scan line (a line parallel to x axis) 
#  and with incrementing y their order changes (two elements are swapped) only at intersections of two lines (Source: Wikipedia)