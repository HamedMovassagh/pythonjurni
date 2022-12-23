from tkinter import *

def sumbit():
    print("the tempurture is "+str(scale.get())+" C ")

window=Tk()


scale=Scale(window,
            from_=100,
            to=0,
            orient=VERTICAL,
            length=700,
            font=('Consolas',19),
            tickinterval=(10),
            showvalue= 1,
            fg="red",
            troughcolor="#69EAFF",
            bg="#111111",
            
            )


scale.set((scale['from']-scale['to'])/2+scale['to'])


Sumbit=Button(window,
             text="sumbit",
             command=sumbit,
             )


scale.pack()
Sumbit.pack()

window.mainloop()


