import tkinter as tk

root = tk.Tk()

root.title("Lap hockey calculator")

#DEFINITIONS#

def submit():
	print("Submit")

	try: 
		x = ent2.get()
		x = float(x)
		lb1.insert(0,ent1.get())
		lb2.insert(0,x)

		if v.get() == "1":
			player1memo.append(ent1.get())
			player1time.append(x)
			txt2.config(text = "Your Average is " + average(player1time,0) + " seconds")

		if v.get() == "2":
			player2memo.append(ent1.get())
			player2time.append(x)
			txt2.config(text = "Your Average is " + average(player2time,0) + " seconds")

		if v.get() == "3":
			player3memo.append(ent1.get())
			player3time.append(x)
			txt2.config(text = "Your Average is " + average(player3time,0) + " seconds")

		if v.get() == "4":
			player4memo.append(ent1.get())
			player4time.append(x)
			txt2.config(text = "Your Average is " + average(player4time,0) + " seconds")

		average()
		print(player1memo)
		print(player1time)
	except: 
		ent1.delete(0,tk.END)
		ent2.delete(0,tk.END)		

def average(list,a):
	
	x = sum(list)/len(list)
	
	#standard algorithm
	'''
	sum = 0
	for i in range(0, len(list),1):
		sum = sum + list[i]

	avg = sum/len(list)
	'''
	return str(x)

def change(*args):
	print(v.get())

	if v.get() == "1":
		lab1.config(text = "Player 1")

	if v.get() == "2":
		lab1.config(text = "Player 2")

	if v.get() == "3":
		lab1.config(text = "Player 3")

	if v.get() == "4":
		lab1.config(text = "Player 4")

	#How do I delete all elements in a listbox
	lb1.delete(0,tk.END)
	lb2.delete(0,tk.END)

	#THIS IS WHERE EVERYTHING GETS DELETED
	if v.get() == "1":
		for i in range(0, len(player1memo),1):
			lb1.insert(0,player1memo[i])
			lb2.insert(0,player1time[i])
			txt2.config(text = "Your Average is " + average(player1time,0) + " seconds")

	if v.get() == "2":
		for i in range(0, len(player2memo),1):
			lb1.insert(0,player2memo[i])
			lb2.insert(0,player2time[i])
			txt2.config(text = "Your Average is " + average(player2time,0) + " seconds")

	if v.get() == "3":
		for i in range(0, len(player3memo),1):
			lb1.insert(0,player3memo[i])
			lb2.insert(0,player3time[i])
			txt2.config(text = "Your Average is " + average(player3time,0) + " seconds")

	if v.get() == "4":
		for i in range(0, len(player4memo),1):
			lb1.insert(0,player4memo[i])
			lb2.insert(0,player4time[i])
			txt2.config(text = "Your Average is " + average(Player4time,0) + " seconds")

#DIFFERENT LISTS#
player1memo = []
player1time = []

player2memo = []
player2time = []

player3memo = []
player3time = []

player4memo = []
player4time = []

#index 0 is player 1, index 1 is player 2. . . etc
playerAvg = [0,0,0,0]


# RADIO BUTTONS #

MODES = [
(" Player 1 ", "1"),
(" Player 2 ", "2"),
(" Player 3 ", "3"),
(" Player 4 ", "4"),
]


v = tk.StringVar()
v.set("1")
v.trace("w",change)
root.configure(background = "SkyBlue1")



for r in range(0,len(MODES),1):
	b = tk.Radiobutton(root, text=MODES[r][0], variable=v, value=MODES[r][1], background = "DeepSkyBlue3", command = change)
	b.grid(row = 3 + r,column = 0)




# ALL WIDGETS #
lab1 = tk.Label(root, text = "PLAYERS NAME")
lab1.grid(row = 2, column = 1, columnspan = 2)

txt1 = tk.Label(root, text = "What week would you like to input time for?")
txt1.grid(row = 3, column = 1)

ent1 = tk.Entry(root)
ent1.grid(row=4, column=1)

txt3 = tk.Label(root, text = "What was the time recorded?")
txt3.grid(row = 5, column = 1)
ent2 = tk.Entry(root)
ent2.grid(row=6, column=1)

btn1 = tk.Button(root, text = "SUBMIT", command = submit)
btn1.grid(row = 7, column=1, columnspan = 2)

txt2 = tk.Label(root, text = "Your average is --")
txt2.grid(row = 7, column = 3, columnspan = 2)

lb1 = tk.Listbox(root,background='SteelBlue2')

lb1.grid(row = 3, column = 3, rowspan = 4)

lb2 = tk.Listbox(root,background = "DodgerBlue2")

lb2.grid(row = 3, column = 4,rowspan = 4)

root.mainloop()