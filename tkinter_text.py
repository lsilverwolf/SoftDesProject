from tkinter import *

master = Tk()

def close_window():
    # Destroying your main window (root)
    master.destroy()

Label(master,text="Enter Task:").grid(row=0,sticky=W,)
Label(master,text="Enter Due Date:").grid(row=1,sticky=W)
Label(master,text="Priority:").grid(row=2,sticky=W)
Label(master,text="Requested Start Date:").grid(row=3,sticky=W)
Label(master,text="Requested End Date:").grid(row=4,sticky=W)



e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=2,column=3)

b1 = Button(master,text="Submit",command=close_window).grid(row=3,sticky=E,column=3,padx=30)

mainloop()