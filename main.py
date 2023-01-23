import math

class Polygon:
  def __init__(self, sides):
    super().__init__()
    self.sides = sides

  def num_sides(self):
    return len(self.sides)

  def perimeter(self):
    return sum(self.sides)


class Triangle(Polygon):
  def __init__(self, side1, side2, side3):
    Polygon.__init__(self, [side1, side2, side3])

  def area(self):
    [a, b, c] = self.sides

    s = (a + b + c) / 2

    return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Quadrilateral(Polygon):
  def __init__(self, side1, side2, side3, side4):
    Polygon.__init__(self, [side1, side2, side3, side4])


class RegularPolygon(Polygon):
  def __init__(self, num_sides, side):
    self.side = side
    self.sides = [side] * num_sides

  def exterior_angle(self):
    return 2 * math.pi / self.num_sides()

  def interior_angle(self):
    return math.pi - self.exterior_angle()

  def area(self):
    radius = 1 / 2 * self.side / math.sin(self.exterior_angle() / 2)

    slice_area = 1 / 2 * radius ** 2 * math.sin(self.exterior_angle())

    return slice_area * self.num_sides()


class Rectangle(Quadrilateral):
  def __init__(self, width, height):
    Quadrilateral.__init__(self, width, height, width, height)
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height


class Square(Rectangle, RegularPolygon):
  def __init__(self, side):
    RegularPolygon.__init__(self, 4, side)
    Rectangle.__init__(self, width=side, height=side)


class EquilateralTriangle(RegularPolygon, Triangle):
  def __init__(self, side):
    RegularPolygon.__init__(self, 3, side)
    Triangle.__init__(self, side, side, side)
    
emma = EquilateralTriangle(4)