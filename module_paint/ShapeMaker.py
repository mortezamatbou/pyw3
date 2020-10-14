from module_paint.Circle import Circle
from module_paint.Rectangle import Rectangle


class Maker:
    __rect = ''
    __circle = ''

    def __init__(self):
        self.__rect = Rectangle()
        self.__circle = Circle()

    def add_circle(self, p1: dict, p2: dict):
        self.__circle.draw(p1, p2)

    def add_rect(self, p1: dict, p2: dict):
        self.__rect.draw(p1, p2)

    def get_shapes(self):
        return self.__rect.get_shapes()

    def get_shapes_cir(self):
        return self.__circle.get_shapes()


class MySingleton:
    __instance = None

    def __init__(self):
        if self.__instance == None:
            pass
        else:
            self.__instance = self

    @staticmethod
    def get_instance(self):
        if self.__instance == None:
            raise Exception("")
