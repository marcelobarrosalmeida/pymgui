import re

#######################
# CRect: Rectangle data
#######################
class CRect(object):
    def __init__(self, scoord):
        self.set_coords(scoord)

    def set_coords(self, scoord):
        #######
        # scoord format (top, left, bottom, right)
        # default coords (0, 0, 0, 0) - integer numbers
        # negative coords are valid
        r = re.compile(u"\({0,1}(-{0,1}\d+)\s*,\s*(-{0,1}\d+)\s*,\s*(-{0,1}\d+)\s*,\s*(-{0,1}\d+)\){0,1}")
        m = r.match(scoord)
        if m:
            self.rect = (int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)))
        else:
            self.rect = (0, 0, 0, 0)

    def get_coords(self):
        return '(' + str(self.rect[0]) + ', ' + str(self.rect[1]) + ', ' + str(self.rect[2]) + ', ' + str(self.rect[3]) + ')'

    def __str__(self):
        return self.get_coords()

    def __cmp__(self, other):
        return self.get_coords() == other.get_coords()

#######################
# CColor: Color object
#######################
class CColor(object):
    def __init__(self, scolor):
        self.set_color(scolor)

    def set_color(self, scolor):
        #########
        # Use: #RRGGBBAA
        # default color: black (#000000ff)
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

    def __cmp__(self, other):
        return self.get_color() == other.get_color()

    def __str__(self):
        return self.get_color()

#######################
# CComponent: Base class for all components
#######################
class CComponent(object):
    def __init__(self, container, rect):
        self.rect = rect
        self.container = container

#######################
#Test area
#######################
c = CColor("#040a7681")
print "Color: " + c.get_color()

coord = CRect("1,002,-03,40")
print "Rect: " + coord.get_coords()
