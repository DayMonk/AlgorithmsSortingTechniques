def selectionSort(arr):
    # Get the length of the array
    arrlen = len(arr)
    print('Length of the Input Array : {}'.format(arrlen))
    # Counter to count # of iterations

    cnt = 0
    cnt_comps = 0  # count the comparisions

    for i in range(0, arrlen-1):   # Initial Loop to iterate through Arrays
        # set the indexposition for example i = 0,1,2,3,4
        indexpos = i
        # set the smallestValue as the Current index position array Value
        smallValue = arr[indexpos]
        #  increment the iteration counter
        cnt = cnt+1

        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print('Iteration : {} starting array is {} '.format(cnt,arr))

    # Loop to compare the index position value with rest of the values in array

        for j in range(i+1, arrlen):

            print('comparing  {}  and  {} '.format( smallValue , arr[j]))
            cnt_comps = cnt_comps + 1
            # Compare smallestValue with the rest of the values
            # This is to check for any values which is smaller than the current position set value.

            if(smallValue > arr[j]):
                # swap the indexposition to the index of newly found small value
                indexpos= j
                # Imp: Swap smallvalue with current array indexposition value.
                # This means the comparision value is changed. This works for large arrays with a complete unsorted list
                smallValue= arr[j]
        # if indexposition is not equal to original index position Swap the values
        if (indexpos!= i):
            currentvalue = arr[i]

            print('Swapping the number {} >> for the number {}'.format(arr[indexpos],arr[i]))

            arr[i], arr[indexpos] = arr[indexpos], currentvalue

            print('Current Array after swap : {} '.format(arr))

        else: # else just print No swap is performed
            print('>>> Looks like value is sorted. No Swap is performed >>>')
    print('Total iterations :{} Total Comparisions : {} Output Array is : {}'.format(cnt,cnt_comps,arr))
    return arr

# Test Long unsorted list
#arrlist = [3, 56, 2, 58, 79, 59, 34, 23, 4, 78, 8, 123, 45]
# Test short unsorted list
arrlist = [10,4,8,6,1]
# Test sorted list arrlist = [1,2,3,4,5]
print(selectionSort(arrlist))
