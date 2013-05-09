Life Sorter
Sharon Grimshaw, Nick Ostrom, and Lyra Silverwolf

-----------------------------------------------------------------------------

HOW TO RUN:
run python3 "tkinter_text.py" from command line

-----------------------------------------------------------------------------

Project Introduction: We spent this semester in Software Design working on an automatic to-do list sorter, which we called the Life Sorter.  The list of tasks is sorted based on user priority and due date, giving special preference to items "due" in the next couple of days.

------------------------------------------------------------------------------

Files:

tkinter_text.py: This is the main file which contains the information to build the GUIs and run the program.  The tkinter_text.py should be run from command line to access the project.  tkinter_text.py runs several GUIs, including GUIs for creating a task on the to-do list, modifying that task, removing the task, or displaying all tasks.  Previous information on the person's to-do list is saved in "save.p", which is a pickle file.

tkCalendar.py: tkCalendar.py is a file downloaded off of the internet and modified to fit our needs.  tkCalendar runs a calendar widget, which we use to pop up a calendar when the calendar button is pressed.  The tkCalendar.py program is run by the tkinter_text.py program.

lifesorter.py: This is the file which contains the information to create a Lifesorter object

------------------------------------------------------------------------------



mandatory...
how to run
say what files do
dependencies: must have tkinter and must be running python3

potentially...
sentence on UI

Acknowledgements:  We specificially thank Heather Boortz and Jeff Carruthers for their help on this project.