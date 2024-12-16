array = [1,2,3,4,5]

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
        binarySearch(A,value,start,mid-1)

    elif(value > A[mid]):
        binarySearch(A,value,mid+1,end)

binarySearch(array,8,0,len(array)-1)

