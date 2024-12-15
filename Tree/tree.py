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

    def inOrderTraverse(self,node):
        
        if node is None:
            return
         
        self.inOrderTraverse(node.left) 
        print(node.data)
        self.inOrderTraverse(node.right)

     
         

newTree = Tree()
newTree.addData(10)
newTree.addData(5)
newTree.addData(20)
newTree.addData(21)

newTree.addData(8)
newTree.inOrderTraverse(newTree.head)


