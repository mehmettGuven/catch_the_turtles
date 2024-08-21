import turtle
import random

drawing_board = turtle.Screen()
drawing_board.bgcolor('light blue')
drawing_board.title('Catch The Turtle')
FONT=('Arial', 30, 'normal')
grid_size=10
turtle_list = []
score=0
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()
game_over  = False
x_coordinates = [-20,-10,0,10,20]
y_coordinates = [-10,0,10,20]

def setup_score_turtle():
    score_turtle.color("dark blue")
    score_turtle.hideturtle()
    score_turtle.penup()
    top_height = drawing_board.window_height() / 2
    y = top_height * 0.8
    score_turtle.setpos(0,y)
    score_turtle.write('Score = 0',False,"center",FONT)

def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(a,y):
        global score
        score+=1
        score_turtle.clear()
        score_turtle.write(f'Score = {score}', False, "center", FONT)
        #print(x,y)

    t.onclick(handle_click)
    t.penup()
    t.shape('turtle')
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x*grid_size,y*grid_size)
    turtle_list.append(t)

def setup_turtle():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        drawing_board.ontimer(show_turtles_randomly,500)

def countdown(time):
    global game_over
    countdown_turtle.color("dark blue")
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = drawing_board.window_height() / 2
    y = top_height * 0.8
    countdown_turtle.setpos(0, y-40)




    if time >0:
        countdown_turtle.clear()
        countdown_turtle.write(f'Time = {time}', False, "center", FONT)
        drawing_board.ontimer(lambda:countdown(time-1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write('Game Over', False, "center", FONT)

def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    countdown(10)
    setup_turtle()
    hide_turtles()
    show_turtles_randomly()
    turtle.tracer(1)

start_game_up()
turtle.mainloop()

