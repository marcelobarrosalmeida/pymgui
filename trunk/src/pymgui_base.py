import re

class PRect(object):
    """ Provides controls over a rectangule
    """
    def __init__(self, scoord=(0,0,0,0)):
        """ Creates a new rectangule given some coordinates in the format (0,0,0,0)
            Fefault coords are (0, 0, 0, 0), using integer numbers and
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

    def __getitem__(self,idx):
        return self.coord[idx]

    def __str__(self):
        return str(self.get_coords())

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

    def __eq__(self, other):
        return self.get_color() == other.get_color()
    
    def __ne__(self, other):
        return self.get_color() != other.get_color()

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
c = CColor("#040a7681") #some color
cc = CColor("040A7681") #equals to c
ccc = CColor("#040a76") #different, alpha ommited is equal to FF
print "Colors:"
print "     c: " + c.get_color()
print "    cc: " + cc.get_color()
print "   ccc: " + ccc.get_color()
if c == cc:
    print "'c' and 'cc' are equals"
if c != ccc:
    print "'cc' and 'ccc' are different"

coord = CRect("1,002,-03,40")
print
print "Rect:"
print "coords: " + coord.get_coords()
