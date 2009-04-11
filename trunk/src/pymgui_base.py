import re

class PRect(object):
    """ Provides controls over a rectangule
    """
    def __init__(self, scoord=(0,0,0,0)):
        """ Creates a new rectangule given some coordinates in the format (0,0,0,0)
            Default coords are (0, 0, 0, 0), using integer numbers and
            negative coords are valid
        """
        self.set_coords(scoord)

    def set_coords(self, scoord):
        """ Set a coordinate
        """
        self.coord = tuple(scoord)

    def get_coords(self):
        """ Retrieve the current coords
        """
        return self.coord

    def __getitem__(self, idx):
        return self.coord[idx]

    def __str__(self):
        return str(self.get_coords())

    def __eq__(self, other):
        return self.get_coords() == other.get_coords()

    def __ne__(self, other):
        return self.get_coords() != other.get_coords()


class PColor(object):
    """ Color representation with some operations
    """
    def __init__(self, scolor):
        self.set_color(scolor)

    def set_color(self, scolor):
        """ Use: #RRGGBBAA
            default color: black (#000000ff)
        """
        r = re.compile(u"#{0,1}([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2}){0,1}", re.IGNORECASE)
        m = r.match(scolor)
        if m:
            i = 3
            self.red = int("0x" + m.group(1), 16)
            self.green = int("0x" + m.group(2), 16)
            self.blue = int("0x" + m.group(3), 16)
            if m.group(4):
                self.alpha = int("0x" + m.group(4), 16)
            else:
                self.alpha = 255
        else:
            self.set_string('#000000ff')

    def get_color(self):
        ret = "#"
        
        if self.red < 16:
            ret += "0"
        ret += "%X" % self.red
        
        if self.green < 16:
            ret += "0"
        ret += "%X" % self.green
        
        if self.blue < 16:
            ret += "0"
        ret += "%X" % self.blue
        
        if self.alpha < 16:
            ret += "0"
        ret += "%X" % self.alpha
        
        return ret

    def __eq__(self, other):
        return self.get_color() == other.get_color()
    
    def __ne__(self, other):
        return self.get_color() != other.get_color()

    def __str__(self):
        return self.get_color()

    def combine(self, other, percent):
        self.red   |= int(other.red   * percent)
        self.green |= int(other.green * percent)
        self.blue  |= int(other.blue  * percent)
        self.alpha |= int(other.alpha * percent)

""" PComponent: Base class for all components
""" 
class PComponent(object):
    def __init__(self, container, rect):
        self.rect = rect
        self.container = container

""" Test area
"""
white = PColor("#ffffffff")
c     = PColor("#550000ff")
c.combine(white, 0.15)
print c                     #772626FF

