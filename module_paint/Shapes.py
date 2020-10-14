class Shapes:
    # __shapes = []

    def __init__(self):
        self.__shapes = []

    def draw(self, p1: dict, p2: dict):
        pass

    def remove(self):
        pass

    def move(self):
        pass

    def add_shape(self, shape_type: str, p1: dict, p2: dict):
        self.__shapes.append({'type': shape_type, 'p1': p1, 'p2': p2})

    def get_shapes(self):
        return self.__shapes
