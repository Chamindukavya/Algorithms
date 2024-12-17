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

    def deleteNode(self,value,head):
      
        if head == None:
            return head
        
        if value < head.data:
            head.left = self.deleteNode(value,head.left)
        elif value > head.data:
            head.right = self.deleteNode(value,head.right)

        else:

            if head.left == None:
                return head.right
            elif head.right == None:
                return head.left
            
        return head    

newTree = Tree()
newTree.addData(10)
newTree.addData(5),
newTree.addData(20)
newTree.addData(21)
newTree.addData(8)
newTree.deleteNode(5,newTree.head)

l2 = []
newTree.inOrderTraverse(newTree.head,l2)
print(l2)
# newTree.searchValue(l2,120,0,len(l2)-1)





