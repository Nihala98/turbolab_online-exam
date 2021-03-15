def findRock(arr, size) :
    right_weightsum, left_weightsum = 0, 0
 # calculating sum of weights of rocks from right
    for i in range(1, size) :
        right_weightsum += arr[i]
    i, j = 0, 1
 
    # Checking the position of rock
    #in which the sum of weight of rocks from left equal sum of weight of rocks from left
    # i.e. left_weightSum == right_weightsum 
    while j < size :
        right_weightsum -= arr[j]
        left_weightsum += arr[i]
 
        if left_weightsum == right_weightsum :
            return arr[i + 1]
        j += 1
        i += 1
 
    return -1
if __name__ == "__main__" :
#assuming 2,1,7,1,4,6 are the weights of rocks in a straight line    
    arr = [ 2, 1, 7, 1, 4, 6]
    n = len(arr)
    print(findRock(arr, n))
 
   

