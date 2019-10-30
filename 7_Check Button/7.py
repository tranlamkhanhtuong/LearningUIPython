from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Bai7")
        self.minsize(640,400)
        self.initUI()
    
    def initUI(self):

       

        self.check1 = ttk.Checkbutton(self,text="Disabled",state="disabled")
        self.check1.grid(row = 0, column = 0, sticky=W)

        #self.name = StringVar()
        #self.checkBox = BooleanVar()
        #self.checkBox.set(True)
        self.checkBox = IntVar()
        #self.check2 = ttk.Checkbutton(self,text="Unchecked",offvalue="unchecked", onvalue="checked",variable = self.name)
        self.check2 = ttk.Checkbutton(self,text="Unchecked",variable = self.checkBox)

        self.check2.grid(row = 0, column = 1)
        

        self.check3 = ttk.Checkbutton(self,text="Disabled")
        self.check3.grid(row = 0, column = 2)

                
        self.button = ttk.Button(self,text="Label1",command=self.clickMe)
        self.button.grid(column = 0 ,row = 3)


    def clickMe(self):
        print("click me")
        #self.label.configure(text="clicked" + self.name.get())
        print(self.checkBox.get())
        #self.label.configure(foreground="green")
        
        
        


root = Root()
root.mainloop()
