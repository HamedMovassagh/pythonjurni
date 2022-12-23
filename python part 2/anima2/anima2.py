from tkinter import *
import time
from ball import *
window=Tk()


canvas=Canvas(window,width=500,height=500)
canvas.pack()

#circle=canvas.create_oval(1,1,100,100)

white=ball(canvas,0,0,100,1,1,"white")
orange=ball(canvas,20,30,200,5,3,"orange")


WIDTH=500
HEIGHT=500

while True:
    white.move()
    orange.move()
    window.update()
    time.sleep(0.01)




window.mainloop()