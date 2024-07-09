class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point

    def draw(self, Canvas, fill_color):

        x1, y1 = self.first_point.x, self.first_point.y
        x2, y2 = self.second_point.x, self.second_point.y

        Canvas.create_line(
            x1, y1, x2, y2, fill=fill_color, width=2
        )
