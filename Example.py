import tkinter as tk
#MISKEW COMMENTS

#1. ALL VARIABLES SHOUDL BE LOWER CASE. (GRAMMER THING)
root = tk.Tk()


root.geometry('300x300+600+200')
root.title('Mean Median Mode')

mlabel = tk.Label(text='Enter number sequence \n seperated by spaces', fg='red').place(x=7,y=25)
mbutton = tk.Button(text = "Calculate" ).place(x=220, y=250)
mEntry = tk.Entry(root, ).place(x=150,y=30)

UserNumbers=input("Enter number sequence separated by spaces: ")
nums = [int(i) for i in UserNumbers.split()]

Average = mean(nums)

print ("The mean is ", Average)

Middle = median(nums)

print ("The median is ", Middle)

if len(set(nums)) == len(nums):
    print("There is no mode ")
else:
    Most = mode(nums)
    print ("The mode is ", Most)