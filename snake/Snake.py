import random
import curses

# init the screen
s = curses.initscr()
# hide the cursor so it doesn't show
curses.curs_set(0)
# get the width and height 
sh, sw = s.getmaxyx()
# create a new window using height, width
# start at top
w = curses.newwin(sh, sw, 0, 0)
# have the window accept keypad input
w.keypad(1)
# refresh screen every 100ms
w.timeout(100)

# create the snake's initial position
snk_x = sw/4
snk_y = sh/2

# create initial snake body parts
# head and then 2 body parts
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# create food with starting place as center
food = [sh/2, sw/2]
# add it to the screen
w.addch(food[0], food[1], curses.ACS_PI)

# tell snake where he's going initially
key = curses.KEY_RIGHT

# Begin snake movement loop
while True:
    # see what the next key is
    next_key = w.getch()
    # return either nothing or the next key pressed
    key = key if next_key == -1 else next_key

    # check if game over
    # if y position ([0,0]) is either at the top or height of the screen
    # or if the x position ([0][1]) is to the left or the width of screen
    # or if the snake is in itself
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        # kill the window and quit
        curses.endwin()
        quit()


    # determine what the new head of the snake will be
    # start by taking the old head of the snake
    new_head = [snake[0][0], snake[0][1]]

    # figure out what the key being clicked is
    # up and left will be negative, down and right will be positive
    if key == curses.KEY_DOWN:
            new_head[0] += 1
    if key == curses.KEY_UP:
            new_head[0] -= 1
    if key == curses.KEY_LEFT:
            new_head[1] -= 1         
    if key == curses.KEY_RIGHT:
            new_head[1] += 1

    # insert new head of snake
    snake.insert(0, new_head)

    # determine whether snake has run into food
    if snake[0] == food:
        # if so we have to remove the food
        # and generate a new piece of food
        # start by setting food to None 
        food = None
        while food is None:
        # try create a new piece of food
            nf = [
                # new food location
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            # if food in snake start over
            food = nf if nf not in snake else None
        # now that it's selected, add food to the screen
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        # get the tail of the snake
        tail = snake.pop()
        # add space where tailpiece was
        w.addch(tail[0], tail[1], ' ')

    # add the head of the snake to the screen
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)


