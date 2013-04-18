"""
Learning how to use GUIs
"""

from tkinter import*

def close_window():
    # Destroying your main window (root)
    root.destroy()

root = Tk()
root.title('New Task')
frame = Frame(root)
frame.pack()

Label(root,text='Enter the task:').grid(row=0)
e1 = Entry(root)
Label(root,text='Enter the due date:').grid(row=1)
e2 = Entry(root)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
# Label(text='Enter the due date:').pack(side=LEFT,padx=10,pady=10)
# Entry(root, width=10).pack(side=LEFT,padx=10,pady=10)

button = Button(root)
button['text'] ="Submit"
button['command'] = close_window
button.pack(side = BOTTOM,pady=10)

mainloop()





# from tkinter import *
# root =Tk()
# frame = Frame(root)

# def close_window():
#     frame.quit()

# root.title('New Task')
# Label(text='Enter the task:').pack(side=LEFT,padx=10,pady=10)
# Entry(root, width=10).pack(side=LEFT,padx=10,pady=10)
# Button(root, text='Submit').pack(side=LEFT,command=close_window)
# root.mainloop()