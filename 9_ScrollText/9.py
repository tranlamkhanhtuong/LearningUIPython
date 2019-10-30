from tkinter import *
from tkinter import scrolledtext

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Bai7b")
        self.minsize(640,400)
        self.initUI()
    
    def initUI(self):
        scrollText = scrolledtext.ScrolledText(self,width = 30 , height = 10, wrap = WORD)
        scrollText.grid(column = 0 , row = 1)

        
    #def clickMe(self):

root = Root()
root.mainloop()
