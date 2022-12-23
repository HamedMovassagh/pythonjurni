from tkinter import *


window=Tk()
window.title("chek_box")
x=IntVar()

def check():
    if x.get():
        print("you agrree")
    else:
        print("you dont agree :(")    

undercheck=PhotoImage(file="angry_white.png")
checkbutton=Checkbutton(window,text="i agree with somthing",font=("Arial",20,"bold") ,
fg="#3cc213",variable=x,onvalue=1,offvalue=0,command=check,bg="black",activebackground="black",activeforeground="#3cc213",
padx=32,pady=10,image=undercheck,compound="bottom")
                        
checkbutton.pack()


window.mainloop()

