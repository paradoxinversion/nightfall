class Building(object):
    def __init__(self, schematic, x=0, y=0):
        # X and Y coordinates for the top left corner of the building
        self.x = x
        self.y = y
        self.schematic = schematic
        self.occupants = []

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
