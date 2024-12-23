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

def heapSort(A):

    if (len(A) == 0):
        return
    if (len(A) == 1):
        sortedArray.append(A[0])
        return

    buildHeap(A)
    arraySize = len(A)
    while(arraySize > 0):
        A[arraySize-1],A[0] = A[0],A[arraySize-1]
        sortedArray[arraySize-1] = A[arraySize-1]
        arraySize = arraySize -1
        A.pop()
        maxHeapify(A,0)

sortedArray = [0]*len(data)
heapSort(data)
print(sortedArray)

