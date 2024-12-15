class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.allHead = None  # Root of the tree

    def addData(self, data):
        newNode = Node(data)
        if self.allHead is None:
            # If the tree is empty, set the new node as the root
            self.allHead = newNode
            return

        # Traverse the tree to find the correct location
        current = self.allHead
        while True:
            if data <= current.data:
                # Go to the left subtree
                if current.left is None:
                    current.left = newNode
                    break
                else:
                    current = current.left
            else:
                # Go to the right subtree
                if current.right is None:
                    current.right = newNode
                    break
                else:
                    current = current.right

    def printTree(self, node):
        # A simple in-order traversal to display the tree structure
        if node is not None:
            self.printTree(node.left)
            print(node.data, end=" ")
            self.printTree(node.right)


# Example usage
newTree = Tree()
newTree.addData(10)
newTree.addData(5)
newTree.addData(20)
newTree.addData(21)
newTree.addData(8)

# Print the tree
newTree.printTree(newTree.allHead)
