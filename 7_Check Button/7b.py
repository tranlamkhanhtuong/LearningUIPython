from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Bai7b")
        self.minsize(640,400)
        self.initUI()
    
    def initUI(self):
        self.checkBox = IntVar()
        self.check2 = ttk.Checkbutton(self,text="Unchecked",variable = self.checkBox,command=self.clickMe)
        self.check2.grid(row = 0, column = 1)
        
    def clickMe(self):
        print(self.checkBox.get())
root = Root()
root.mainloop()
