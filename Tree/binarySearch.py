def binarySearch(A,value,start,end):
    if start == end:
        if(value == A[start]):
            print("Value is found in the array")
            return
        else:
            print("Value is not found in the array")
            return
        
    
    mid = (start+end)//2

    if(A[mid]==value):
        print("Value is found in the array")
        return
    
    elif(value < A[mid]):
        if (mid-1)<0:
            print("Value is not found in the array")
            return
        binarySearch(A,value,start,mid-1)

    elif(value > A[mid]):
        binarySearch(A,value,mid+1,end)

