import string, calendar
import tkinter
import time
from tkCalendar import tkCalendar

year = time.localtime()[0]
print(year)
month = time.localtime()[1]
day =time.localtime()[2]
strdate = (str(year) +  "/" + str(month) + "/" + str(day))

tk = tkinter 

fnta = ("Times", 12)
fnt = ("Times", 14)
fntc = ("Times", 18, 'bold')

lang="engl"
#lang = "span" #else lang="engl"

if lang == "span":
    #Spanish Options 
    strtitle = "Calendario"
    strdays= "Do  Lu  Ma  Mi  Ju  Vi  Sa"
    dictmonths = {'1':'Ene','2':'Feb','3':'Mar','4':'Abr','5':'May',
    '6':'Jun','7':'Jul','8':'Ago','9':'Sep','10':'Oct','11':'Nov',
    '12':'Dic'}
else :
    #English Options 
    strtitle = "Calendar"
    strdays = "Su  Mo  Tu  We  Th  Fr  Sa"
    dictmonths = {'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'May',
    '6':'Jun','7':'Jul','8':'Aug','9':'Sep','10':'Oct','11':'Nov',
    '12':'Dec'}


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
