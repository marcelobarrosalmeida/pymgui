import graphics
from papp import papp
    
class PWin(object):
    def __init__(self,position):
        self.abs_position = position
        self.size = (position[2]-position[0],position[3]-position[1])
        self.canvas = graphics.Image.new(self.size)
        papp.add_window(self)

    def bind(self,key,funct):
        papp.bind(self,key,funct)

    def update_canvas(self):
        pass
    
    def get_position(self):
        return self.abs_position

    def get_size(self):
        return self.size
    
    def get_canvas(self):
        self.update_canvas()
        return self.canvas
  
    
