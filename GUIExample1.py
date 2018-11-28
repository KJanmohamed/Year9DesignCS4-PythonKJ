import tkinter as tk

root = tk.Tk()

v = tk.IntVar()

RB1 = tk.Radiobutton(root, text="Player 1", variable=v, value=1)
RB1.grid(row = 3, column = 0)

RB2 = tk.Radiobutton(root, text="Player 2", variable=v, value=2)
RB2.grid(row = 4, column = 0)

RB3 = tk.Radiobutton(root, text="Player 3", variable=v, value=3)
RB3.grid(row = 5, column = 0)

RB4 = tk.Radiobutton(root, text="Player 4", variable=v, value=4)
RB4.grid(row = 6, column = 0)

Lab1 = tk.Label(root, text = "PLAYERS NAME")
Lab1.grid(row = 2, column = 1, columnspan = 2)

Txt1 = tk.Label(root, text = "Please Input your time for this Week", height = 10, width = 50)
Txt1.grid(row = 3, column = 1, columnspan = 2, rowspan = 2)

Ent1 = tk.Entry(root)
Ent1.grid(row=5, column=1, columnspan = 2)

Btn1 = tk.Button(root, text = "SUBMIT")
Btn1.grid(row = 6, column=1, columnspan = 2)

Txt2 = tk.Label(root, text = "Your average until week 4 is ")
Txt2.grid(row = 7, column = 0, columnspan = 3)

Lb1 = tk.Listbox(root)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.grid(row = 8, column = 1)

root.mainloop()