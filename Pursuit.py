from turtle import Turtle, Screen
import time

# SCREEN
screen = Screen()

def screen_width():
    return screen.window_width()


def screen_height():
    return screen.window_height()


def config_screen():
    screen.title('Autorama')
    screen.setup(1360, 768, 0, 0)
    screen.tracer(0, 0)

# SPEEDWAY
pista = Turtle()
pista.hideturtle()
pista.speed(0)

def arco_pista_maior():
    pista.forward(2 * screen_width() / 5)
    pista.circle(2 * screen_height() / 5, 180)

def arco_pista_menor():
    pista.forward(2 * screen_width() / 5)
    pista.circle(screen_height() / 5, 180)

def pontilhado_pista_reto():
    for i in range(4):
        pista.forward(screen_width() / 20)
        pista.penup()
        pista.forward(screen_width() / 20)
        pista.pendown()

def pontilhado_pista_curva():
    for i in range(5):
        pista.circle(1.5 * screen_height() / 5, 20)
        pista.penup()
        pista.circle(1.5 * screen_height() / 5, 20)
        pista.pendown()

def pontilhado_reto2():
    for i in range(4):
        pista.forward(screen_width() / 20)
        pista.pendown()
        pista.forward(screen_width() / 20)
        pista.penup()

def pontilhado_curva2():
    for i in range(5):
        pista.circle(1.5 * screen_height() / 5, 20)
        pista.pendown()
        pista.circle(1.5 * screen_height() / 5, 20)
        pista.penup()

def draw_pista():
    pista.pensize(3)
    pista.penup()
    pista.goto(-screen_width() / 2, -screen_height() / 2)
    pista.forward(screen_width() / 5)
    pista.left(90)
    pista.forward(screen_height() / 5 - screen_height() / 10)
    pista.right(90)
    pista.forward(1 * screen_width() / 10)
    pista.pendown()
    pista.fillcolor("black")
    pista.begin_fill()
    arco_pista_maior()
    arco_pista_maior()
    pista.end_fill()
    pista.left(90)
    pista.penup()
    pista.forward(screen_height() / 5)
    pista.pendown()
    pista.right(90)
    pista.fillcolor("white")
    pista.begin_fill()
    arco_pista_menor()
    arco_pista_menor()
    pista.end_fill()
    pista.penup()
    pista.right(90)
    pista.forward(screen_height() / 10)
    pista.left(90)
    pista.pendown()
    pista.pencolor("white")
    pontilhado_pista_reto()
    pontilhado_pista_curva()
    pista.undo()
    pista.undo()
    pontilhado_reto2()
    pontilhado_curva2()
    pista.undo()
    pista.undo()

# CARS
player1 = Turtle()
player1.speed(0)
player1.penup()

player2 = Turtle()
player2.speed(0)
player2.goto(100, 100)
player2.penup()

players = {
    1: player1,
    2: player2
}

up_keys = {
    1: ["Up"],
    2: ["W", "w"]
}
down_keys = {
    1: ["Down"],
    2: ["S", "s"]
}
left_keys = {
    1: ["Left"],
    2: ["A", "a"]
}
right_keys = {
    1: ["Right"],
    2: ["D", "d"]
}

has_pressed_up_1 = False
has_pressed_up_2 = False
has_pressed_down_1 = False
has_pressed_down_2 = False
move_speed = 0.5
turn_speed = 15
player_ratio = 15
gameover = False

def update_player(player):
    switch(player, player.heading())

    for p in players.values():
        if p != player:
            d = player.distance(p.xcor(), p.ycor())
            if d < 2*player_ratio:
                globals()['gameover'] = True

def car_image(angle):
    return "red_viper_" + str(int(angle)) + ".gif"

def forward(player):
    player.forward(move_speed)

def backward(player):
    player.backward(move_speed)

def left(player):
    def l():
        player.left(turn_speed)

    return l

def right(player):
    def r():
        player.right(turn_speed)

    return r

def switch(player, x):
    player.shape(car_image(x))

def register_car_shapes():
    for a in range(0, 360, 15):
        screen.addshape(car_image(a))

def used_button(player, btn, action):
    def p_up():
        globals()['has_pressed_' + btn  + '_' + str(player)] = action

    return p_up

def move_car():
    if has_pressed_up_1:
        forward(player1)

    if has_pressed_up_2:
        forward(player2)

    if has_pressed_down_1:
        backward(player1)

    if has_pressed_down_2:
        backward(player2)


# GAME
def start():
    screen.bgcolor("green")
    config_screen()
    register_car_shapes()
    draw_pista()

    for i, p in players.items():
        for k in up_keys[i]:
            screen.onkeypress(used_button(i, "up", True), k)
            screen.onkeyrelease(used_button(i, "up", False), k)

        for k in down_keys[i]:
            screen.onkeypress(used_button(i, "down", True), k)
            screen.onkeyrelease(used_button(i, "down", False), k)

        for k in left_keys[i]:
            screen.onkey(left(p), k)

        for k in right_keys[i]:
            screen.onkey(right(p), k)


def update():
   update_player(player1)
   update_player(player2)
   move_car()

start()
while not gameover:
    screen.listen()
    update()
    screen.update()
