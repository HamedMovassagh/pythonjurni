from tkinter import *

z=IntVar

def butt(x,y,r,t,f):
   
   
   
   Button(window,text=x,width=y,height=r,command=lambda : fota(x) ).grid(row=t,column=f)
dick=""
def fota(x):
   #global dick
   #
   #dick=dick+str(x)
   #lbl_safhe.config(text=dick)
   a.append(x)
   
   print(a)

    

    


def fr():
   pass


window=Tk()

a=[]
print(a)

lbl_safhe=Label(window,text="somthing",font=("Arial",20),width=10,height=4)

lbl_safhe.grid(row=0,column=0,columnspan=3)


one=      butt(1,10,4,3,0) #Button(window,text=1,width=10,height=4,command=lambda :fota(1) ).grid(row=3,column=0)                         
two =     butt(2,10,4,3,1) #Button(window,text=2,width=10,height=4,command=lambda :fota(2) ).grid(row=3,column=1)                         
three=    butt(3,10,4,3,2) #Button(window,text=3,width=10,height=4,command=lambda :fota(3) ).grid(row=3,column=2)                         
four=     butt(4,10,4,2,0) #Button(window,text=4,width=10,height=4,command=lambda :fota(4) ).grid(row=2,column=0)                         
five=     butt(5,10,4,2,1) #Button(window,text=5,width=10,height=4,command=lambda :fota(5) ).grid(row=2,column=1)                         
six=      butt(6,10,4,2,2) #Button(window,text=6,width=10,height=4,command=lambda :fota(6) ).grid(row=2,column=2)                         
seven=    butt(7,10,4,1,0) #Button(window,text=7,width=10,height=4,command=lambda :fota(7) ).grid(row=1,column=0)                         
eight=    butt(8,10,4,1,1) #Button(window,text=8,width=10,height=4,command=lambda :fota(8) ).grid(row=1,column=1)                         
nine=     butt(9,10,4,1,2) #Button(window,text=9,width=10,height=4,command=lambda :fota(9) ).grid(row=1,column=2)                         


window.mainloop()







