from tkinter import *

def creat_window():

    new_window= Tk() #Toplevel() could use on top :)
    
    #old_window.destroy()

old_window=Tk()

Button(old_window,text='create new window',command=creat_window).pack()



old_window.mainloop()










