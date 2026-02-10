class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)


node1.next = node2
node2.next = node3
node3.next = node4


head = node1

current = head

while current:
    print(current.data,end="  ->")
    current = current.next

print("None")

temp = int(input("Enter the key value to search: "))

current = head
pos = 1

while current:
    if current.data == temp:
        print(f"Found key value {temp} at position {pos}")
    current = current.next
    pos += 1







    

       