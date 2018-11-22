#Ths imports the tkinter "tool box" this contains all the support material to make GUI elements.
#By inclusing " as tk " er are giving a short name to use
import tkinter as tk
#With the login page all elements are vertucally aligned so I am just goign to use pack



#Main Window
root = tk.Tk() #creates the standard main window
#Tk() is a special function called a CONSTRUCTOR. 
#If a function is written with a capital letter it indicates it is a constructor
labUN = tk.Label(root, text = "username")
#ordered parameters: the order we send them matters. (COMMON)
#named parameters: JavaScript and Python specific
labUN.pack()

entUN = tk.Entry(root)
entUN.pack(padx = 10)

labPassword = tk.Label(root, text = "Password")
labPassword.pack()

entPassword = tk.Entry(root, show="*")
entPassword.pack()

btnSubmit = tk.Button(root, text = "Submit")
btnSubmit.pack()



#We are writing an EVENT DRIVE PROGRAM
#Build the GUI
#Start it running
#Wait for "EVENT"
root.mainloop() #Starts the program