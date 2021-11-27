import turtle

def get_mid_point(point_1: list, point_2: list):

    return ((point_1[0] + point_2[0]) / 2, (point_1[1] + point_2[1]) / 2)

def triangle(turtle: turtle, points, depth):

    turtle.penup()
    turtle.goto(points[0][0], points[0][1])

    turtle.pendown()
    turtle.goto(points[1][0], points[1][1])
    turtle.goto(points[2][0], points[2][1])
    turtle.goto(points[0][0], points[0][1])

    if depth > 0:

        triangle(turtle, [points[0], get_mid_point(points[0], points[1]), get_mid_point(points[0], points[2])], depth-1)
        triangle(turtle, [points[1], get_mid_point(points[0], points[1]), get_mid_point(points[1], points[2])], depth-1)
        triangle(turtle, [points[2], get_mid_point(points[2], points[1]), get_mid_point(points[0], points[2])], depth-1)

if __name__ == '__main__':

    turtle.title('Hi! I\'m Bob the turtle!')
    turtle.setup(width=800, height=800)

    larry = turtle.Turtle(shape='turtle')
    larry.color('purple')

    points = [[-175, -125], [0, 175], [175, -125]]  # size of triangle

    triangle(larry, points, 5)

    turtle.exitonclick()
