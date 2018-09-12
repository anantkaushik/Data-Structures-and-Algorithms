"""
------------------------ Singly Linked List -------------------------
"""
class node:
	def __init__(self, data = None):
		self.data = data
		self.next = None

class singly_linked_list:
	def __init__(self):
		self.head = node()

	def append(self, data):
		new_node = node(data)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_node

	def length(self):
		cur = self.head
		count = 0
		while cur.next != None:
			count += 1
			cur = cur.next
		return count

	def display(self):
		elements = []
		cur = self.head
		while cur.next != None:
			cur = cur.next
			elements.append(cur.data)
		return elements

	def get(self, index):
		if index >= self.length():
			return "ERROR : index out of range!"
		idx = 0
		cur = self.head
		while cur.next != None:
			cur = cur.next
			if idx == index:
				return cur.data
			idx += 1

	def delete(self, index):
		if index >= self.length():
			return "ERROR : index out of range!"
		idx = 0
		cur = self.head
		while cur.next != None:
			last_node = cur
			cur = cur.next
			if idx == index:
				last_node.next = cur.next
				return "Node Deleted"
			idx += 1

	def insert(self, index, value):
		if index > self.length():
			return "ERROR : index out of range!"
		elif index == self.length():
			self.append(value)
			return "Node Added"
		new_node = node(value)
		idx = 0
		cur = self.head
		while cur.next != None:
			last_node = cur
			cur = cur.next
			if idx == index:
				last_node.next = new_node
				new_node.next = cur
				return "Node Added"
			idx += 1