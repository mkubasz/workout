
class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'{Point.__name__}(x={self.x}, y={self.y}, z={self.z})'

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __add__(self, other) -> 'Point':
        return Point(self.x + other.x,
                     self.y + other.y,
                     self.z + other.z)

    def __sub__(self, other) -> 'Point':
        return Point(self.x - other.x,
                     self.y - other.y,
                     self.z - other.z)

    def __mul__(self, other) -> 'Point':
        return Point(self.x * other,
                     self.y * other,
                     self.z * other)

    def __rmul__(self, other) -> 'Point':
        return Point(self.x * other,
                     self.y * other,
                     self.z * other)

    # def __iter__(self) -> tuple:
    #      yield from (self.x, self.y, self.z)

    def __getitem__(self, index) -> tuple:
        return (self.x, self.y, self.z)[index]
