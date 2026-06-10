#move fast
think(0)

#guarantee i'm facing north
while not is_facing_north():
    turn_left()

#now turn to face south
repeat 2:
    turn_left()

#go to bottom edge of world
while front_is_clear():
    move()

#face west
repeat 3:
    turn_left()
    
#head to west edge
while front_is_clear():
    move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
