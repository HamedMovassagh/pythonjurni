from tkinter import *
def doSomething(event):
    print("mouse coordinates "+str(event.x)+","+str(event.y))
    
window=Tk()

canvas=Canvas(window,height=500,width=500)




#window.bind("<Button-1>",doSomething) #left mouse click
#window.bind("<Button-2>",doSomething) #scroll wheel
#window.bind("<Button-3>",doSomething) #right mouse click
#window.bind("<ButtonRelease>",doSomething)#mousebutton release
#window.bind("<Enter>",doSomething) #enter the window
#window.bind("<Leave>",doSomething) #leave the window
window.bind("<B1-Motion>",doSomething) #Where the mouse moved



canvas.pack()

window.mainloop()