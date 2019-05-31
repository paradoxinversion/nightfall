class Tile:
    """ A tile on the map """

    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        # Block sight if a tile is blocked by default
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight
        self.explored = False
