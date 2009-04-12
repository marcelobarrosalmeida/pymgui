from appuifw import *
import graphics
import sysinfo
import e32

class PApp(object):

    canvas_ctrl = None
    size = sysinfo.display_pixels()
    canvas = None
    window_list = []
    active_win = None
    bind_list = {}
    background = None

    def __init__(self):
        app.screen = "full"
        self.canvas_ctrl = Canvas(redraw_callback = self.redraw,event_callback = self.event,resize_callback = self.resize)
        self.size = sysinfo.display_pixels()
        self.canvas = graphics.Image.new(self.size)
        app.body = self.canvas_ctrl
        self.lock = e32.Ao_lock()
        app.exit_handler = lambda: self.lock.signal()

    def set_background(self,background):    
        if background:
            self.background = background

    def bind(self,win,key,funct):
        if funct is None:
            try:
                del self.bind_list[key][win]
            except:
                pass # forgive me, Zen of Python
        else:
            if not self.bind_list.has_key(key):
                self.bind_list[key] = {}
            self.bind_list[key][win] = {'win':win,'cbk':funct}
            self.canvas_ctrl.bind(key,lambda: self.bind_dispatch(key))

    def bind_dispatch(self,key):
        for updt in self.bind_list[key].values():
            updt['cbk']()
            w=updt['win']
            self.canvas.blit(w.get_canvas(),target=w.get_position(),source=((0,0),w.get_size()))
        self.canvas_ctrl.blit(self.canvas)
        
    def add_window(self,win):
        self.window_list.append(win)

    def redraw_window(self,w):
        self.canvas.blit(w.get_canvas(),target=w.get_position(),source=((0,0),w.get_size()))
        self.canvas_ctrl.blit(self.canvas)
        
    def redraw(self,rect=None):
        if self.background:
            self.canvas.blit(self.background)
        for w in self.window_list:
            self.canvas.blit(w.get_canvas(),target=w.get_position(),source=((0,0),w.get_size()))
        self.canvas_ctrl.blit(self.canvas)

    def event(self,ev):
        pass

    def resize(self,rect):
        pass

    def set_focus(self):
        pass

    def run(self):
        self.redraw()
        self.lock.wait()
    
papp = PApp()