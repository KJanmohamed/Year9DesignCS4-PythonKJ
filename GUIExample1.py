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

root.mainloop()