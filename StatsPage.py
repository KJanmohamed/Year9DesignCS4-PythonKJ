import tkinter as tk


root = tk.Tk()

output = tk.Text(root, height = 10, width = 50)
output.config(state = "disable")
output.grid(row = 0, column = 0, columnspan = 2)

btn1 = tk.Button(root, height = 1, width = 10, text = "Button 1")
btn1.grid(row = 1, column = 0)



root.mainloop()