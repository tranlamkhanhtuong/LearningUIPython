from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Bai10")
        self.minsize(640,400)

        self.labelFrame = ttk.LabelFrame(self,text = " My Label Frame")
        self.labelFrame.grid(row=7, column=0,padx = 20, pady = 40)
        self.initUI()
    
    def initUI(self):
        ttk.Label(self.labelFrame,text = "Label One").grid(column = 0 , row = 0 , sticky=W)
        ttk.Label(self.labelFrame,text = "Label Two").grid(column = 0 , row = 1 , sticky=W)
        ttk.Label(self.labelFrame,text = "Label Three").grid(column = 0 , row = 2 , sticky=W)


        
    #def clickMe(self):

root = Root()
root.mainloop()
