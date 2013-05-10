Life Sorter
Sharon Grimshaw, Nick Ostrom, and Lyra Silverwolf

-----------------------------------------------------------------------------

HOW TO INSTALL AND RUN:

For installation instructions,, please see Installation.txt.
To run, type ./LifeSorter into the command line.
For a userguide, please see UserGuide.txt.

-----------------------------------------------------------------------------

Project Introduction: 

We spent this semester in Software Design working on a smart to-do list, which we called the LifeSorter.  The list of tasks is sorted based on user priority and due date, giving special preference to items "due" in the next couple of days.

------------------------------------------------------------------------------

Files:

LifeSorter: This is a command line program which contains the information to build the GUIs and run the program.  LifeSorter should be run from command line to access the project.  LifeSorter runs several GUIs, including GUIs for creating a task on the to-do list, modifying that task, removing the task, or displaying all tasks.  Previous information on the person's to-do list is saved in "save.p", which is a pickle file.

tkCalendar.py: tkCalendar.py is a file downloaded off of the internet and modified to fit our needs.  tkCalendar runs a calendar widget, which we use to pop up a calendar when the calendar button is pressed.  The tkCalendar.py program is run by the LifeSorter program.

sorter.py: This is the file which contains the Lifesorter class. The Lifesorter class has methods for inputing events, sorting events, and returning events to the user.

For further information, visit DesignGuide.txt.

All of the files for this project are located in the main branch of the 
github repository at https://github.com/lsilverwolf/SoftDesProject.git.

------------------------------------------------------------------------------

Acknowledgements and Reflection:  

We specificially thank Heather Boortz and Jeff Carruthers for their help on this project.

We really enjoyed working on this project. There are a few extra steps we would have taken if we had the time, but overall we are very happy with what we have created. To see our full reflection, please see SelfEvaluation.txt.