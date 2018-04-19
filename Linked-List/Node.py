class Node:
	next = None
	data = None

	def __init__(self, data):
		self.data = data

	def add_node(self, node):
		self.next = node

