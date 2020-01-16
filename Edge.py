class Edge:
    def __init__(self, x=-1, y=-1, boundary=False):
        self.boundary = boundary

        smallerIdx = x if x < y else y
        largerIdx = y if x < y else x

        self.X = smallerIdx
        self.Y = largerIdx

    def __str__(self):
        return "(%d, %d, %s)" % (self.X, self.Y, "true" if self.boundary else "false")

    def __eq__(self, other):
        return other and self.X == other.X and self.Y == other.Y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.X, self.Y))
