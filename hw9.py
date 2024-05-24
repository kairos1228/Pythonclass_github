class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            return False
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def show(self):
        lt = (self.x1, self.y1)
        rb = (self.x2, self.y2)
        print(f'좌측 상단 꼭지점이 {lt}이고 우측 하단 꼭지점이 {rb}인 사각형입니다.', end = '')

    def getWidth(self):
        return self.x2 - self.x1

    def getHeight(self):
        return self.y2 - self.y1

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())

# 주 프로그램부

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')