from graphics import Window
from draws import Point, Line


def main():
    win = Window(800,600)

    p1 = Point(100, 100)
    p2 = Point(200, 200)
    my_line = Line(p1, p2)

    win.draw_line(my_line, "white")

    win.wait_for_close()

main()
