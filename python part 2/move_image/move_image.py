from tkinter import *
#def move_up(event):
#    lbl_hiesnberg.place(x=lbl_hiesnberg.winfo_x() ,y=lbl_hiesnberg.winfo_y()-10)
#def move_down(event):
#    lbl_hiesnberg.place(x=lbl_hiesnberg.winfo_x() ,y=lbl_hiesnberg.winfo_y()+10)
#def move_right(event):
#    lbl_hiesnberg.place(x=lbl_hiesnberg.winfo_x()+10 ,y=lbl_hiesnberg.winfo_y())
#def move_left(event):
#    lbl_hiesnberg.place(x=lbl_hiesnberg.winfo_x()-10 ,y=lbl_hiesnberg.winfo_y())
def move_up(event):
    canvas.move(myimage,0,-10)
def move_down(event):
    canvas.move(myimage,0,+10)
def move_right(event):
    canvas.move(myimage,+10,0)
def move_left(event):
    canvas.move(myimage,-10,0)
window=Tk()
window.geometry("500x500")



img_hiesnberg=PhotoImage(file='angrywhite(1).png')
#lbl_hiesnberg=Label(window,image=img_hiesnberg)
canvas=Canvas(window,width=500,height=500)
canvas.pack()   

myimage=canvas.create_image(0,0,image=img_hiesnberg,anchor=NW)





window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<d>",move_right)
window.bind("<a>",move_left)

#lbl_hiesnberg.place(x=0,y=0)

window.mainloop()