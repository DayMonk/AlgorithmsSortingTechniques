#function for merging the left and right array. Sorting will be performed

def merge(left, right, array):
    print("  ")
    print(" Merge -> array : {} Left : {} Right : {} ".format(array,left,right))
    # Iterator i for traversing through the Left Half of the array
    i = 0
    # Iterator j for traversing through the Right Half of the array
    j = 0
    # Iterator k for the main list
    k = 0

    while (i<len(left) and j<len(right)):
        # compare the lefthalf index value for iterator i with rightHalf index value for iterator j
        if(left[i]<right[j]):
            array[k] = left[i]
            i = i+1
        else:
            array[k] = right[j]
            j = j+1
        k = k+1
    # New loop for any remaining values which are left out of the above check on leftHalf side
    while(i<len(left)):
        #print (" left array is: {} ".format(left))
        array[k] = left[i]
        i = i+1
        k = k+1
    # New loop for any remaining values which are left out of the above check on RightHalf side
    while(j<len(right)):
        #print (" right array is: {} ".format(right))
        array[k] = right[j]
        j = j+1
        k = k+1
    print(" *-*-* End of merge function >> Merged array is : {} ".format(array));
    print(" ")
    return array
    
######################################################
### Function for dividing and calling merge function #
######################################################

def mergesort(array):
    arrlen = len(array)
    if(arrlen<2):
        print(" array has only one element {} - no further action ".format(array))
        return
    # derive the midpoint of the array
    mid = int(arrlen/2)
    # divide the array into left Half and Right Half based on the midpoint
    left =  array[:mid]
    right = array[mid:]
    print(" Left Half :{} Right Half : {}".format(left,right))
    print(" ")
    print(" Recursive call mergesort for left array {} ".format(left))
    print(" ---------------------------------------------------------")
    mergesort(left)
    print(" ----------------------------------------------------------")
    print(" ")
    print(" Recursive call mergesort for Right array {} ".format(right))
    print(" ----------------------------------------------------------")
    mergesort(right)
    print(" ----------------------------------------------------------")
   # print( " After MergeSort Right :{} ".format(right))
    merge(left,right,array)
    return array
 
 # test driver code    
if __name__ == '__main__': 
    # Test Long unsorted list
    # arrlist = [3, 56, 2, 58, 79, 59, 34, 23, 4, 78, 8, 123, 45]
    # arrlist = []
    # Test short unsorted list
    arrlist = [10,4,8,6,1,3]
    #Test sorted list 
    # arrlist = [1,2,3,4,5]
    #Test n= 100 unsorted list
    #arrlist = [52,68,84,73,3,81,91,58,1,19,8,78,32,94,4,98,23,6,21,20,43,69,31,87,33,62,36,41,70,51,48,38,72,24,47,57,13,7,64,49,9,16,14,99,90,92,35,25,37,89,50,85,76,67,88,131,39,56,74,42,77,26,93,97,80,82,96,60,53,46,18,65,30,27,2,83,66,29,61,10,55,22,11,75,95,45,59,86,12,15,17,79,40,34,5,71,44,63,28,54]
    print(" Input array : {}".format(arrlist))
    print(" Output array :{} ".format(mergesort(arrlist)))