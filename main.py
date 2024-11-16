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
    app.states = ["intro", 'build', 'play', 'load'] #intro, build, play, load
    app.width = 1100
    app.height = 700
    
    app.maps = [None, None, None, None]
    app.selectedMap = None

    #buttons
    app.buttonLocations = set()
    app.buttonFunctions = {}

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
    if app.state == "build":
        drawBuildUI(app)
        drawBuildMap(app)
    elif app.state == 'intro':
        drawIntro(app)
    elif app.state == 'load':
        drawLoad(app)

def drawIntro(app):
    drawRect(0, 0, app.width, app.height, fill='darkblue', opacity=70)
    drawLabel('STOPDOT', app.width/2, app.height/3, bold=True, size=100, font='arial', fill='white', opacity=50)

    #Edit Button
    editButtonSize = 80
    drawRect(app.width/2-editButtonSize/2-150, app.height/2-editButtonSize/2, editButtonSize+300, editButtonSize, fill='midnightblue', opacity=80, border='black', borderWidth=5)
    drawLabel('Edit Build', app.width/2, app.height/2, size=editButtonSize, fill='white', opacity=50)
    newButton(app, app.width/2-editButtonSize/2-150, app.height/2-editButtonSize/2, app.width/2-editButtonSize/2-150+editButtonSize+300, app.height/2+editButtonSize/2, clickEditBuild)
    
    #Load Button
    loadButtonSize = 80
    drawRect(app.width/2-loadButtonSize/2-150, app.height/2-loadButtonSize/2 + 100, loadButtonSize+300, loadButtonSize, fill='midnightblue', opacity=80, border='black', borderWidth=5)
    drawLabel('Load Build', app.width/2, app.height/2 + 100, size=loadButtonSize, fill='white', opacity=50)
    newButton(app, app.width/2-loadButtonSize/2-150, app.height/2-loadButtonSize/2 + 100, app.width/2-loadButtonSize/2-150+loadButtonSize+300, app.height/2+loadButtonSize/2 + 100, clickLoadBuild)

def drawBuildUI(app):
    #Menus
    topMenuWidth = app.width-200
    borderWidth = 5
    drawRect(0, 0, topMenuWidth + borderWidth, 100, fill='darkblue', opacity=70, border='black', borderWidth=borderWidth) #top menu
    drawRect(topMenuWidth, 0, 200, 700, fill='darkblue', opacity=70, border='black', borderWidth=borderWidth) #side bar
    
    #Menu Button
    menuButtonSize = 100
    drawLabel('Menu', 130, 50, size=menuButtonSize, fill='white', opacity=50)
    newButton(app, 0, 0, 130+menuButtonSize+50, 50+menuButtonSize, clickMenu)

def drawLoad(app):
    drawRect(0, 0, app.width, app.height, fill='darkblue', opacity=70)
    drawLabel('Pick a map to load', app.width/2, app.height/4, bold=True, size=100, font='arial', fill='white', opacity=50)



def drawBuildMap(app):
    pass

#End Drawing

#Button Functions
def newButton(app, toplx, toply, botrx, botry, func):
    topLeft = (toplx, toply)
    botRight = (botrx, botry)
    location = (topLeft, botRight)
    app.buttonLocations.add(location)
    app.buttonFunctions[location] = func

def clickMenu(app):
    app.state = 'intro'

def clickEditBuild(app):
    app.state = 'build'

def clickLoadBuild(app):
    app.state = 'load'

#End Button Functions

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

def onMousePress(app, mouseX, mouseY):
    #check buttons
    for location in app.buttonLocations:
        isBetweenX = location[0][0] <= mouseX <= location[1][0]
        isBetweenY = location[0][1] <= mouseY <= location[1][1]
        if (isBetweenX) and (isBetweenY):
            app.buttonFunctions[location](app)

def main():
    print("blehh")
    runApp()

main()


