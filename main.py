# How to escape a maze using code :)

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if not front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif front_is_clear and right_is_clear():
        move()
    elif front_is_clear():
        if right_is_clear():
            turn_right()
        move()
    else:
        turn_left()
       
    
    