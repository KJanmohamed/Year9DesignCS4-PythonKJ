import tkinter as tk
#MISKEW COMMENTS

#1. ALL VARIABLES SHOUDL BE LOWER CASE. (GRAMMER THING)

root = tk.Tk()

#Data Fields
#If you ahve variables that you need to keep track of they MUST BE LISTS!


def submit():
	print("Submit")

	try: 
		x = ent2.get()
		x = int(x)
		lb1.insert(0,ent1.get())
		lb2.insert(0,x)

		if v.get() == "1":
			player1memo.append(ent1.get())
			player1time.append(x)
		if v.get() == "2":
			player2memo.append(ent1.get())
			player2time.append(x)

		print(player1memo)
		print(player1time)
	except: 
		ent1.delete(0,tk.END)
		ent2.delete(0,tk.END)		


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

	#Put all of hte player 2 back in 
	if v.get() == "1":
		for i in range(0, len(player1memo),1):
			lb1.insert(0,player1memo[i])
			lb2.insert(0,player1time[i])



player1memo = []
player1time = []

player2memo = []
player2time = []


MODES = [
("Player1", "1"),
("Player2", "2"),
("Player3", "3"),
("Player4", "4"),
]


v = tk.StringVar()
v.set("1")
v.trace("w",change)
root.configure(background = "SkyBlue1")



for r in range(0,len(MODES),1):
	b = tk.Radiobutton(root, text=MODES[r][0], variable=v, value=MODES[r][1], background = "DeepSkyBlue3", command = change)
	b.grid(row = 3 + r,column = 0)





lab1 = tk.Label(root, text = "PLAYERS NAME")
lab1.grid(row = 2, column = 1, columnspan = 2)

txt1 = tk.Label(root, text = "Please Input your time for this Week")
txt1.grid(row = 3, column = 1)

ent1 = tk.Entry(root)
ent1.grid(row=4, column=1)

ent2 = tk.Entry(root)
ent2.grid(row=5, column=1)

btn1 = tk.Button(root, text = "SUBMIT", command = submit)
btn1.grid(row = 6, column=1, columnspan = 2)

txt2 = tk.Label(root, text = "Your average until week 4 is ")
txt2.grid(row = 7, column = 1, columnspan = 2)


lb1 = tk.Listbox(root,background='SteelBlue2')

lb1.grid(row = 3, column = 3, rowspan = 4)

lb2 = tk.Listbox(root,background = "DodgerBlue2")

lb2.grid(row = 3, column = 4,rowspan = 4)

root.mainloop()