class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, first_point, second_point):
        self.first_point = Point(x, y)
        self.second_point = Point(x, y)

    def draw(Canvas, fill_color):
        canvas.create_line(
            x1, y1, x2, y2, fill=fill_color, width=2
        )
