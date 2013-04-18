"""
A program to solve your problems
"""

import datetime
data = []
newItem = []
task = ""
dateInfo = []
checkTask = "y"
hoursInTask = 0

# def assignTime(task,dueDate,hoursInTask):
#     if mandatory = True:
#         schedule task during mandatory blockOfTime
#         remove from list of things to schedule
#     elif blockOfTime > hoursInTask:
#         schedule task then
#         remove from list of things to schedule
#     elif blockOfTime >= 1 and hoursInTask>=2:
#         schedule part of task then
#         timeLeft = hoursInTask - blockOfTime
#         update hoursInTask with timeLeft and continue scheduling
#     elif blockOfTime >= 0.5 amd hoursInTask >= 1:
#         schedule part of task then
#         timeLeft = hoursInTask - blockOfTime
#         update hoursInTask with timeLeft and continue scheduling

while checkTask == "y":
    todayDate = datetime.date.today()
    task = input("What is the name of the task?: ")
    dateInput = input("What is the due date? Input date in the format 1/3/2013 for Jan 3, 2013: ")
    dateInfo = dateInput.split('/')
    dueDate = datetime.date(int(dateInfo[2]), int(dateInfo[0]), int(dateInfo[1]))
    priority = input("What is the priority (scale 1-highest through 5-lowest)?: ")
    hoursInTask = input("How long do you expect this task to take (in hours)?: ")
    daysLeft = dueDate - todayDate
    daysLeft = daysLeft.days
    sortingRank = daysLeft + int(priority)
    if daysLeft == 1:
        sortingRank -= 4
    if daysLeft == 2:
        sortingRank -= 2
    newItem = [task,dueDate,priority,hoursInTask,sortingRank]
    data.append(newItem)
    checkTask = input("If you have another item to input, type y: ")
data.sort(key=lambda x: x[4])
for element in data:
    print(element[0] + ': ' + element[1].isoformat())
#print(data)

"""
If you get to the due date, it will prompt you with the question "Are you 
done?".  If you say yes, it will remove it from the list.  If you say no, 
it will ask you how much more time you expect it to take and budget that 
amount of time accprdingly, updating the rest of your tasks to allocate 
that amount of unplanned time
find the largest chunk of free time
"""