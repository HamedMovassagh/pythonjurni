from tkinter import *
import time
WIDTH=500
HEIGHT=500
xvlocity=3
yvlocity=1
window=Tk()


canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

photo1=PhotoImage(file='skyler (1).png')
wife=canvas.create_image(0,0,image=photo1,anchor=NW)

photo=PhotoImage(file='angrywhite(1).png')
Hisen=canvas.create_image(0,0,image=photo,anchor=NW)




Hisen_w=photo.width()
Hisen_h=photo.height()


while True:
    cordinate=canvas.coords(Hisen)
    print(cordinate)
    if  (cordinate[0])>= WIDTH-Hisen_w or (cordinate[0])<0:
        xvlocity=-xvlocity 
    if (cordinate[1])>=HEIGHT-Hisen_h or(cordinate[1])<0:
        yvlocity=-yvlocity 
    canvas.move(Hisen,xvlocity,yvlocity)    
    window.update()     
    time.sleep(0.01)


window.mainloop()