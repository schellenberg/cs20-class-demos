#move fast
think(0)

#step off goal/home
move()

#keep going until you get back to the start
while not at_goal():
    #pick up an apple if there's one here
    if object_here():
        take()
    
    #only move forward if you won't crash into a wall
    if front_is_clear():
        move()
    #if you would crash into a wall, turn left
    else:
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
