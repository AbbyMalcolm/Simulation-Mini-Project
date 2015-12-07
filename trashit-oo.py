import runWorld as rw
import drawWorld as dw
import pygame as pg
import math

from random import randint
print(randint(1,5))

################################################################

# Initialize world
name = "Trash it!"
width = 500
height = 500
rw.newDisplay(width, height, name)

################################################################

# Display the state by drawing trash and a trash can
myimage = dw.loadImage("papertrash.bmp")

otherimage = dw.loadImage("recycle.bmp")

# state -> image (IO)
# draw the trash at the bottom, center of the screne and
# paper trash at the top
def updateDisplay(state):
    dw.fill(dw.white)
    dw.draw(myimage, (state.xpos, state.yvel))
    dw.draw(otherimage, (width/2, height-100))


################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).

# state -> state
def updateState(state):
    state.yvel += 1
    return state

################################################################

# Terminate the simulation when the trash misses the trash can, generate
# another paper trash if the preceding one is placed in the can

def endState(state):
    x1, y1, x2, y2 = width/2, height-100, state.xpos, state.yvel
    x = math.fabs(x2-x1)
    y = math.fabs(y2-y1)
    if (y < 30 and x < 30):
        state.xpos = 100
        state.yvel = 100
        return False
    #dw.draw(myimage, (100, 100))
    if y < 10:
        return True

################################################################

# state -> event -> state

def handleEvent(state, event):
    key_pressed = pg.key.get_pressed()
    if key_pressed[pg.K_LEFT]:
        state.xpos -= 10
        return state
    elif key_pressed[pg.K_RIGHT]:
        state.xpos += 10
        return state
    else:
        return(state)

################################################################

# World state will be single x coordinate at left edge of world

# The cat starts at the left, moving right
#initState = (0, 1)
class State:
    xpos = 0
    yvel = 1

initState = State()

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
