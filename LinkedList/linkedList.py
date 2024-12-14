class Node:
    def __init__(self,data):
      self.data = data
      self.next = None


class LinkedList:
    
    def __init__(self):
       self.head = None

    def insertAtBegin(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertAtEnd(self,data):
        current = self.head
        if current == None:
            self.insertAtBegin(data)
            return

        while(current!=None):

            if current.next == None:
                newNode = Node(data)
                current.next = newNode

                break

            else:
                current = current.next

    def insertAtIndex(self,index,data):
        current = self.head
        tempIndex = 0

        if (current == None) and index == 0:
            self.insertAtBegin(data)
            return
            
        while (current!=None):
            if(index == tempIndex):
                current.data = data
                print("Data added to the index")
                break
            else:
                current = current.next
                tempIndex=tempIndex+1
        else:
            print("Invalid Index. Please enter a valid index")


    def deleteAtBegin(self):
        if self.head == None:
            print("List is empty nothing to delete")
            return

        self.head = self.head.next    

    def deleteAtEnd(self):
        current = self.head

        if current == None:
            print("List is empty. Nothing to delete")
            return

        while(current.next.next != None):
            
            current = current.next
         
           
                
        current.next = None

    def deleteAtIndex(self,index):
   
        current = self.head
        size = 0
        if current == None:
            print("list is empty")
            return

        if index == 0:
         
            current = current.next 
            self.head = current
            return   
        while((current.next != None)):
            if index == size+1:
                current.next = current.next.next
                break
            current = current.next
            size = size +1


    def showLinkedList(self):
        current = self.head
        
        while(current!=None):
            print(current.data,end=" -> ")
            current = current.next
        print("",sep="/n")


newLinkedList = LinkedList()
newLinkedList.insertAtBegin(10)            
newLinkedList.insertAtBegin(11)            
newLinkedList.insertAtBegin(12)
newLinkedList.showLinkedList()
# newLinkedList.insertAtIndex(3,20)    
newLinkedList.insertAtEnd(21)
newLinkedList.deleteAtBegin()
newLinkedList.insertAtBegin(22)
newLinkedList.deleteAtEnd()
newLinkedList.deleteAtIndex(0)
newLinkedList.showLinkedList()


