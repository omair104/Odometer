# -*- coding: utf-8 -*-
"""
Created on June 02 10:00:25 2019

@author: Babri
"""

import os
import sys
import tkinter
from tkinter import Toplevel
import image_creation

#For third party libraies
try:
    our_location = os.path.realpath(os.path.abspath(os.path.dirname(__file__)))
    print(our_location)
except:
    our_location = os.path.abspath(os.path.normpath(os.path.dirname(sys.argv[0])))

__base_dir = our_location
__libs_dir = os.path.join(__base_dir, 'thirdparty')

sys.path.insert(0, __base_dir)
sys.path.insert(0, __libs_dir)

def makedirs(dest):
    if not os.path.exists(dest):
        os.makedirs(dest)


class Application(tkinter.Frame):
       
    def __init__(self, directory, master=None):
        self.directory=directory        
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.QUIT = tkinter.Button(self, width=15, fg = "red", font =('bold',18))
        self.QUIT["text"] = "EXIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.grid(row=30, sticky = 'W', pady=10)

        #------------------------------------------- WIDGETS ON MAIN GUI -------------------------------------------

        self.convertlabel=tkinter.Label(self, text='ODOMETER',font=('bold',16)).grid(row=16, pady=2, sticky='W')

        #Enter Length
        self.length_label = tkinter.Label(self, text='Enter Length:').grid(row=17, sticky='W')
        self.length_entrybox = tkinter.Entry(self, width=40)
        self.length_entrybox.grid(row=18, sticky='W')

        #Enter Units
        #self.unit_label=tkinter.Label(self, text='Enter Units:').grid(row=19, sticky='W')
        self.units_variable = tkinter.StringVar(root)
        self.units_variable.set('meters')
        self.unit_entrybox=tkinter.OptionMenu(self, self.units_variable, "meters", "feet")
        self.unit_entrybox.grid(row=18, sticky='E')
        
        #Enter Time
        self.time_label=tkinter.Label(self, text='Enter time (in seconds):').grid(row=21, sticky='W')
        self.time_entrybox=tkinter.Entry(self, width=40)
        self.time_entrybox.grid(row=22, sticky='W')

        #button for converting
        self.convertbutton = tkinter.Button(self, width=15, text='CREATE VIDEO',font=('bold',18), command=self.createVideo)
        self.convertbutton.grid(row=28, pady=10, sticky='W')
        
    def createVideo(self):
        self.fields_check()
        entered_length = int(self.length_entrybox.get())
        entered_unit = str(self.units_variable.get())
        entered_time=int(self.time_entrybox.get())
        image_creation.main(entered_length, entered_unit, entered_time)
        


    def display_error(self, text_message):
        top = Toplevel()
        x = self.master.winfo_rootx()
        y = self.master.winfo_rooty()
        top.geometry("+%d+%d" %(x+250,y+150))
        #top.geometry("+550+350")
        top.title('Error')
        tkinter.Label(top, text=text_message).grid(row=1, sticky='W')
        tkinter.Button(top, text="OK", command=top.destroy).grid(row=2)


    def fields_check(self):

        self.field1=self.length_entrybox.get()
        self.field2=self.units_variable.get()
        self.field3=self.time_entrybox.get()

        if  not self.field1:
            text_message = "Please select length"
            self.display_error(text_message)
            return
        else:
            pass

        if not self.field2:
            text_message = "Please select units"
            self.display_error(text_message)
            return
        else:
            pass

        if not self.field3:
            text_message = "Please select time"
            self.display_error(text_message)
            return   
        else:
            pass
        
    
        #makedirs(self.rotatedlocation)


root = tkinter.Tk()
root.geometry("800x400+300+200")
root.title("Odometer")

app = Application('', master=root)

#app.configure(background='grey')
app.mainloop()
#com= comparing(app)
root.destroy()
