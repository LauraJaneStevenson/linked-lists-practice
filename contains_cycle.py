class Node(object):

	def __init__(self,value,nxt = None):

		self.value = value
		self.nxt = nxt

	def __repr__(self):

		return f"Node:{self.value}"

n1 = Node(1)
n4 = Node(4,n1)
n3 = Node(3,n4)
n2 = Node(2,n3)
n1.nxt = n2

print(n1.nxt.nxt)

def contains_cycle(node):

	current = node
	runner = node.nxt

	while current.nxt != None and runner.nxt != None: 
		
		if current != runner:

			current = current.nxt
			runner = runner.nxt.nxt

		else: 

			return True

	return False 

print(contains_cycle(n1))
