import string, calendar
import tkinter
import time
from tkCalendar import tkCalendar

year = time.localtime()[0]
month = time.localtime()[1]
day =time.localtime()[2]
strdate = (str(year) +  "/" + str(month) + "/" + str(day))

tk = tkinter 

class clsMainFrame(tk.Frame):
    def __init__(self, master):
        self.parent = master
        tk.Frame.__init__(master)
        self.date_var = tk.StringVar()
        self.date_var.set(strdate)        
        label = tk.Label(master, textvariable= self.date_var, bg = "white")
        label.pack(side="top")
        testBtn = tk.Button(master, text = 'getdate',command = self.fnCalendar)
        testBtn.pack(side = 'left')
        exitBtn = tk.Button(master, text = 'Exit',
             command = master.destroy)
        exitBtn.pack(side = 'right')

    def fnCalendar(self):
        tkCalendar(self.parent, year, month, day, self.date_var)
    
if __name__ == '__main__':
    root =tk.Tk()
    root.title ("Calendar")
    Frm = tk.Frame(root)
    clsMainFrame(Frm)
    Frm.pack()
    root.mainloop()
