# Name: Jason James
# Course: CS 4308
# Section: W01
# Assignment: Project Deliverable 2
# Date: 7/12/19


class Node:

	# Constructor
	def __init__(self, parent, scanLine, data):
		self.parent = parent
		self.children = None
		self.scanLine = scanLine
		self.data = data

	# Getter Methods for all fields
	def getParent(self):
		return self.parent

	def getChildren(self):
		return self.children

	def getScanLine(self):
		return self.scanLine

	def getData(self):
		return self.data

	# Setter Methods for all fields
	def setParent(self, parent):
		self.parent = parent

	def setChildren(self, children):
		self.children = children

	def setScanLine(self, scanLine):
		self.scanLine = scanLine

	def setData(self, data):
		self.data = data

	# Adds node object to children list
	def addChildNode(self, child):
		if self.children is None:
			self.children = []  # Convert to array from None type

		self.children.append(child)

	# Returns the distance from the root node
	def getDepth(self):
		if self.getParent() is None:
			return 0
		else:
			currentNode = self
			depth = 0
			while currentNode.getParent() is not None:
				depth += 1
				currentNode = currentNode.getParent()
			return depth