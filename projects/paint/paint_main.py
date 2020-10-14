from module_paint.Rectangle import Rectangle
from module_paint.Circle import Circle
from module_paint.ShapeMaker import Maker

# maker = Maker()
#
# p1 = {'x': 10, 'y': 10}
# p2 = {'x': 40, 'y': 40}
# maker.add_rect(p2, p2)
#
# p1 = {'x': 25, 'y': 20}
# p2 = {'x': 70, 'y': 70}
# maker.add_circle(p1, p2)
#
# p1 = {'x': 22, 'y': 15}
# p2 = {'x': 63, 'y': 65}
# maker.add_circle(p1, p2)
#
# list_of_shapes = maker.get_shapes_cir()
#
# for shape in list_of_shapes:
#     print(shape)

r = Rectangle()
c = Circle()

p1 = {'x': 10, 'y': 10}
p2 = {'x': 40, 'y': 40}
r.draw(p1, p2)

p1 = {'x': 25, 'y': 20}
p2 = {'x': 70, 'y': 70}
c.draw(p1, p2)

p1 = {'x': 22, 'y': 15}
p2 = {'x': 63, 'y': 65}
c.draw(p1, p2)

for shape in c.get_shapes():
    print(shape)