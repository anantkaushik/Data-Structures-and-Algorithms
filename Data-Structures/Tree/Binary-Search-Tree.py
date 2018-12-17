"""
----------------------- Binary Search Tree ------------------------
"""
class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.data = val

class Binary_Tree:
	def __init__(self):
		self.root = None

	def getRoot(self):
		return self.root.data

	def add(self, val):
		if self.root == None:
			self.root = Node(val)
		else:
			self._add(val, self.root)

	def _add(self, val, node):
		if val < node.data:
			if node.left != None:
				self._add(val, node.left)
			else:
				node.left = Node(val)
		else:
			if node.right != None:
				self._add(val, node.right)
			else:
				node.right = Node(val)

	def printTree(self, trav = "in"):
		if self.root != None:
			if trav == "in":
				self.printTree_in(self.root)
			elif trav == "pre":
				self.printTree_pre(self.root)
			elif trav == "post":
				self.printTree_post(self.root)
		
	def printTree_in(self, node):
		if node == None:
			return
		self.printTree_in(node.left)
		print(node.data)
		self.printTree_in(node.right)

	def printTree_pre(self, node):
		if node == None:
			return
		print(node.data)
		self.printTree_pre(node.left)
		self.printTree_pre(node.right)

	def printTree_post(self, node):
		if node == None:
			return
		self.printTree_post(node.left)
		self.printTree_post(node.right)
		print(node.data)

bTree = Binary_Tree()
bTree.add(6)
bTree.add(4)
bTree.add(8)
bTree.add(10)
bTree.add(3)
bTree.add(5)
bTree.printTree("pre") # 6 4 3 5 8 10
print("----------------")
bTree.printTree("in") # 3 4 5 6 8 10
print("----------------")
bTree.printTree("post") # 3 5 4 10 8 6
