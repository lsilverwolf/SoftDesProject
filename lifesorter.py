"""
Creates the Lifesorter class with sort, add, remove, modify, get, getEventNames,
prepareSort, search methods.

sortEvents sorts the events based on the given priority
addEvents adds a newEvent, defined by the user
removeEvents removes an event from the events list
modifyEvents takes a modified event from the user and incorporates 
    it into the events list
getEvents returns the events list
getEventNames returns a list of the event names
prepareSort finds the rankings of each event, based on due date and
    priority level
getTop sorts the events list and returns the first thing to do
searchEvents finds a given string in any cell or the cell column selected

"""

#event = [task,due date,priority,hoursInTask,sortingRank]
#Lifesorter has sort,add,remove,modify,get,prepareSort,getTop

import datetime
import re

class Lifesorter:
    def __init__(self,events=[]):
        """ Initializes the Lifesorter class """
        self.events = []
        if events != [] and events != [[]]:
            eventString = str(events)
            if eventString[0:2] == "[[":
                self.events = events
            else:
                self.events.append(events)            

    def __str__(self):
        """ Returns a string of the events list """
        return str(self.events)
        
    def sortEvents(self):
        """ Sorts the events based on the given priority and due date """
        self.prepareSort() # Finds the rankings of each task
        self.events.sort(key=lambda x: x[4]) # Sorts based on the rankings
        return self.events

    def addEvents(self,newEvent):
        """ Adds a newEvent, defined by the user """
        self.events.append(newEvent)
        return self.events

    def removeEvents(self,rmEvent):
        """ Removes an event from the events list """
        self.events.remove(rmEvent)
        return self.events

    def modifyEvents(self,modEvent):
        """ Takes a modified event from the user and incorporates it into
        the events list by finding the event title and changing information """
        task = modEvent[0] # Matches the modified task to an existing one
        for i in range(len(self.events)): # Finds the task to be modified
            if self.events[i][0] == task:
                self.events[i] = modEvent
        return self.events

    def getEvents(self):
        """ Returns the events list """
        return self.events

    def getEventNames(self):
        """ Returns a list of all event task names """
        tasks = []
        for n in range(0,len(self.events)):
            taskName = self.events[n][0]
            tasks.append(taskName)
        tasks.sort()
        return tasks

    def prepareSort(self):
        """ Finds the rankings of each event, based on given due date and
        priority level, and assigns each task a 'sorting rank' """
        todayDate = datetime.date.today() # Gets today's date
        for i in self.events:
            event = i
            eventIndex = self.events.index(i)
            event[4] = 0 # Initializes the sorting rank
            dueDate = event[1]
            priority = event[2]
            daysLeft = dueDate - todayDate #how many days until it's due
            daysLeft = daysLeft.days
            sortingRank = daysLeft + int(priority)
            if daysLeft == 0: # Gives higher rank to tasks that are due today
                sortingRank -= 4
            if daysLeft == 1:
                sortingRank -= 2
            event[4] += sortingRank # Adds the rank to the current event
            self.events[eventIndex] = event
        return self.events

    def searchEvents(self, searchTerm, index=-1):
        """ Searches through the events to find the given searchTerm and
        returns the event list of any matching entries
        
        if index is -1, the search function will search through every index
        if index is specified, the search function will only look at that index of the events
        
        0)task 
        1)due date
        2)priority 
        3)hoursInTask
        4)sortingRank """

        matches = []
        matchIndecies = []
        if index == -1 or index > 4:
            # Search through every index of the events for the searchTerm
            self.sortEvents()
            for n in range(0,len(self.events)):
                for m in range(0, len(self.events[n])):
                    curr = str(self.events[n][m])
                    if re.search(searchTerm, curr, re.IGNORECASE):
                        if n in matchIndecies:
                            break
                        else:
                            matchIndecies.append(n)
                            matches.append(self.events[n])
            
        else:
            # Search through only the given index in the events
            self.sortEvents()
            for n in range(0,len(self.events)):
                curr = str(self.events[n][index])
                if re.search(searchTerm, curr, re.IGNORECASE):
                    matches.append(self.events[n])
        return matches


if __name__ == "__main__":
    """ DEBUGGER """
    #event = [task,due date,priority,hoursInTask,start date,end date,sortingRank]
    #Lifesorter has sort,add,remove,modify,get,prepareSort,getTop
    dueDate = datetime.date(2013,5,12)
    testLifesorter = Lifesorter() #["ztest1", dueDate, 1, 4, 0]

    dueDate = datetime.date(2013,5,13)
    testLifesorter.addEvents(["ytask2", dueDate, 2, 3, 0])

    dueDate = datetime.date(2013,5,8)
    testLifesorter.addEvents(["xtest3", dueDate, 3, 2, 0])

    dueDate = datetime.date(2013,5,10)
    testLifesorter.addEvents(["wtask4", dueDate, 4, 1, 0])
    
    print(testLifesorter.searchEvents("2"))
    print(testLifesorter.getEventNames())
