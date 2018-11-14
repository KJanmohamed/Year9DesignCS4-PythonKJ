import tkinter as tk

def submit():
	print("Submit pressed")
	list.append(ent.get())

	#convert list to a string
	str = ""
	for i in range(0, len(list),1):
		str = str + list[i] + " "
	lb.config(text = str)

#This function will parse a string and
#add a new element to the list for all
#values 



#creates an empty list
list = []

root = tk.Tk()

lab = tk.Label(root, text = "Input Food")
lab.pack()

ent = tk.Entry(root)
ent.pack()

btn = tk.Button(root, text = "Submit", command = submit)
btn.pack()

lb = tk.Label(root, text = "")
lb.pack()

root.mainloop()