from graphics import Window
from draws import Point, Line


def main():
    win = Window(800,600)

    win.draw_line( 32,"white")

    win.wait_for_close()

main()
