from papp import papp
from pwidget import PWidget
from random import randint
from plistbox import PListBox
from ptrend import PTrend

class MyPWidget(PWidget):
    def __init__(self,position):
        menu = [(u"New color", self.new_color)]
        PWidget.__init__(self,position,menu)

    def new_color(self):
        self.update_canvas()
        
    def get_color(self):
        return (randint(0,255),randint(0,255),randint(0,255))
    
    def update_canvas(self): 
        self.canvas.clear(self.get_color())

w1 = MyPWidget((0,0,50,50))
w2 = MyPWidget((50,50,100,100))

items = ["A","B","C","D","E","F","G","H"]
w3 = PTrend(position=(150,50,250,130))

w4 = PTrend(position=(5,110,160,200))

w5 = PListBox(position=(130,110,250,190),items=items)

papp.run()
