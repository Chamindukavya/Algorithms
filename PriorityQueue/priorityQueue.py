data = [16,14,8,10,1,3,9,2,4,7]

def maxHeapify(A,i):
    l = (i*2)+1
    r = (i*2)+2

    largest = i

    if(l<=(len(A)-1) and A[l]>A[i]):
        largest = l
    elif(r<=(len(A)-1) and A[r]>A[i]):
        largest = r
    ##print("largest" , largest)
    if(largest != i):
        print("A[L]",A[l])
        ##print("A[r]",A[r])
        A[largest],A[i] = A[i],A[largest]
        ##print("on road ", A)
        maxHeapify(A,largest)





def buildHeap(A):
    heapSize = len(A) - 1
    startIndex = (heapSize-1)//2
    ##print(startIndex)
    for i in range(startIndex,-1,-1):
        ##print(i)
        maxHeapify(A,i)
    print(A)

buildHeap(data)