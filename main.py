import numpy as np
from cmu_graphics import *
from types import SimpleNamespace
import os
import time
import random
from map import *

msg = "Roll for initiative:"
print(msg)

print(np.random.randint(1,20))

def onAppStart(app):
    app.states = "testing" #home. build, play
  
    app.width = 1100
    app.height = 700
    
    app.maps = [None, None, None, None]
    app.selectedMap = None

    restart(app)

def onStep(app):
    pass

def posToCell():
    pass

def restart(app):
    app.state = "intro" #intro, build, play
    app.rows = app.cols = 5
    changeMapWidth(app)
    changeMapHeight(app)
    app.map = Map(app.rows, app.cols)
    print(app.map)

#Drawing

def redrawAll(app):
    if app.state == "testing":
        drawBuildUI(app)
        drawBuildMap(app)
    elif app.state == 'intro':
        drawIntro(app)

def drawIntro(app):
    pass

def drawBuildUI(app):
    drawRect(0, 0, app.width, 100, fill='dark')
    pass

def drawBuildMap(app):
    pass

#End Drawing
#Loading
def loadMap(app):
    pass

#End Loading

def changeMapHeight(app):
    height = app.getTextInput('Enter the height of the map: ')
    isInt = height.isdigit()
    if not isInt:
        app.showMessage('Please enter an integer!')
        changeMapHeight(app)
        return
    height = int(height)
    moreThan5 = height >= 5
    if not moreThan5:
        app.showMessage('Please enter a number greater than 5!')
        changeMapHeight(app)
        return
    app.rows = height

def changeMapWidth(app):
    width = app.getTextInput('Enter the width of the map: ')
    isInt = width.isdigit()
    if not isInt:
        app.showMessage('Please enter an integer!')
        changeMapWidth(app)
        return
    width = int(width)
    moreThan5 = width >= 5
    if not moreThan5:
        app.showMessage('Please enter a number greater than 5!')
        changeMapWidth(app)
        return
    app.cols = width


def onKeyPress(app, keys):
    pass

def main():
    print("blehh")
    runApp()

main()


