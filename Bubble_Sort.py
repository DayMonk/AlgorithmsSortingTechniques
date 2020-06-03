# Function to demonstrate bubble sort technique
def bubbleSort(alist):
    length = len(alist)
    # Counter is used only for displaying iteration count
    cnt = 0

    for i in range(length):
        # Check the element pairs for correct Order. 'n' elements will yield n-1 iterations to achieve sorted list
        cnt = cnt+1
        isSwapped = False
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print(" Iteration : {} starting array is {} ".format(cnt,alist))
        for j in range(length-i-1):
            # now, compare the elements to probe the order. Example : First element pair is compared
            print ("Now Comparing >> {} with {} : ".format(alist[j],alist[j+1]))
            if alist[j] > alist[j+1]:
                # swap the elements. For clarity purposes the swapping is shown in seperate steps
                # Use a Temp variabe to store the first element number in a element pair ex (1,2), temp will store value 1
                # Temp variable is not required for swapping, is used only for understanding the swap logic
                temp = alist[j]
                # swap first element in pair with second element
                alist[j] = alist[j+1]
                # swap second element in pair with first element
                alist[j+1]= temp
                # As the element pair is sorted set it to true
                isSwapped = True
            if isSwapped :
                print(" Array is modified as {} ".format(alist))
            else:
                print(" Array is not modified {} ".format(alist))
            # Increase the counter to process into next element pair
        print( 'Iteration {} ending array {} : '.format(cnt,alist))
        print( ' is array Swapped atleast Once in the Iteration >> {} '.format(isSwapped))
        if isSwapped == False:
            break
    return alist

alist = [10,4,8,6,1]
print(bubbleSort(alist))