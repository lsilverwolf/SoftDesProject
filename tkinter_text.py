from tkinter import *
import time
import pickle
from lifesorter import *

import tkCalendar

global e1_text, e2_text, e3_text, newEvent, modEvent, action, searchTerm

def CreateGUI():
    master = Tk()
    master.title("New Task")    # Title of the GUI

    # Getting the current date
    year = time.localtime()[0]
    month = time.localtime()[1]
    day = time.localtime()[2]

    # Setting variables for the calendar icon
    height = 13
    width = 13
    photo = PhotoImage(file = "cal_icon.gif") # Calendar icon

    def close_window():
        # Getting all the information out of the GUI
        e1_text = e1.get() # Task name information
        e2_text = e2.get() # Due date information
        e3_text = e3.get() # Hours in task information
        
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
        newEvent = [e1_text, e2_text, priority, e3_text, checkYes]
        # Closing the window
        master.destroy()

    def fnCalendar1():
        calendar1 = tkCalendar.tkCalendar(master, year, month, day, StringVar())
        date1 = calendar1.getstrdate()
        if date1 is not "":
            date_1 = date1    
    
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
    e2.insert(0, 'mm/dd/yyyy')

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
    e3_entry = StringVar()
    e3 = Entry(master,textvariable=e3_entry)
    e3.grid(row=3,column=1,columnspan=5)

    ########## Buttons ##########
    #Check button if you want to enter another task immediately
    Checkbutton(master,text="Submit another",variable=check,onvalue=1,offvalue=0).grid(row=6,sticky=W,padx=10)
    #Submit button, which saves information from GUI and closes window
    b1 = Button(master,text="Submit",command=close_window).grid(row=6,sticky=E,column=4,padx=10)

    mainloop()
    return newEvent

def SearchTaskGUI(myLife):
    master = Tk()
    master.title("Modify Task")    # Title of the GUI

    def close_window():
        # Getting all the information out of the GUI
        global searchTerm
        searchTerm = var.get()
        
        # Closing the window
        master.destroy()
    var = StringVar(master)
    options = myLife.getEventNames()
    var.set(options[0])
    Label(master,text="Search for task to modify:").grid(row=0,sticky=W)
    mySearch = OptionMenu(master,var,*options).grid(row=0,column=1,sticky=EW,padx=10)
    b1 = Button(master,text="Submit",command=close_window).grid(row=2,sticky=E,column=1,padx=10)
    
    mainloop()
    return searchTerm

def ModGUI(search):
    master = Tk()
    master.title("Modify Task")    # Title of the GUI

    # Getting the current date
    year = time.localtime()[0]
    month = time.localtime()[1]
    day = time.localtime()[2]

    # Setting variables for the calendar icon
    height = 13
    width = 13
    photo = PhotoImage(file = "cal_icon.gif") # Calendar icon

    def close_window():
        # Getting all the information out of the GUI
        e1_text = searchTerm # Task name information
        e2_text = e2.get() # Due date information
        e3_text = e3.get() # Hours in task information
        
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
        global modEvent
        modEvent = [e1_text, e2_text, priority, e3_text, checkYes]
        # Setting check variable
        master.destroy()

    def fnCalendar1():
        calendar1 = tkCalendar.tkCalendar(master, year, month, day, StringVar())
        date1 = calendar1.getstrdate()
        if date1 is not "":
            date_1 = date1

    check = IntVar()

    ########## Task entry ##########
    Label(master,text="Enter Task:").grid(row=0,sticky=W)
    v = StringVar()
    Entry(master,state=DISABLED, textvariable=v).grid(row=0,column=1,columnspan=5)
    v.set(searchTerm)

    ########## Due date entry ##########
    Label(master,text="Enter Due Date:").grid(row=1,sticky=W)
    e2_entry = StringVar()
    e2 = Entry(master,textvariable=e2_entry)
    cal1 = Button(master,height=height,width=width, image = photo,command=fnCalendar1).grid(row=1,column=5,sticky=W,padx=10)
    e2.grid(row=1,column=1,columnspan=5)
    e2.insert(0, 'mm/dd/yyyy')

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
    e3_entry = StringVar()
    e3 = Entry(master,textvariable=e3_entry)
    e3.grid(row=3,column=1,columnspan=5)

    ########## Buttons ##########
    #Check button if you want to enter another task immediately
    Checkbutton(master,text="Submit another",variable=check,onvalue=1,offvalue=0).grid(row=6,sticky=W,padx=10)
    #Submit button, which saves information from GUI and closes window
    b1 = Button(master,text="Submit",command=close_window).grid(row=6,sticky=E,column=4,padx=10)

    mainloop()
    return modEvent

def FirstGUI():
    master = Tk()
    master.title("Choose Function")    # Title of the GUI

    def close_window():
        # Getting all the information out of the GUI
        global action
        if v1.get() == 1:
            action = "create"
        elif v2.get() == 2:
            action = "modify"
        elif v3.get() == 3:
            action = "display"
        elif v4.get() == 4:
            action = "remove"
        else:
            action = None
        # Closing the window
        master.destroy()

    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()

    Label(master,text="Create New Event or Modify Existing Event?").grid(row=0,sticky=W)
    Checkbutton(master,text="Create",variable=v1,onvalue=1,offvalue=0).grid(row=1,column=0)
    Checkbutton(master,text="Modify",variable=v2,onvalue=2,offvalue=0).grid(row=1,column=1)
    Checkbutton(master,text="Display",variable=v3,onvalue=3,offvalue=0).grid(row=2,column=0)
    Checkbutton(master,text="Remove",variable=v4,onvalue=4,offvalue=0).grid(row=2,column=1)
    b1 = Button(master,text="Submit",command=close_window).grid(row=3,sticky=E,column=1,padx=10)

    mainloop()
    return action
    

def main():
    #event = [task,due date,priority,hoursInTask,start date,end date,sortingRank]
    #Lifesorter has sort,add,remove,modify,get,prepareSort,getTop

    ########## Load Using Pickle ##########
    createYes = False
    modYes = False
    rmYes = False
    try:
        prevInfo = pickle.load(open("save.p", "rb"))
    except:
        prevInfo = None
        print("No stuff in file")

    myLife = Lifesorter(prevInfo)

    if myLife.events == [[]]:
        createYes = True
        modYes = False
        rmYes = False
    else:
        action = FirstGUI()
        if action == "create":
            createYes = True
        elif action == "remove":
            rmYes = True
        elif action == "modify":
            modYes = True
        else:
            ################ LYRA

    while createYes == True:
        info = CreateGUI()
        createYes = info[4]
        myLife.addEvents(info)

    while modYes == True:
        search = SearchTaskGUI(myLife)
        info = ModGUI(search)
        modYes = info[4]
        myLife.modifyEvents(info)

    ########## Save Using Pickle ##########
    myLifeEvents = myLife.getEvents()
    if myLifeEvents[0] == []:
        myLifeEvents
    pickle.dump(myLifeEvents, open("save.p", "wb"))

if __name__ == "__main__":
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
