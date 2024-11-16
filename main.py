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
    app.states = "intro" #intro, build, play  
    app.width = 1100
    app.height = 700
    
    app.maps = [None, None, None, None]
    app.selectedMap = None

    restart(app)

def restart(app):
    app.state = "intro" #intro, build, play

#Loading
def loadMap(app):
    app.rows = app.cols = 5
    changeMapWidth(app)
    changeMapHeight(app)
    app.map = Map(app.rows, app.cols)
    print(app.map)

#End Loading

#Drawing

def redrawAll(app):
    if app.state == "testing":
        drawBuildUI(app)
        drawBuildMap(app)
    elif app.state == 'intro':
        drawIntro(app)

def drawIntro(app):
    drawRect(0, 0, app.width, app.height, fill='darkblue', opacity=70)
    drawLabel('STOPDOT', app.width/2, app.height/3, bold=True, size=100, font='arial', fill='white', opacity=50)

    #Buttons

def drawBuildUI(app):
    #Menus
    topMenuWidth = app.width-200
    borderWidth = 5
    drawRect(0, 0, topMenuWidth + borderWidth, 100, fill='darkblue', opacity=70, border='black', borderWidth=borderWidth) #top menu
    drawRect(topMenuWidth, 0, 200, 700, fill='darkblue', opacity=70, border='black', borderWidth=borderWidth) #side bar
    
    #Buttons


def drawBuildMap(app):
    pass

#End Drawing


def onStep(app):
    pass

def posToCell():
    pass

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

def onStep(app):
    pass

def posToCell():
    pass

def onKeyPress(app, keys):
    pass

def main():
    print("blehh")
    runApp()

main()


