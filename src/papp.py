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
        #self.window_list = []
        #self.active_win = None
        #self.bind_list = {}
        #self.background = None
        app.body = self.canvas_ctrl
        self.lock = e32.Ao_lock()
        app.exit_handler = lambda: self.lock.signal()

    def set_background(self,background):    
        if background:
            self.background = background

    def bind(self,win,key,funct):
        if funct is None:
            if self.bind_list.has_key(win):
                if self.bind_list[win].has_key(key):
                    del self.bind_list[win][key]
        else:
            if not self.bind_list.has_key(win):
                self.bind_list[win] = {}
            self.bind_list[win][key] = funct
            self.canvas_ctrl(key,lambda: self.bind_manager(win,key))

    def bind_manager(self,win,key):
        self.bind_list[win][key]()
        
    def add_window(self,win):
        self.window_list.append(win)

    def redraw(self,rect=None):
        if self.background:
            self.canvas.blit(self.background)
        for w in self.window_list:
            self.canvas.blit(w.update_canvas(),target=w.position,source=((0,0),w.size))
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