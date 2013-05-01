"""
Creates the Lifesorter class with sort, add, remove, modify, get,
prepareSort, and getTop methods.

sortEvents sorts the events based on the given priority
addEvents adds a newEvent, defined by the user
removeEvents removes an event from the events list
modifyEvents takes a modified event from the user and incorporates 
    it into the events list
getEvents returns the events list
prepareSort finds the rankings of each event, based on due date and
    priority level
getTop sorts the events list and returns the first thing to do

"""

#event = [task,due date,priority,hoursInTask,start date,end date,sortingRank]
#Lifesorter has sort,add,remove,modify,get,prepareSort,getTop

import datetime

class Lifesorter:
    def __init__(self,events=[]):
        self.events = events

    def __str__(self):
        return str(self.events)
        
    def sortEvents(self):
        #sortEvents sorts the events based on the given priority
        prepareSort(self) #finds the rankings of each task
        self.events.sort(key=lambda x: x[6]) #sorts based on the rankings
        return self.events

    def addEvents(self,newEvent):
        #addEvents adds a newEvent, defined by the user
        self.events += newEvent
        return self.events

    def removeEvents(self,rmEvent):
        #removeEvents removes an event from the events list
        self.events.remove(rmEvent)
        return self.events

    def modifyEvents(self,modEvent):
        #modifyEvents takes a modified event from the user and incorporates 
        #it into the events list
        task = modEvent[0] #to match the modified task to an existing one
        for i in events: #find the task to be modified
            if self.events[i][0] == task:
                self.events[i] = modEvent
        return self.events

    def getEvents(self):
        #getEvents returns the events list
        return self.events

    def prepareSort(self):
        #prepareSort finds the rankings of each event, based on due date and
        #priority level
        todayDate = datetime.date.today() #gets today's date
        for i in self.events:
            event = self.events[i]
            priority = event[2] #user given priority
            daysLeft = dueDate - todayDate #how many days until it's due
            daysLeft = daysLeft.days
            sortingRank = daysLeft + int(priority) #ranks the task based on priority 
                #and how many days are left before it's due
            if daysLeft == 1: #gives higher rank to tasks that are due now, regardless of priority
                sortingRank -= 4
            if daysLeft == 2:
                sortingRank -= 2
            event += sortingRank #adds the rank to the current event
            self.events[i] = event
        return self.events

    def getTop(self):
        #getTop sorts the events list and returns the first thing to do
        sortEvents(self)
        return self.events[0]