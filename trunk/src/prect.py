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