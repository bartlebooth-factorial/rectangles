import turtle
import random


class Rectangle:
    def __init__(self, coords, dimens, fill_color):
        self.x = coords[0]
        self.y = coords[1]
        self.width = dimens[0]
        self.height = dimens[1]
        self.fill_color = fill_color

    def draw(self, pen):
        pen.penup()
        pen.goto(self.x - (self.width // 2), self.y - (self.height // 2))
        pen.pendown()
        pen.fillcolor(self.fill_color)
        pen.begin_fill()

        for _ in range(2):
            pen.forward(self.width)
            pen.left(90)
            pen.forward(self.height)
            pen.left(90)

        pen.end_fill()

    def is_inside(self, x, y):
        xpos = int(self.x - (self.width // 2))
        ypos = int(self.y - (self.height // 2))
        xbounds = range(xpos, xpos + self.width)
        ybounds = range(ypos, ypos + self.height)
        if x in xbounds and y in ybounds:
            return True
        return False


class Display:
    def __init__(self):
        self.t = turtle.Turtle()
        self.scr = turtle.Screen()
        self.rectangles = []
        self.fill_colors = [
                'yellow', 'gold', 'orange', 'red', 'maroon', 'violet',
                'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan',
                'turquoise', 'lightgreen', 'green', 'darkgreen',
                'chocolate', 'brown', 'black', 'gray'
                ]
        self.user_score = 0
        self.play = True

        self.t.speed(0)
        self.t.hideturtle()

        self.scr.setup(width = 1.0, height = 1.0)
        self.scr.bgcolor("white")
        self.scr.onclick(self.mouse_input)
        self.scr.onkey(self.leave, 'q')
        self.scr.onkey(self.retry, 'r')
        self.scr.listen()
        self.scr.mainloop()

    def reset(self):
        self.rectangles = []
        self.scr.bgcolor("white")
        self.scr.onclick(self.mouse_input)
        self.scr.onkey(self.leave, 'q')
        self.scr.onkey(self.retry, 'r')
        self.scr.listen()

    def add_rectangle(self, coords):
        rectangle = Rectangle(
                coords,
                (random.randint(300, 900), random.randint(300, 900)),
                self.fill_colors[random.randint(0, len(self.fill_colors) - 1)]
                )
        rectangle.draw(self.t)
        self.rectangles.append(rectangle)

    def end(self):
        self.play = False

        self.scr.clear()
        self.reset()

        self.t.penup()
        self.t.goto(0, 0)
        self.t.pendown()
        self.t.write(
                f'Game over! Your score is {self.user_score}',
                font = ('Arial', 48, 'normal'),
                align = 'center'
                )
        self.check_high_score(self.user_score)

    def check_high_score(self, score):
        with open('high_score_rectangles.txt') as reader:
            data = reader.read()
        high_score = int(data)

        if score > high_score:
            high_score = score
            with open('high_score_rectangles.txt', 'w') as writer:
                writer.write(str(high_score))

            self.t.penup()
            self.t.goto(0, -200)
            self.t.pendown()
            self.t.write(
                    f'New high score!',
                    font = ('Arial', 48, 'normal'),
                    align = 'center'
                    )

        self.t.penup()
        self.t.goto(0, -100)
        self.t.pendown()
        self.t.write(
                f'High score: {high_score}',
                font = ('Arial', 48, 'normal'),
                align = 'center'
                )

    def mouse_input(self, x, y):
        if self.play:
            for rectangle in self.rectangles:
                if rectangle.is_inside(x, y):
                    game_over = True
                    break
            else:
                game_over = False

            if game_over:
                self.end()
            else:
                self.user_score += 1
                self.add_rectangle((x, y))

    def leave(self):
        self.scr.bye()

    def retry(self):
        self.play = True
        self.scr.clear()
        self.reset()
        self.user_score = 0


if __name__ == '__main__':
    d = Display()
