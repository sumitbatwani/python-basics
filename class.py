class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# point1 = Point()
# point1.draw()
# point1.move()
# point1.x = 10
# print(point1.x)

# point2 = Point()
# point2.draw()
# point2.move()
# print(point2.x) # attribute not available on point2

point = Point(10, 20)
print(point.x)
