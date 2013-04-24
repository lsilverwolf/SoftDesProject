"""Creates a GUI class for user input. It includes
--getNewEvent() to query the user for a new event to add
--displayEvents() to show the user a list of the events already created

"""

from tkinter import *
import dlgCalendar2 as dlgCal
import time


class GUI():
	def __init__(self, textFile = "schedule.txt"):

        self.schedule = textFile


    self.year = time.localtime()[0]
    self.month = time.localtime()[1]
    self.day = time.localtime()[2]
    self.strdate = (str(self.month) +  "/" + str(self.day) + "/" + str(self.year))

    def close_window():
        master.destroy()

    def fnCalendar():
        d1 = dlgCal.tkCalendar(master, self.year, self.month, self.day, StringVar())
        return(self.strdate)

    master = Tk()
    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()
    v5 = IntVar()
    CheckVar = IntVar()

    master.title("New Task")

    Label(master,text="Enter Task:").grid(row=0,sticky=W,)
    e1_entry = StringVar()
    e1 = Entry(master,textvariable=e1_entry)
    e1.grid(row=0,column=1,columnspan=5)
    e1_text = e1.get()


    Label(master,text="Enter Due Date:").grid(row=1,sticky=W)
    e2 = Entry(master)
    '''
    print(dlgCal.tkCalendar())
    e2.insert(0, dlgCal.tkCalendar()) 
    '''
    e2.grid(row=1,column=1,columnspan=5)

    Label(master,text="Priority:").grid(row=2,sticky=W)

    Label(master,text="Hours In Task:").grid(row=3,sticky=W)
    e5 = Entry(master)
    e5.grid(row=3,column=1,columnspan=5)

    Label(master,text="Requested Start Date:").grid(row=4,sticky=W)
    e3 = Entry(master)
    e3.grid(row=4,column=1,columnspan=5)

    Label(master,text="Requested End Date:").grid(row=5,sticky=W)
    e4 = Entry(master)
    e4.grid(row=5,column=1,columnspan=5)

    Radiobutton(master,text=str(1),variable=v1,value=1).grid(row=2,column=1)
    Radiobutton(master,text=str(2),variable=v1,value=2).grid(row=2,column=2)
    Radiobutton(master,text=str(3),variable=v1,value=3).grid(row=2,column=3)
    Radiobutton(master,text=str(4),variable=v1,value=4).grid(row=2,column=4)
    Radiobutton(master,text=str(5),variable=v1,value=5).grid(row=2,column=5)

    height = 13
    width = 13

    photo = PhotoImage(file = "cal_icon.gif")
    cal1 = Button(master,height=height,width=width, image = photo,command=fnCalendar).grid(row=3,column=6,sticky=W,padx=10)
    cal2 = Button(master,height=height,width=width, image = photo,command=fnCalendar).grid(row=1,column=6,sticky=W,padx=10)
    cal3 = Button(master,height=height,width=width, image = photo,command=fnCalendar).grid(row=4,column=6,sticky=W,padx=10)

    check1 = Checkbutton(master,text="Submit another",variable=CheckVar1,onvalue=1,offvalue=0).grid(row=6,sticky=W,padx=10)
    b1 = Button(master,text="Submit",command=close_window).grid(row=6,sticky=E,column=4,padx=10)


print("I got here")
print(e1_text)
print(type(e1_text))
print("Now I'm after")
