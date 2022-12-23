class ball:
    def __init__(self,canvas,x,y,diemeter,xvlocity,yvlocity,color): 
        self.canvas=canvas
        self.imag=canvas.create_oval(x,y,diemeter,diemeter,fill=color)
        self.xvlocity=xvlocity
        self.yvlocity=yvlocity
    def move(self):
            cordinate=self.canvas.coords(self.imag)
            print(cordinate)  
            if (cordinate[2])>=(self.canvas.winfo_width())or (cordinate[0]<0):
                self.xvlocity=-self.xvlocity

            if (cordinate[3])>=(self.canvas.winfo_width())or (cordinate[1]<0):
                self.yvlocity=-self.yvlocity

            self.canvas.move(self.imag,self.xvlocity,self.yvlocity)  