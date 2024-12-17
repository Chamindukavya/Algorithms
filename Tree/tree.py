import binarySearch
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None


class Tree:
    
    def __init__(self):
        self.head = None

    def addData(self,data):
        current = self.head
        if current == None:
            newNode = Node(data)
            self.head = newNode
            return
        flag = True
        current = self.head
        while flag:
            if current.data>=data:

                if current.left == None:
                    newNode = Node(data)
                    current.left = newNode
                    flag = False
                    
                else:
                    current = current.left
            elif current.data<data:
               
                if current.right == None:
                    newNode = Node(data)
                    current.right = newNode
                    flag = False

                else:
                    current = current.right

    def inOrderTraverse(self,node,l3):
       

        if node is None:
            return 
         
        self.inOrderTraverse(node.left,l3) 
        l3.append(node.data)
        self.inOrderTraverse(node.right,l3)

        return l3

    def searchValue(self,A,value,start,end):
        binarySearch.binarySearch(A,value,start,end)    

     
         

newTree = Tree()
newTree.addData(10)
newTree.addData(5),
newTree.addData(20)
newTree.addData(21)
newTree.addData(8)

l2 = []
newTree.inOrderTraverse(newTree.head,l2)
print(l2)
newTree.searchValue(l2,120,0,len(l2)-1)





