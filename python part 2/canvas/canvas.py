from tkinter import *
window=Tk()

window.config(bg="black")

canvas=Canvas(window,height=500,width=500)
#canvas.create_line(0,0,500,500,fill="green",width=6)
#canvas.create_line(0,500,500,0,fill="red",width=6)
#canvas.create_rectangle(23,23,340,233,fill="black")
#canvas.create_polygon(250,0,500,500,0,500#you can give the dots position by list
#                     ,fill="green",outline="black",width=5)

#canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,extent=359)
canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
canvas.create_arc(0,0,500,500,start=180,extent=180,width=10)
canvas.create_oval(190,190,310,310,fill="white",width=10)
canvas.pack()

window.mainloop()