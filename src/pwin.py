import graphics
from papp import papp

class PWin(object):
    def __init__(self,position):
        self.abs_position = position
        self.size = (position[2]-position[0],position[3]-position[1])
        self.canvas = graphics.Image.new(self.size)
        self.handle = papp.add_window(self)

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

    def redraw(self):
        papp.redraw_window(self)
        
    def draw_focus(self):
        pass
    
    def clear_focus(self):
        pass

    def set_focus(self):
        papp.set_focus(self.handle)

    def release_focus(self, direction=0):
        papp.release_focus(self.handle, direction)
