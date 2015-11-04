class Partner():

	def __init__(self,rootid):
		self.left = None
		self.right = None
		self.rootid = rootid

	def getLeftChild(self):
		return self.left
	def getRightChild(self):
		return self.right
	def setNodeValue(self,value):
		self.rootid = value
	def getNodeValue(self):
		return self.rootid

	def insertRight(self,newNode):
		if self.right == None:
			self.right = Partner(newNode)
		else:
			tree = Partner(newNode)
			tree.right = self.right
			self.right = tree

	def insertLeft(self,newNode):
		if self.left == None:
			self.left = Partner(newNode)
		else:
			tree = Partner(newNode)
			self.left = tree
			tree.left = self.left


def printTree(tree):
	if tree != None:
		printTree(tree.getLeftChild())
		print(tree.getNodeValue())
		printTree(tree.getRightChild())


def testTree():
	myTree = Partner("Maud")
	myTree.insertLeft("Bob")
	myTree.insertRight("Tony")
	myTree.insertRight("Steven")
	printTree(myTree)
  

class node(object):
	def __init__(self, value, children = []):
		self.value = value
		self.children = children

	def __repr__(self, level=0):
		ret = "\t"*level+repr(self.value)+"\n"
		for child in self.children:
			ret += child.__repr__(level+1)
		return ret

tree = node("grandmother", [
	node("daughter", [
		node("granddaughter"),
		node("grandson")]),
	node("son", [
		node("granddaughter"),
		node("grandson")])
	]);