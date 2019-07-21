# Name: Jason James
# Course: CS 4308
# Section: W01
# Assignment: Project Deliverable 2
# Date: 7/12/19

from scl.parser.SCL_Parser import SCL_Parser
from datetime import datetime

inputPath = "C:\\Users\\Jason\\PycharmProjects\\CS4308_W01_JasonJames_Project\\test\\sample.scl"
outputPath = "ParserTestOutput.txt"

# Output file
testFile = open(outputPath, "w")

# Creates SCL_Parser object
parser = SCL_Parser(inputPath)

# Performs syntax analysis
parseTree = parser.parse()

testFile.write("Log Time: " + str(datetime.now()) + "\n")
testFile.write("="*50 + "\n")
for printLine in parser.printLines:
	testFile.write(printLine + "\n")
