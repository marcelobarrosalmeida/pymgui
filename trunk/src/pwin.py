import graphics
from papp import papp
    
class PWin(object):
    def __init__(self,position):
        self.position = position
        self.size = (position[2]-position[0],position[3]-position[1])
        self.canvas = graphics.Image.new(self.size)
        papp.add_window(self)

    def bind(self,key,funct):
        papp.bind(self,key,funct)
        
    def update_canvas(self):
        # update canvas and return it, override this function
        return self.canvas
  
    
