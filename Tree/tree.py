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
        while flag:
            if current.data>=data:
                current = current.left
                if current == None:
                    newNode = Node(data)
                    current = newNode
                    print("Hii1")
                    flag = False
                    
                else:
                    continue
            elif current.data<data:
                current = current.right
                if current == None:
                    newNode = Node(data)
                    current = newNode
                    print("hii2")
                    flag = False

                else:
                    continue

    def inOrderTraverse(self):
                    

newTree = Tree()
newTree.addData(10)
newTree.addData(5)
newTree.addData(20)


