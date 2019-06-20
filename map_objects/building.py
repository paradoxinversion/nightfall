class Building(object):
    def __init__(self, schematic, x=0, y=0):
        # X and Y coordinates for the top left corner of the building
        self.x = x
        self.y = y
        self.schematic = schematic
        self.occupants = []

    @property
    def x1(self):
        return self.x

    @property
    def y1(self):
        return self.y

    @property
    def x2(self):
        return self.x + self.width

    @property
    def y2(self):
        return self.y + self.height

    @property
    def width(self):
        """How many tiles wide is the schematic?"""
        return len(self.schematic[0])

    @property
    def height(self):
        """How many tiles tall is the schematic?"""
        return len(self.schematic)

    @property
    def self_center(self):
        return [int(self.width/2), int(self.height/2)]

    @property
    def map_center(self):
        return [self.x + int(self.width/2), self.y + int(self.height/2)]

    @property
    def center(self):
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)
        return (center_x, center_y)

    def intersect(self, other):
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)


building_schematics = {
    "basic_house":    ['####D###',
                       '#......#',
                       '#......#',
                       '#......#',
                       '#......#',
                       '#......#',
                       '#......#',
                       '#......#',
                       '########'],
    "player_house":   ['####D###....',
                       '#......#....',
                       '#......#....',
                       '#......#####',
                       '#..........#',
                       '#..........#',
                       '#......#####',
                       '#......#....',
                       '########....']
}
