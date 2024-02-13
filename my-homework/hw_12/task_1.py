from math import pi, sqrt

class Shape:
    def area(self) -> float:
        raise NotImplementedError("Area method must be implemented in subclass")

    def perimeter(self) -> float:
        raise NotImplementedError("Perimeter method must be implemented in subclass")


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return round(pi * self.radius ** 2, 2)

    def perimeter(self) -> float:
        return round(2 * pi * self.radius)


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self) -> float:
        s = (self.side1 + self.side2 + self.side3) / 2
        return sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3



if __name__ == "__main__":
    def test_circle(radius, exp_area, exp_perimeter):
        circle = Circle(radius)
        assert circle.area() == exp_area
        assert circle.perimeter() == exp_perimeter

    radius = 3
    exp_area = 28.27
    exp_perimeter = 19
    test_circle(radius, exp_area, exp_perimeter)


    def test_rectangle(length, width, exp_area, exp_perimeter):
        rectangle = Rectangle(length, width)
        assert rectangle.area() == exp_area
        assert rectangle.perimeter() == exp_perimeter

    length = 4
    width = 5
    exp_area = 20
    exp_perimeter = 18
    test_rectangle(length, width, exp_area, exp_perimeter)


    def test_triangle(s1, s2, s3, exp_area, exp_perimeter):
        triangle = Triangle(s1, s2, s3)
        assert triangle.area() == exp_area
        assert triangle.perimeter() == exp_perimeter

    s1 = 3
    s2 = 4
    s3 = 5
    exp_area = 6.0
    exp_perimeter = 12
    test_triangle(s1, s2, s3, exp_area, exp_perimeter)



