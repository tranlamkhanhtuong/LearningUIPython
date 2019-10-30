from tkinter import *

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Bai 1 b")
        self.minsize(640,400)
        #self.wm_iconbitmap('icon.ico')
        self.configure(background='#4D4D4D')
        
root = Root()
root.mainloop()
        