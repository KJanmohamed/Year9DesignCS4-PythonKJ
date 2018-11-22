import tkinter as tk

root = tk.Tk()

v = tk.IntVar()

tk.Label(root, 
        text="""Choose a 
player:""",
        justify = tk.LEFT,
        padx = 20).pack()
tk.Radiobutton(root, 
              text="Player 1",
              padx = 20, 
              variable=v, 
              value=1).pack(anchor=tk.W)
tk.Radiobutton(root, 
              text="Player 2",
              padx = 20, 
              variable=v, 
              value=2).pack(anchor=tk.W)

tk.Radiobutton(root, 
              text="Player 3",
              padx = 20, 
              variable=v, 
              value=3).pack(anchor=tk.W)

tk.Radiobutton(root, 
              text="Player 4",
              padx = 20, 
              variable=v, 
              value=4).pack(anchor=tk.W)
root.mainloop()