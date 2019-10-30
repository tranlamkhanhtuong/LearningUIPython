from tkinter import *

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Bai3")
        self.minsize(640,400)
        #self.wm_iconbitmap('icon.ico')
        #self.configure(background='#4D4D4D')
        
    def createWidget(self):
        # khoi tao va noi dung
        label = Label(self,text="Label1")
        label2 = Label(self,text="Label2")
        label3 = Label(self,text="Label3")
        '''label.pack()
        label2.pack()
        label3.pack()'''
        label.place(x=20,y=30)
        label2.place(x=40,y=10)
        label3.place(x=10,y=20)
        
        
root = Root()
root.createWidget()
root.mainloop()

        

