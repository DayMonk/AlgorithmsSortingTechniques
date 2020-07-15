
# Python code for Insertion Sort
# Additional Logs are  used for demonstration purposes.
def InsertionSort(arr):
    # Get the length of the array
    arrlen = len(arr)
    print(' Input Array : {} >> Length : {} '.format(arr,arrlen))
    
    # iterate through the array elements starting from index[1], as we have to compare left index [0] for sorting    
    for i in range(1,arrlen):
        print ('-----------------------------------------------------')
        print( 'Current Unsorted array  : {} '.format(arr))
        print ('At Index: {} >>  unsortedValue value {} '.format(i,arr[i]))
        # Set up j value as a copy of i value
        j = i
        # set up the unsorted value to be compared to the left array of sorted values
        unsortedValue = arr[j]
        print ('Current unsortedValue array value : {}, value to the left : {}'.format(unsortedValue,arr[j-1]))
        
        # Loop from the j (copy of i) element to check for j-1 (left) index value to find the right sorting positon
        while j > 0 and unsortedValue < arr[j-1]:
            print ('As {} < {}, Move arr[j-1] value {} to the right at index {}  '.format(unsortedValue,arr[j-1],arr[j-1],j))
            
            # As unsortedValue is less then left index value, Move the left index value to right side
            arr[j] = arr[j-1]
            print ('At index {} - New value is {} '.format(j,arr[j]))
            # to check all the left index values, until the list is exhuasted.
            j = j-1
            print (' >> Comparing Left of index: {}, Value {} with  unsortedValue: {}'.format(j,arr[j-1],unsortedValue))
            # ## ### ## ## # # ### ### # ### ## ## ## # ### # ## ### ## # ## ## # ### # ## ### ## #
            # The below If condition is not required >> It's added only for demonstration purpose
            #--------------------------------------------------------------------------------------
            if unsortedValue < arr[j-1] and j > 0:
                print(' >> ({} < {}) => True >> Continue Checking left index values'.format(unsortedValue,arr[j-1]))
            else:
                print(' >> ({} < {}) => False and j : {} >> unsortedValue is at sorted position '.format(unsortedValue,arr[j-1],j))
            # ---------------------------------------------------------------------------------------
            print ('At index {} >> Insert unsortedValue value {} '.format(j,unsortedValue))
        # Insert unsortedValue to it's rightful position.
        arr[j]= unsortedValue
        print ('New array formation : {} '.format(arr))  
            
    return arr

# Test Long unsorted list
#arrlist = [3, 56, 2, 58, 79, 59, 34, 23, 4, 78, 8, 123, 45]
# Test short unsorted list
arrlist = [10,4,8,6,1]
#Test sorted list 
#arrlist = [1,2,3,4,5]
#Test n= 100 unsorted list
#arrlist = [52,68,84,73,3,81,91,58,1,19,8,78,32,94,4,98,23,6,21,20,43,69,31,87,33,62,36,41,70,51,48,38,72,24,47,57,13,7,64,49,9,16,14,99,90,92,35,25,37,89,50,85,76,67,88,131,39,56,74,42,77,26,93,97,80,82,96,60,53,46,18,65,30,27,2,83,66,29,61,10,55,22,11,75,95,45,59,86,12,15,17,79,40,34,5,71,44,63,28,54]
print(InsertionSort(arrlist))
