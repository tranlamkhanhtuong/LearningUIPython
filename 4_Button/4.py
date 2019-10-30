from tkinter import *
from tkinter import ttk
class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Bai4")
        self.minsize(640,400)
        #self.wm_iconbitmap('icon.ico')
        #self.configure(background='#4D4D4D')
        
        self.label = ttk.Label(self,text="Label1")
        self.label.grid(column = 1 ,row = 0)
        
        self.button = ttk.Button(self,text="Label1",command=self.clickMe)
        self.button.grid(column = 0 ,row = 0)
        
    def clickMe(self):
        print("click me")
        self.label.configure(text="clicked")
        self.label.configure(foreground="green")
        
        
        


root = Root()
root.mainloop()
