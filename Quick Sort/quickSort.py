Array = [10, 14, 28, 11, 7, 16, 30, 50, 25, 18]


endOriginal = len(Array)-1

def quickSort(A,start,end):
    if(start < end):
        pindex = partition(A,start,end)
        
        quickSort(A,start,pindex-1)
        print("pIndex second ",pindex)
        quickSort(A,pindex+1,end)
        
def partition(A,start,end):
    pivot = A[end]
    pindex = start
    print("Partition is: ",A[start:end+1])

    for i in range(start,end): 
        if (A[i]<= pivot):

            A[i],A[pindex] = A[pindex],A[i]
            pindex+=1

    A[end],A[pindex] = A[pindex],A[end]
    print("Pindex: ",pindex)
    return pindex

quickSort(Array,0,len(Array)-1)
print("Sorted Array is",Array)
sortedArray = [1,2,3,4,5,6,7,8]

if Array == sortedArray:
    print("Sorted Success")