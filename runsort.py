import pygame as pg
import random

# this is your function to fill in!
def dosort():
  return
  
# You do not need to change any of the code below, but there is no harm in understanding what it does!

# Set the dimensions of the window and display it
display = pg.display.set_mode(600,600)

# set the colors:
colors = ("#ff0000", "#e81416", "#ffa500", "#faeb36", "#b9d725", "#79c314", "#487de7", "#4b369d", "#70369d", "#301934")
# create a randomly sorted list of blocks from 1-10
blocks = random.shuffle(i for i in range(1,11))

# The swap function also updates the visualization
def swap(left, right):
    display.fill(pg.Color("#CBC3E3")) # clear the window
    for i in range(10):
        # draw the rectangles
        # pg.draw.rect(dsiplay_window, color_of_rectangle, size_of_rectangle)
        pg.draw.rect(display, colors[block_list[i]], (25+i*50,550,50,-block_list[i] * 50))
    check_events()
    pg.display.update()


# the program that is run
if __name__ == "__main__":
        try:
          randomize() # randomize the blocks
          swap(1,1) # draw the blocks
          while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            pygame.time.wait(100) # slow down the visualization
          except:
            print("Error.")
