class Area:
    def __init__(self, width, height):
        # Setting the width and height as private
        self._width = width
        self._height = height

    def compute_area(self, width, height):
        return self._width * self._height


area1 = Area(5,4)
print(area1.compute_area(5,4))
