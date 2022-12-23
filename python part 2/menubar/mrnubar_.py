from tkinter import *

def openFile():
    print("file has been open")
def saveFile():
    print("file has been save")
def Cut():
    print("You cut some Text")
def Copy():
    print("You Copy some Text")
def Paste():
    print("You Paste some Text")




window= Tk()

menubar= Menu(window)
window.config(menu=menubar)

fileMenue=Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="file",menu=fileMenue)
fileMenue.add_command(label="open",command=openFile)
fileMenue.add_command(label="save",command=saveFile)
fileMenue.add_separator()
fileMenue.add_command(label="Exit",command=quit)


editMenu= Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=Cut)
editMenu.add_command(label="Copy",command=Copy)
editMenu.add_command(label="Paste",command=Paste)



window.mainloop()


