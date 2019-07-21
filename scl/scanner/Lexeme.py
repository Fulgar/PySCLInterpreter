# Name: Jason James
# Course: CS 4308
# Section: W01
# Assignment: Project Deliverable 1
# Date: 7/12/19

class Lexeme:

	# Constructor
	# Parameters: lexStr : lexeme string , token :  Token object
	def __init__(self, lexStr, token):
		self.lexStr = lexStr
		self.token = token

	def getLexemeString(self):
		return self.lexStr

	def getToken(self):
		return self.token
