from tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="SUBMIT", fg="red", command = self.accepted_message and frame.quit)
        self.button.pack(side=LEFT)
        
        self.textbox = Entry(frame).pack(side=LEFT)

    def accepted_message(self):
        print ("Entry submitted!")
        
    def recordtext(self):
        text = self.get()
        print(text)

root = Tk()

app = App(root)

root.mainloop()
