class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(19)
node2 = Node(12)
node3 = Node(3)
node4 = Node(40)
node5 = Node(54)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def iterate_ll(node):
    current = node
    while(current):
        print(current.data, end="->")
        current = current.next
    print('null')

print('linked list:- ')
iterate_ll(node1)


print('find lowest from node:- ')
def find_lowest(node):
    min = node.data
    current = node
    while current:
        if current.data < min:
            min = current.data
        current = current.next
    print(min)

find_lowest(node1)

print('delete 4th node')
def delete_node(start, delete):
    current = start
    while current:
        if current.next == delete:
            current.next = delete.next
        current = current.next
delete_node(node1, node4)
iterate_ll(node1)

print('insert new node 4 bw 3 - 5')

def insert_new(strat, pos, new):
    current = strat
    while current:
        if current.next == pos:
            new.next = pos.next
            pos.next = new
        current = current.next

newNode = Node(100)
insert_new(node1, node3, newNode)
iterate_ll(node1)