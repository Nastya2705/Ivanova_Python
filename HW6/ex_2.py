class Road:
    def __init__(self, _length, _width):
        self.length = _length
        self._width = _width
    def mass(self):
        return self._length * self._width

class MassCount(Road):
    def __init__(self, _length,_width, volume):
        super().__init__(_length, _width)
        self.volume = volume

r = MassCount(25, 5000, 25)
print(r.mass())