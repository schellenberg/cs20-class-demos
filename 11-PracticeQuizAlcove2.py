import library as lib 

def pick_move_flower():
    take()
    while front_is_clear():
        move()
    put()
    lib.turn_around()
    while front_is_clear():
        move()
    lib.turn_around()

def check_for_flower():
    turn_left()
    move()
    lib.turn_around()
    if object_here():
        pick_move_flower()
    move()
    turn_left()

think(10)
repeat 6:
    move()
    check_for_flower()
    if front_is_clear():
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
    
