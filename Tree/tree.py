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

    def findSuccesor(self,node,l3):
        l4 = []
        l4 = self.inOrderTraverse(node,l3)
        minNode = min(l4)
        #print("min val is ",minNode)
        return minNode
        

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
            else:
                array1 = []
                minNode = self.findSuccesor(head.right,array1)
                head.data  = minNode
                head.right = self.deleteNode(minNode,head.right)
        print(head.data)
        return head    

    def updateValue(self,node,value1,value2):

        if node == None:
            return

        self.updateValue(node.left,value1,value2)
        if node.data == value1:
            node.data = value2
        self.updateValue(node.right,value1,value2)
        if node.data == value1:
            node.data = value2



newTree = Tree()
newTree.addData(10)
newTree.addData(5),
newTree.addData(20)
newTree.addData(21)
newTree.addData(8)
newTree.addData(15)
# temp = newTree.deleteNode(10,newTree.head)
# print(temp.data)  #this returns 15 becouse now 10 is replaces by 15
l2 = []
# #we can't update the tree as we wish. it will change the binary tree structure 
# newTree.updateValue(newTree.head,5,100)
newTree.inOrderTraverse(newTree.head,l2)
print(l2)

# newTree.searchValue(l2,120,0,len(l2)-1)





