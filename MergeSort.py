def merge_sort(sort_list):
    arrlength = len(sort_list)
    print(' Input Array : {} >> Current Array Length : {} '.format(sort_list,arrlength))
    
    if (arrlength <= 1):
        print('** Array Length should be more than 1 to perform Merge Sort ** ')
        return
    
    if arrlength > 1:
        
        # derive the midpoint of the array
        mid = arrlength // 2
        print(" Mid Index value is : {}".format(mid))
        # divide the array into left Half and Right Half based on the midpoint
        leftHalf = sort_list[:mid]
        rightHalf = sort_list[mid:]
        print(" lefthalf : {}  >> rightHalf : {} ".format(leftHalf,rightHalf))

        # Recursive call on right and left half, First complete the leftHalf followed by rightHalf
        merge_sort(leftHalf)
        merge_sort(rightHalf)
        
        # Iterator i for traversing through the Left Half of the array
        i = 0
        # Iterator j for traversing through the Right Half of the array
        j = 0
        # Iterator k for the main list
        k = 0
        
        while i < len(leftHalf) and j < len(rightHalf):
            
            # compare the lefthalf index value for iterator i with rightHalf index value for iterator j
            if leftHalf[i] < rightHalf[j]:
                #assign the sort_list index k value as leftHalf index i value to it's sorted position
                sort_list[k] = leftHalf[i]
                #increment the i iterator to next position
                i = i + 1
            else: #in else condition if the rightHalf value is less than Left Half index position value. 
                #assign the sort_list index k value as RightHalf index j value to it's sorted position
                sort_list[k] = rightHalf[j]
                #increment the j iterator to next position
                j = j + 1
            # increment the K iterator to check for next value in both the halves
            k = k + 1
        # New loop for any remaining values which are left out of the above check on leftHalf side
        print(" Iterating through remaining lefthalf : {} ".format(leftHalf)) 
        while i < len(leftHalf):
            sort_list[k] = leftHalf[i]
            i = i + 1
            k = k + 1
        # New loop for any remaining values which are left out of the above check on RightHalf side
        print(" Iterating through remaining righthalf : {} ".format(rightHalf)) 
        while j < len(rightHalf):
            sort_list[k] = rightHalf[j]
            j = j + 1
            k = k + 1
    print("merging...", sort_list)
    return sort_list

# Test Long unsorted list
#arrlist = [3, 56, 2, 58, 79, 59, 34, 23, 4, 78, 8, 123, 45]
# arrlist = []
# Test short unsorted list
arrlist = [10,4,8,6,1,3]
#Test sorted list 
#arrlist = [1,2,3,4,5]
#Test n= 100 unsorted list
#arrlist = [52,68,84,73,3,81,91,58,1,19,8,78,32,94,4,98,23,6,21,20,43,69,31,87,33,62,36,41,70,51,48,38,72,24,47,57,13,7,64,49,9,16,14,99,90,92,35,25,37,89,50,85,76,67,88,131,39,56,74,42,77,26,93,97,80,82,96,60,53,46,18,65,30,27,2,83,66,29,61,10,55,22,11,75,95,45,59,86,12,15,17,79,40,34,5,71,44,63,28,54]
print(merge_sort(arrlist))