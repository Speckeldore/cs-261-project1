class Node:
  def __init__(self, val=None):
    self.next = None
    self.val = val

#This insert function cuts off the list and needs to be fixed
def insert(value, head, index):
  cur = head
  for i in range(index):
    cur = cur.next
  newnode = Node(value)
  newnode.next = cur.next
  cur.next = newnode

def print_list(head):
  cur = head
  while cur != None:
    cur = cur.next
    if cur != None:
      print(cur.val)
  print("End of list.\n")

def remove_by_index(head,index):
  prev = head
  cur = head
  cur = cur.next
  for i in range(index):
    prev = prev.next
    cur = cur.next
  prev.next = cur.next

def remove_by_value(head,value):
  prev = head
  cur = head
  cur = cur.next
  while cur != None:
    prev = prev.next
    cur = cur.next
    if cur.val == value:
      break
  prev.next = cur.next




#Build a simple list
head = Node()
cur = head

for i in range(5):
  cur.next = Node()
  cur = cur.next
  cur.val = i

print_list(head)
insert("Hi!", head, 5)
remove_by_index(head,3)
remove_by_value(head,2)
#This should print 0, 1, 2, Hi!, 3, 4, End of list. but our insert
#cuts off the tail of the list
print_list(head)