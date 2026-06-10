#move fast
think(0)

def turn_around():
    turn_left()
    turn_left()

def fix_column():
    #face north
    turn_left()
    #move all the way up the column, picking up all carrots
    repeat 8:
        move()
        #don't know how many carrots are here, so use a while loop
        while object_here():
            take()
    #face south
    turn_around()
    #move back down the column, placing one carrot at each spot
    repeat 6:
        move()
        put()
    #go to bottom wall, so the next time i call the function, i'm in the same starting spot
    repeat 2:
        move()
    #face east
    turn_left()
    #get underneath the next column to fix
    move()

#get under the first column
move()
move()

#there are 6 columns of garden to fix
#so my fix_column function should end ready for the next
repeat 6:
    fix_column()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
