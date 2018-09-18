import os

#Loop Structure 
#Two types of loops
#Counted loops: We know in advance how many times something should run for loops
#Conditional loops: We don't know how many times sonthing will run before entering the loop while loops
while (True):
	statement = input("What would you like me to say: ")
	os.system("say "+statement)