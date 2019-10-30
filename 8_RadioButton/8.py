from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Bai7b")
        self.minsize(640,400)
        self.initUI()
    
    def initUI(self):
        self.radValue = IntVar()

        rad1 = ttk.Radiobutton(self,text="test1",value=1, variable=self.radValue, command = self.clickMe)
        rad1.grid(column = 0 , row = 0, sticky=W, columnspan = 3)
        
        rad2 = ttk.Radiobutton(self,text="test2",value=2, variable=self.radValue, command = self.clickMe)
        rad2.grid(column = 0 , row = 1, sticky=W, columnspan = 3)
        
        rad3 = ttk.Radiobutton(self,text="test3",value=3,variable=self.radValue, command = self.clickMe)
        rad3.grid(column = 0 , row = 2, sticky=W, columnspan = 3)
        
    def clickMe(self):
        radSelected = self.radValue.get()
        
        if radSelected == 1  :
            print("Tuong1")
        elif radSelected == 2 :
            print("Tuong2")
        elif radSelected == 3:
            print("Tuong3")
root = Root()
root.mainloop()
