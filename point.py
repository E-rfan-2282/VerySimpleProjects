from functools import total_ordering


@total_ordering
class Point:
    default_coordinates = 0, 50, 0

    def __set_coordinates(self, *coordinates):
        if not all(isinstance(c, (int, float)) for c in coordinates):
            raise TypeError("All coordinates must be numbers.")

        self.dimension = len(coordinates)

        if self.dimension == 0:
            self.x, self.z, self.y = 0, 0, 0

        elif self.dimension == 2:
            self.x, self.y = coordinates
            self.dimension += 1

        elif self.dimension == 3:
            self.x, self.z, self.y = coordinates

        else:
            raise ValueError("You must enter between 2 and 3 attributes.")

    def __init__(self, *coordinates):
        self.__set_coordinates(*coordinates)
        if self.dimension == 2:
            self.z = 0
            self.dimension += 1

    @property
    def coordinates(self):
        return self.dimension

    @coordinates.setter
    def coordinates(self, coordinates):
        self.__set_coordinates(*coordinates)

    def __str__(self):
        return f"Point coordinates: (x: {self.x}, z: {self.z}, y: {self.y})"

    @classmethod
    def create(cls):
        return cls(*cls.default_coordinates)

    def __eq__(self, other):
        if not isinstance(other, Point):
            raise NotImplementedError(
                f"Cannot compare Point with {type(other).__name__}")
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __lt__(self, other):
        if not isinstance(other, Point):
            raise NotImplementedError(
                f"Cannot compare Point with {type(other).__name__}")
        return (self.x, self.y, self.z) < (other.x, other.y, other.z)

    def __add__(self, other):
        return Point(self.x + other.x, self.z + other.z, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.z - other.z, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.z * other.z, self.y * other.y)

    def __floordiv__(self, other):
        return Point(self.x // other.x, self.z // other.z, self.y // other.y)

    def __truediv__(self, other):
        return Point(self.x / other.x, self.z / other.z, self.y / other.y)

    def __mod__(self, other):
        return Point(self.x % other.x, self.z % other.z, self.y % other.y)

    def __pow__(self, other):
        return Point(self.x ** other.x, self.z ** other.z, self.y ** other.y)
