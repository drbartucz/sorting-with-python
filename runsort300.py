import pygame as pg
import random
from sys import exit

# this is an extension for runsort.py - do that part first!

def dosort():

    # fill in your code here

    return


# ******************************************************************************************************
# You do not need to change any of the code below, but there is no harm in understanding what it does! *
# ******************************************************************************************************

# Set the dimensions of the window and display it
display = pg.display.set_mode((700, 700))

# set the colors to a random selection
colors = ["#%06x" % random.randint(0, 0xFFFFFF) for _ in range(300)]

# create a randomly sorted list of blocks from 1-300
blocks = [i for i in range(1, 301)]
random.shuffle(blocks)

# basically just keep the window open until they kill it
def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

# Swap two blocks (and update the visualization)
def swap(left, right):

    pg.draw.rect(display, "#CBC3E3", (60 + left * 2, 650 - 2 * blocks[left], 2, 2 * blocks[left]))
    pg.draw.rect(display, "#CBC3E3", (60 + right * 2, 650 - 2 * blocks[right], 2, 2 * blocks[right]))

    # swap the blocks
    tmp = blocks[left]
    blocks[left] = blocks[right]
    blocks[right] = tmp

    # redraw the 2 blocks
    pg.draw.rect(display, colors[left], (60 + left * 2, 650 - 2 * blocks[left], 2, 2 * blocks[left]))
    pg.display.update(60 + left * 2, 650 - 2 * blocks[left], 2, 2 * blocks[left])
    pg.draw.rect(display, colors[right], (60 + right * 2, 650 - 2 * blocks[right], 2, 2 * blocks[right]))
    pg.display.update(60 + right * 2, 650 - 2 * blocks[right], 2, 2 * blocks[right])
    check_events()
    # pg.time.wait(500)  # slow down the visualization


if __name__ == "__main__":
    # the program that is run
    try:
        pg.display.init()
        display.fill(pg.Color("#CBC3E3"))  # clear the window
        swap(1, 1)  # draw the randomized blocks
        pg.display.update()
        check_events()
        dosort()  # run the sorting algorithms
        while True:
            check_events()
    except Exception as error:
        print("An exception occurred:", type(error).__name__)
