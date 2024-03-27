# Python program to create a table

from tkinter import *


class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=20, fg='black',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


# take the data
lst = [('Assignment Average','assavg'),
	('Homework Average','hwavg'),
	('Quiz Average','quizavg'),
	('Exam Average','examavg'),
	('Class Average','classavg')]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])


# create root window
root = Tk()

t = Table(root)
#root.mainloop()

#BUTTON
# create a tkinter window
root = Tk()              
 
# Open window having dimension 100x100
root.geometry('100x100') 
 
# Create a Button
btn = Button(root, text = 'Click me !', bd = '5',
                          command = root.destroy) 
 
# Set the position of button on the top of window.   
btn.pack(side = 'top')    
 
root.mainloop()