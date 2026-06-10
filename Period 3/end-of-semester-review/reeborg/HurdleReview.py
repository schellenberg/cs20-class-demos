#move fast
think(0)

def turn_right():
    repeat 3:
        turn_left()

def jump_hurdle():
    #face north
    turn_left()
    #go all the way up the hurdle
    while wall_on_right():
        move()
    #face east
    turn_right()
    #take one step 
    move()
    #if the hurdle extends horizontally, go to end of it
    while wall_on_right():
        move()
    #face south
    turn_right()
    #head to south edge
    while front_is_clear():
        move()
    #face east again, like i was at the start
    turn_left()

#keep going until you get to the flag/goal
while not at_goal():
    #if nothing in front of you, just move
    if front_is_clear():
        move()
    #otherwise, jump over the hurdle
    else:
        jump_hurdle()
        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
