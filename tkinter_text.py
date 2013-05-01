from tkinter import *
import time
from lifesorter import *

import tkCalendar

global e1_text, e2_text, e3_text, e4_text, e5_text, newEvent, action

def CreateGUI():
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
        # Getting all the information out of the GUI
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
        global newEvent
        newEvent = [e1_text, e2_text, priority, e5_text, e3_text, e4_text, checkYes]
        # Closing the window
        master.destroy()

    def fnCalendar1():
        calendar1 = tkCalendar.tkCalendar(master, year, month, day, StringVar())     
        date1 = calendar1.getstrdate
        if date1 is not "":
            date_1 = date1()
            e3.insert(0, date_1)
        
    def fnCalendar2():
        calendar2 = tkCalendar.tkCalendar(master, year, month, day, StringVar())
        date2 = calendar2.getstrdate
        if date2() is not "":
            date_2 = date2()
            e2.insert(0, date_2)
        
    def fnCalendar3():
        calendar3 = tkCalendar.tkCalendar(master, year, month, day, StringVar())
        date3 = calendar3.getstrdate
        if date3 is not "":
            date_3 = date3()
            e4.insert(0, date_3)

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
    cal1 = Button(master,height=height,width=width, image = photo,command=fnCalendar1).grid(row=1,column=5,sticky=W,padx=10)
    e2.grid(row=1,column=1,columnspan=5)

    ########## Priority entry ##########
    Label(master,text="Priority (choose one):").grid(row=2,sticky=W)
    # Initializing the priority variables
    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()
    v5 = IntVar()
    # Making the buttons for the priority
    Checkbutton(master,text=str(1),variable=v1,onvalue=1,offvalue=0).grid(row=2,column=1)
    Checkbutton(master,text=str(2),variable=v2,onvalue=2,offvalue=0).grid(row=2,column=2)
    Checkbutton(master,text=str(3),variable=v3,onvalue=3,offvalue=0).grid(row=2,column=3)
    Checkbutton(master,text=str(4),variable=v4,onvalue=4,offvalue=0).grid(row=2,column=4)
    Checkbutton(master,text=str(5),variable=v5,onvalue=5,offvalue=0).grid(row=2,column=5)

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
    cal2 = Button(master,height=height,width=width, image = photo,command=fnCalendar2).grid(row=4,column=5,sticky=W,padx=10)

    ########## Requested end date ##########
    Label(master,text="Requested End Date:").grid(row=5,sticky=W)
    e4_entry = StringVar()
    e4 = Entry(master,textvariable=e4_entry)
    e4.grid(row=5,column=1,columnspan=5)
    cal3 = Button(master,height=height,width=width, image=photo,command=fnCalendar3).grid(row=5,column=5,sticky=W,padx=10)

    ########## Buttons ##########
    #Check button if you want to enter another task immediately
    Checkbutton(master,text="Submit another",variable=check,onvalue=1,offvalue=0).grid(row=6,sticky=W,padx=10)
    #Submit button, which saves information from GUI and closes window
    b1 = Button(master,text="Submit",command=close_window).grid(row=6,sticky=E,column=4,padx=10)

    mainloop()
    return newEvent

def ModGUI():
    return modEvent

def FirstGUI():
    master = Tk()
    master.title("Choose Function")    # Title of the GUI

    def close_window():
        # Getting all the information out of the GUI
        global action
        if v1 == 1:
            action = "create"
        elif v2 == 2:
            action = "modify"
        else:
            action = None
        # Closing the window
        master.destroy()

    v1 = IntVar()
    v2 = IntVar()

    Label(master,text="Create New Event or Modify Existing Event?").grid(row=0,sticky=W)
    Checkbutton(master,text="Create",variable=v1,onvalue=1,offvalue=0).grid(row=1,column=0)
    Checkbutton(master,text="Modify",variable=v2,onvalue=2,offvalue=0).grid(row=1,column=1)
    b1 = Button(master,text="Submit",command=close_window).grid(row=2,sticky=E,column=1,padx=10)

    mainloop()
    return action
    

def main():
    #event = [task,due date,priority,hoursInTask,start date,end date,sortingRank]
    #Lifesorter has sort,add,remove,modify,get,prepareSort,getTop

    ########## Load Using Pickle ##########
    try:
        prevInfo = pickle.load(open( "save.p", "rb"))
    except:
        prevInfo = []

    myLife = Lifesorter(prevInfo)

    action = FirstGUI()
    if action == "create":
        createYes = True
        modYes = False
    else:
        createYes = False
        modYes = True


    while createYes == True:
        info = CreateGUI()
        createYes = info[6]
        myLife.addEvents(info)

    while modYes == True:
        info = CreateGUI()
        modYes = info[6]
        myLife.modifyEvents(info)

    ########## Save Using Pickle ##########
    myLifeEvents = myLife.getEvents()
    pickle.dump(myLifeEvents, open("save.p", "wb"))

main() ### RUN ALL THE THINGS ###

#                         ,,
#                         ';;
#                          ''
#            ____          ||
#           ;    \         ||
#            \,---'-,-,    ||
#            /     (  o)   ||
#          (o )__,--'-' \  ||
#,,,,       ;'uuuuu''   ) ;;
#\   \      \ )      ) /\//
# '--'       \'nnnnn' /  \
#   \\      //'------'    \
#    \\    //  \           \
#     \\  //    )           )
#      \\//     |           |
#       \\     /            |