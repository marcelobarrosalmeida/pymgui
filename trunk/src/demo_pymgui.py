from papp import papp
from pwin import PWin
from random import randint
from plistbox import PListBox
from ptrend import PTrend

class MyPWin(PWin):
    def __init__(self,position):
        PWin.__init__(self,position)

    def update_canvas(self): 
        self.canvas.clear((randint(0,255),randint(0,255),randint(0,255)))

w1 = MyPWin((0,0,50,50))
w2 = MyPWin((50,50,100,100))

items = ["A","B","C","D","E","F","G","H"]
w3 = PTrend(position=(150,50,250,100))

w4 = PTrend(position=(5,110,145,200))

w5 = PListBox(position=(150,110,250,190),items=items)

papp.run()
