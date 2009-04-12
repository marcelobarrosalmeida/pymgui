from papp import papp
from pwin import PWin
from random import randint

class MyPWin(PWin):
    def __init__(self,position):
        PWin.__init__(self,position)

    def update_canvas(self): 
        self.canvas.clear((randint(0,255),randint(0,255),randint(0,255)))
        return self.canvas

w1 = MyPWin((0,0,50,50))
w2 = MyPWin((50,50,100,100))
w3 = MyPWin((100,100,150,150))
w4 = MyPWin((150,150,200,200))

papp.run()
