class Node:
    def __init__(self,data):
        self.data = data
        self.link = None

node1 = Node(1)     
node2 = Node(2)
node3 = Node(3)



node1.link = node2
node2.link = node3

head = node1


currentNode = head
#traversing

while currentNode :
    print(currentNode.data ,end=" =>")
    currentNode = currentNode.link
print("none")    


