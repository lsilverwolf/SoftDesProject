"""
Creates the Lifesorter class with sort, add, remove, modify, get,
prepareSort, getTop and search methods.

sortEvents sorts the events based on the given priority
addEvents adds a newEvent, defined by the user
removeEvents removes an event from the events list
modifyEvents takes a modified event from the user and incorporates 
    it into the events list
getEvents returns the events list
prepareSort finds the rankings of each event, based on due date and
    priority level
getTop sorts the events list and returns the first thing to do
search finds a given string in any cell or the cell column selected

"""

#event = [task,due date,priority,hoursInTask,start date,end date,sortingRank]
#Lifesorter has sort,add,remove,modify,get,prepareSort,getTop

import datetime

class Lifesorter:
    def __init__(self,events=[]):
        self.events = []
        self.events.append(events)

    def __str__(self):
        return str(self.events)
        
    def sortEvents(self):
        #sortEvents sorts the events based on the given priority
        self.prepareSort() #finds the rankings of each task
        self.events.sort(key=lambda x: x[6]) #sorts based on the rankings
        return self.events

    def addEvents(self,newEvent):
        #addEvents adds a newEvent, defined by the user
        self.events.append(newEvent)
        return self.events

    def removeEvents(self,rmEvent):
        #removeEvents removes an event from the events list
        self.events.remove(rmEvent)
        return self.events

    def modifyEvents(self,modEvent):
        #modifyEvents takes a modified event from the user and incorporates 
        #it into the events list
        task = modEvent[0] #to match the modified task to an existing one
        for i in range(len(self.events)): #find the task to be modified
            if self.events[i][0] == task:
                self.events[i] = modEvent
        return self.events

    def getEvents(self):
        #getEvents returns the events list
        return self.events

    def getEventNames(self):
        #getEventNames returns a list of all event task names
        tasks = []
        for n in range(0,len(self.events)):
            taskName = self.events[n][0]
            tasks.append(taskName)
        tasks.sort()
        return tasks

    def prepareSort(self):
        #prepareSort finds the rankings of each event, based on due date and
        #priority level
        todayDate = datetime.date.today() #gets today's date
        for i in range(0,len(self.events)):
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

    def searchEvents(self, searchTerm, index=-1):
        #Searches through the events to find the given searchTerm
        #Returns the event list
        #if index is -1, the search function will search through every index
        #if index is specified, the search function will only look at that index of the events
        #0)task 
        #1)due date
        #2)priority 
        #3)hoursInTask
        #4)sortingRank
        if index == -1 or index > 4:
            # Serch through every index of the events
            self.sortEvents()
            for n in range(0,len(self.events)):
                for m in range(0, len(self.event[n])):
                    curr = self.events[n][m]
                    if curr == searchTerm:
                        return self.events[n]
            

        else:
            # Search through only the given index in the events
            self.sortEvents()
            for n in range(0,len(self.events)):
                curr = self.events[n][index]
                if curr == searchTerm:
                    return self.events[n]


if __name__ == "__main__":
    ########## USE ME FOR DEBUGGING ##########
    #event = [task,due date,priority,hoursInTask,start date,end date,sortingRank]
    #Lifesorter has sort,add,remove,modify,get,prepareSort,getTop
    dueDate = datetime.date(13,5,12)
    testLifesorter = Lifesorter(["test1", dueDate, 1, 4, 1])

    dueDate = datetime.date(13,5,13)
    testLifesorter.addEvents(["test2", dueDate, 2, 3, 2])

    dueDate = datetime.date(13,5,14)
    testLifesorter.addEvents(["test3", dueDate, 3, 2, 3])

    dueDate = datetime.date(13,5,15)
    testLifesorter.addEvents(["herpderp", dueDate, 4, 1, 4])
    
    print(testLifesorter.getEvents())
    print(testLifesorter.getEventNames())
 #   print(testLifesorter.searchEvents("test1"))