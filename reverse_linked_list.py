

class Node(object):

	def __init__(self,data):

		self.data = data
		self.next = None

	def __repr__(self):

		return f"<Node:{self.data}>"


def reverse_linked_list(head):

	current = head
	previous = None

	while current != None:

		temp_next = current.next
		current.next = previous 
		previous = current
		current = temp_next

	return previous



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.next = n2
n2.next = n3
n3.next = n4

print(reverse_linked_list(n1).next)
