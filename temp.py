# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""from tkinter import *

root=Tk()
root.title("Add")
root.geometry("400x200")
show_label=Label(root)


def add():
    addition= 4
    addition_2=1
    result=addition+addition_2
    show_label["text"]=result
   print(addition+addition_2)

    
button=Button(root,text="Add",command=add)
button.pack()
    
    
show_label.pack()
root.mainloop()"""
from tkinter import *

root=Tk()
root.title("Driving License")
root.geometry("400x200")
show_label=Label(root)

def driving_license():
    Name="Sricharan"
    Date_of_birth="13|6|2009"
    Pin_number="451478"
    Address="Disney Land, Hong Kong"
    Authorization_to_drive_the_following_vehicles="Two four"
    result=Name+Date_of_birth+ Pin_number+ Address+  Authorization_to_drive_the_following_vehicles
    show_label["text"]=result
    
    
button=Button(root,text="Show Driving license",command=driving_license)
button.pack()
    
    
show_label.pack()
root.mainloop()
    
    