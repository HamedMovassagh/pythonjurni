from tkinter import *
window = Tk()  # instantr an instance of a window
# window.geometry("420x420")
window.title("I am the danger")
Photo = PhotoImage(file='angry_white.png')
icon = PhotoImage(file='angry_white.png')
window.iconphoto(True, icon)
# window.config(background='#52131f')
lable = Label(window, text="I AM THE DANGER", font=("Arial", 40, "bold"), fg='#d40f39',
              bg='black', relief=RAISED, bd=10, padx=60, pady=100, image=Photo, compound='top')

entry=Entry(window,
            font=("Arial",40),
            fg="#00FF00",
            bg="black",
            show="*"
            )
entry.insert(0,"take this bich")
entry.pack()
def sumbit():
    username=entry.get()
    print("Hello "+username)
   # entry.config(state=DISABLED)
def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1,END)


sumbit_button=Button(window,text="sumbit",command=sumbit)
delete_button=Button(window,text="delete",command=delete)
sumbit_button.pack(side="right")
delete_button.pack(side="right")

backspace_button=Button(window,text="back space",command=backspace)
backspace_button.pack(side="right")

count=0
def click():
    global count
    count+=1
    print("cilicked on skyler "+str(count)+" bitch")
photo2=PhotoImage(file="walter_wife.png")
boutton=Button(window,
                text='click me',
                command=click,
                font=("Comic Sans",40),
                fg="#6e0320",
                bg="black",
                activeforeground="#6e0320",
                activebackground="black",
                state=ACTIVE,
                image=photo2,
                compound="bottom",
                padx=239
                
                )
boutton.pack()

lable.pack()
# lable.place(x=0,y=0)

window.mainloop()  # place window on computer screen, listen for events
