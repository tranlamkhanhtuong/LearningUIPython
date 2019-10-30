from tkinter import *

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Bai2")
        self.minsize(640,400)
        #self.wm_iconbitmap('icon.ico')
        #self.configure(background='#4D4D4D')
        
    def createWidget(self):
        # khoi tao va noi dung
        label = Label(self,text="Label1")
        label.grid(column = 0 ,row = 0)
        
        label2 = Label(self,text="Label2")
        label2.grid(column = 1 ,row = 1)
        
        
root = Root()
root.createWidget()
root.mainloop()

        
