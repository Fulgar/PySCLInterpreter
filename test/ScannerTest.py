# Name: Jason James
# Course: CS 4308
# Section: W01
# Assignment: Project Deliverable 1
# Date: 7/12/19

from scl.scanner.SCL_Scanner import SCL_Scanner
from datetime import datetime

# Enter absolute path of sample.scl file location here
inputPath = "C:\\Users\\Jason\\PycharmProjects\\CS4308_W01_JasonJames_Project\\test\\sample.scl"

#Path of output file
outputPath = "ScannerTestOutput.txt"

#Output file
testFile = open(outputPath, "w")




# Creates Scanner object which contains Lexical Analysis data on SCL file input
scanner = SCL_Scanner(inputPath)

# Performs Lexical Analysis
# scanner.scan() # REMOVED: The SCL_Scanner object now calls scan in constructor

testFile.write("Log Time: " + str(datetime.now()) + "\n")
testFile.write("="*50)
for scanLine in scanner.getScanLines():
	lexemes = scanLine.getLexemes()
	lineNumber = scanLine.getLineNum()
	lineString = scanLine.getLineStr()
	testFile.write("\n" + "-"*40)
	labelText = "\nLine " + str(lineNumber) + ": " + lineString + "\n"
	testFile.write(labelText)
	for lexeme in lexemes:
		lexemeStr = lexeme.getLexemeString()
		token = lexeme.getToken()
		# print("Lexeme: ", lexemeStr, "\tToken: ", str(token.name))
		#rowText = "Lexeme: {:15} \t Token: {}".format(lexemeStr, token.name)
		testFile.write("Lexeme: {:15} \t Token: {}\n".format(lexemeStr, token.name))
	bottomFormatText = "-"*40 + "\n\n"
	testFile.write(bottomFormatText)


