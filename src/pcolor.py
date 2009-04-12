import re

class PColor(object):
    """ Color representation with some operations
    """
    def __init__(self, scolor=[0,0,0,255]):
        self.set_color(scolor)

    def set_color(self, scolor):
        """ Use: #RRGGBBAA or [R, G, B, A]
            default color: black (#000000ff) (0, 0, 0, 255)
        """
        if isinstance(scolor, str):
            #RRGGBBAA
            regex = re.compile(u"#{0,1}([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2}){0,1}", re.IGNORECASE)
            m = regex.match(scolor)
            if m:
                if m.group(4):
                    alpha = int("0x" + m.group(4), 16)
                else:
                    alpha = 255

                self.color = [int("0x" + m.group(1), 16), 
                              int("0x" + m.group(2), 16),
                              int("0x" + m.group(3), 16),
                              alpha]
            else:
                self.color = [0,0,0,255]
        elif isinstance(scolor, list):
            # [R, G, B, A]
            self.color = [ max(0,int(c)) for c in scolor ]
        else:
            self.color = [0,0,0,255]

    def combine(self, other, perc):
        self.color = map(lambda a,b: int(a*(1-perc)+0.5) + int(b*perc+0.5), self.color, other.color)

    def __str__(self):
        return "#" + "".join([ "%02X" % c for c in self.color ])

    def __eq__(self, other):
        return self.color == other.color

    def __ne__(self, other):
        return self.color != other.color

""" Test area
"""
white = PColor("#ffffffff")
c     = PColor("#550000ff")
c.combine(white, 0.8)
print c
print c.color