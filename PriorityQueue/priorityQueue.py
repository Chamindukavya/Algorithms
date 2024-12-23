data = [8,7,6,5,4,3,2,1]

def maxHeapify(A,i):
    l = (i*2)+1
    r = (i*2)+2

    if(l<=(len(A)-1) and A[l]>A[i]):
        largest = l
    else:
        largest = i

    if(r<=(len(A)-1) and A[r]>A[largest]):
        largest = r
    if(largest != i):
        A[largest],A[i] = A[i],A[largest]
        maxHeapify(A,largest)

def buildHeap(A):
    heapSize = len(A) - 1
    startIndex = (heapSize-1)//2
    for i in range(startIndex,-1,-1):
        maxHeapify(A,i)
    print("heap",A)


def getMax(A):
    return A[0]

def extractMax(A):
    max = A[0]
    A[0] = A[len(A)-1]
    A.pop()
    buildHeap(A)
    
    return max


buildHeap(data)
print(getMax(data))
print(extractMax(data))