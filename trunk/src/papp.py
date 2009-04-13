from appuifw import *
import graphics
import sysinfo
import e32
import key_codes

__all__ = [ "PApp" ]

class PApp(object):

    canvas_ctrl = None
    size = sysinfo.display_pixels()
    canvas = None
    window_list = []
    active_win = None
    bind_list = {}
    background = None
    active_focus = 0

    def __init__(self):
        app.screen = "full"
        self.canvas_ctrl = Canvas(redraw_callback = self.redraw,
                                  event_callback = self.event,
                                  resize_callback = self.resize)
        self.size = sysinfo.display_pixels()
        self.canvas = graphics.Image.new(self.size)
        app.body = self.canvas_ctrl
        self.menu = [ (u"Exit",self.close_app) ]
        app.menu = self.menu
        self.lock = e32.Ao_lock()
        self.bind(self,key_codes.EKeyLeftArrow, self.focus_next, False)
        self.bind(self,key_codes.EKeyRightArrow, self.focus_prev, False)
        app.exit_handler = self.close_app

    def close_app(self):
        # TODO: call all widgets saying that the app is closing
        self.lock.signal()
        app.set_tabs( [], None )
        app.menu = []
        app.body = None
        app.set_exit()
        
    def set_background(self,background):    
        if background:
            self.background = background

    def bind(self,win,key,funct,is_app=True):
        if funct is None:
            try:
                del self.bind_list[key][win]
            except:
                pass # forgive me, Zen of Python
        else:
            if not self.bind_list.has_key(key):
                self.bind_list[key] = {}
            self.bind_list[key][win] = {'win':win,'cbk':funct,'app':is_app}
            self.canvas_ctrl.bind(key,lambda: self.bind_dispatch(key))

    def bind_dispatch(self,key):
        for updt in self.bind_list[key].values():
            updt['cbk']()
            if updt['app']:
                w=updt['win']
                self.canvas.blit(w.get_canvas(),target=w.get_position(),source=((0,0),w.get_size()))
        if updt['app']:                
            self.update_canvas()
       
    def add_window(self,win):
        self.window_list.append(win)
        self.active_focus = len(self.window_list) - 1

    def update_canvas(self):
        self.draw_focus()
        self.canvas_ctrl.blit(self.canvas)
        
    def redraw(self,rect=None):
        if self.background:
            self.canvas.blit(self.background)
        # generating a repaint respecting focus order
        nw = len(self.window_list)            
        for wi in [ c%nw for c in range(self.active_focus+1,self.active_focus+1+nw) ]:
            w = self.window_list[wi]
            self.canvas.blit(w.get_canvas(),target=w.get_position(),source=((0,0),w.get_size()))
        self.update_canvas()

    def draw_focus(self):
        if self.window_list:
            w = self.window_list[self.active_focus]
            p = list(w.get_position()[0:2])
            p += [p[0]+5,p[1]+5]
            self.canvas.rectangle(p,fill=(255,0,0),outline=(255,0,0))
            w.got_focus()
        
    def event(self,ev):
        pass

    def resize(self,rect):
        pass

    def focus_next(self):
        self.active_focus = (self.active_focus + 1) % len(self.window_list)
        self.redraw()
        
    def focus_prev(self):
        self.active_focus = (self.active_focus - 1) % len(self.window_list)
        self.redraw()

    def set_menu(self,menu):
        """ Merge window menu with PApp menu
        """
        m = menu + self.menu
        app.menu = m
        
    def run(self):
        self.redraw()
        self.lock.wait()
        
    
papp = PApp()
