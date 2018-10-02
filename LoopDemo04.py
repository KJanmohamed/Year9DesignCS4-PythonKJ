#A loop is a programming structure that can repeat a section of code
#A loop can run the same code exactly over and over again or with ome thought it can generate a pattern

#There are two broad catagries of loops
# Conditional loops (while): These loop as a long as a condition is true

#Counted loops (for): These loop using a counter to keep track of how many the loop has run
#
#
#
# You can use any loop in any situation, but usually from a design perspective there is a better loop in terms of coding
#
#If you know in advance how many times a loop should run a COUNTED LOOP is usually the better choice
#
#If you dont know how many times a loop should run a CONDTIONAL LOOP is usually the better choice



print("*******************************************")
#Taking Input


word="" #We have to declare and initialize 

#A while loop evaluates a condition when it is first reached
#If the condition is true it enters the loop block
while len(word) <6 or word.isalpha() == False:
#Loop block
#When we reach the bottom of the loop block we check the condition again. If it is true, we go back to the top of the block and run it again.
	while len(word) <6:

		word = input("Please input a word larger than 5 letters: ")
		print(word.isalpha())
		if (len(word) <6):
			print("Dude, I said more than 5 letters!!!!!!!!!")

		if (word.isalpha() == False):
			print("Dude, I said a real word!!!")
		#When we reach the bottom of the loop block we check the codition again, If it is true, we go back to the top of the block and run it again.

	print(word+" is a seriously long word!")