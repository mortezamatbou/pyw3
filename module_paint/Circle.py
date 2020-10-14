from module_paint.Shapes import Shapes as Sh2


class Circle(Sh2):

    def draw(self, p1: dict, p2: dict):
        message = "Draw a Circle by [{x1},{y1}] -> [{x2},{y2}]"
        message = message.format(x1=p1['x'], y1=p1['y'], x2=p2['x'], y2=p2['y'])
        self.add_shape('cir', p1, p2)