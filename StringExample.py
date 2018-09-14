#This file will go through the basics of String manipulation

#Strings are collections of characters
#Strings are encclosed in "" or ''
# "Kalen"
# "Kalen is cool"
# "Kalen is cool!"
#Two things we need to talk about when we think about strings
#index - always starts at 0
#length

#Example
#  01234	 012345
# "Kalen" 	"Monkey"
#len("Kalen") = 5
#len("Monkey") = 6

name = "Kalen"

print(name) #I can print strings
sentence = name + " is cool!" # connection is adding string
print(sentence)
print(sentence + "!")

#I can access specific letters 
fLetter = name[0] #name at 0
letters1 = name[0:2] #inclusive:exclusive
print(letters1)
letters2 = name[2:]
print(letters2)

letters2a = name[2:len(name)]
print(letters2a) #formal way of writing letters

letters3 = name[:2]
print(letters3)

lname = len(name) #length of string
print(lname)

#if I want to print out all letters
for i in range(len(name)):
	print(name[i])