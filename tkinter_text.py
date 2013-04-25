from tkinter import *
import dlgCalendar2 as dlgCal
import time

global e1_text, e2_text, e3_text, e4_text, e5_text

master = Tk()
master.title("New Task")    # Title of the GUI

"""class GUI():
	def __init__(self, textFile = "schedule.txt"):

        self.schedule = textFile
"""

# Getting the current date
year = time.localtime()[0]
month = time.localtime()[1]
day = time.localtime()[2]
strdate = (str(month) +  "/" + str(day) + "/" + str(year))

# Setting variables for the calendar icon
height = 13
width = 13
photo = PhotoImage(file = "cal_icon.gif") # Calendar icon

def close_window():
    # Getting all the information out of the GUI and closing it
    e1_text = e1.get() # Task name information
    e2_text = e2.get() # Due date information
    e3_text = e3.get() # Requested start date information
    e4_text = e4.get() # Requested end date information
    e5_text = e5.get() # Hours in task information

    # Setting priority
    if v1.get() == 1:
        priority = "1"
    elif v2.get() == 2:
        priority = "2"
    elif v3.get() == 3:
        priority = "3"
    elif v4.get() == 4:
        priority = "4"
    elif v5.get() == 5:
        priority = "5"
    else:
        priority = None

    # Setting check variable
    if check.get() == 1:
        checkYes = True
    else:
        checkYes = False

    # Closing the window
    master.destroy()

def fnCalendar():
    # Opening the calendar
    d1 = dlgCal.tkCalendar(master, year, month, day, StringVar())
    return(strdate)

check = IntVar()

########## Task entry ##########
Label(master,text="Enter Task:").grid(row=0,sticky=W,)
e1_entry = StringVar()
e1 = Entry(master,textvariable=e1_entry)
e1.grid(row=0,column=1,columnspan=5)

########## Due date entry ##########
Label(master,text="Enter Due Date:").grid(row=1,sticky=W)
e2_entry = StringVar()
e2 = Entry(master,textvariable=e2_entry)
cal1 = Button(master,height=height,width=width, image = photo,command=fnCalendar).grid(row=3,column=5,sticky=W,padx=10)
'''
print(dlgCal.tkCalendar())
e2.insert(0, dlgCal.tkCalendar()) 
'''
e2.grid(row=1,column=1,columnspan=5)

########## Priority entry ##########
Label(master,text="Priority:").grid(row=2,sticky=W)
# Initializing the priority variables
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
# Making the buttons for the priority
Radiobutton(master,text=str(1),variable=v1,value=1).grid(row=2,column=1)
Radiobutton(master,text=str(2),variable=v2,value=2).grid(row=2,column=2)
Radiobutton(master,text=str(3),variable=v3,value=3).grid(row=2,column=3)
Radiobutton(master,text=str(4),variable=v4,value=4).grid(row=2,column=4)
Radiobutton(master,text=str(5),variable=v5,value=5).grid(row=2,column=5)

########## Hours in task entry ##########
Label(master,text="Hours In Task:").grid(row=3,sticky=W)
e5_entry = StringVar()
e5 = Entry(master,textvariable=e5_entry)
e5.grid(row=3,column=1,columnspan=5)

########## Requested start date entry ##########
Label(master,text="Requested Start Date:").grid(row=4,sticky=W)
e3_entry = StringVar()
e3 = Entry(master,textvariable=e3_entry)
e3.grid(row=4,column=1,columnspan=5)
cal2 = Button(master,height=height,width=width, image = photo,command=fnCalendar).grid(row=1,column=5,sticky=W,padx=10)

########## Requested end date ##########
Label(master,text="Requested End Date:").grid(row=5,sticky=W)
e4_entry = StringVar()
e4 = Entry(master,textvariable=e4_entry)
e4.grid(row=5,column=1,columnspan=5)
cal3 = Button(master,height=height,width=width, image = photo,command=fnCalendar).grid(row=4,column=5,sticky=W,padx=10)

########## Buttons ##########
#Check button if you want to enter another task immediately
Checkbutton(master,text="Submit another",variable=check,onvalue=1,offvalue=0).grid(row=6,sticky=W,padx=10)
#Submit button, which saves information from GUI and closes window
b1 = Button(master,text="Submit",command=close_window).grid(row=6,sticky=E,column=4,padx=10)

mainloop()