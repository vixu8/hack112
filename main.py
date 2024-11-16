import numpy as np
from cmu_graphics import *
from types import SimpleNamespace
import os
import time
import random
from map import *
from character import *

msg = "Roll for initiative:"
print(msg)

print(np.random.randint(1,20))

def onAppStart(app):
    app.stepsPerSecond = 100

    app.state = "testing" #home. build, play
  
    app.width = 1100
    app.height = 700

    app.blockPx = 40
    
    app.g = 10 #gravity, in terms of pixels

    app.maps = [None, None, None, None]
    app.selectedMap = Map(15,20)

    for  i in range(5):
        app.selectedMap.map[10+i][10] = 1

    print(app.selectedMap)

    app.char = Character("main", 100, 100, 80,30)

    #restart(app)

def onStep(app):
    if app.state == "testing":

        physics(app,app.char, app.selectedMap)

        app.char.x += app.char.vx
        app.char.y += app.char.vy
        app.char.updateCoords()

        
def physics(app, character, map):
    if character.botCell < map.rows:
        if map.getSquareType(character.botCell, character.leftCell) == "block" or map.getSquareType(character.botCell, character.rightCell) == "block":
            character.vx = 0
            character.x = (character.botCell)*app.blockPx - character.height/2
        else: character.vx += app.g/5

    

# def startPlay(app):
#     loadMap()
#     app.char = Character("main", 0, 0, 80,30)


def restart(app):
    app.state = "testing" #intro, build, play
    app.rows = app.cols = 5
    changeMapWidth(app)
    changeMapHeight(app)
    app.map = Map(app.rows, app.cols)
    print(app.map)


#Drawing

def redrawAll(app):
    if app.state == "testing":
        #drawBuildUI(app)
        #drawBuildMap(app)
        drawMap(app)
        drawCharacter(app)
        print(app.char)
    elif app.state == 'intro':
        drawIntro(app)

def drawIntro(app):
    pass

def drawBuildUI(app):
    drawRect(0, 0, app.width, 100, fill='dark')
    pass

def drawBuildMap(app):
    pass

def drawMap(app):
    drawRect(0, 0, app.width, app.height, fill="gray")
    for r in range(app.selectedMap.rows):
        for c in range(app.selectedMap.cols):
            cell = app.selectedMap.getSquareType(r,c)
            if cell == "empty":
                drawRect(40*c, 40*r, 40,40,fill="white", border="black")
            if cell == "block":
                drawRect(40*c, 40*r, 40,40,fill="blue", border="black")

def drawCharacter(app):
    drawRect(app.char.left, app.char.top, app.char.width, app.char.height, fill="red")

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
    map = app.selectedMap

    if "w" in keys:
        if app.char.botCell < map.rows:
            if map.getSquareType(app.char.botCell, app.char.leftCell) == "block" or map.getSquareType(app.char.botCell, app.char.rightCell) == "block":
                app.char.jump()
    if "d" in keys:
        if app.char.rightCell < map.cols:
            # (map.getSquareType(app.char.botCell, app.char.leftCell) == "block" or 
            #     map.getSquareType(app.char.botCell, app.char.rightCell) == "block")
            #     and 
            if (map.getSquareType(app.char.botCell-1, app.char.rightCell) != "block"
                and map.getSquareType(app.char.topCell, app.char.rightCell) != "block"):
                app.char.vy = 10
        elif app.char.rightCell == map.cols:
            app.char.vy = 0
    elif "a" in keys:
        if app.char.leftCell >= 0:
            #(map.getSquareType(app.char.botCell, app.char.leftCell) == "block" or 
                #map.getSquareType(app.char.botCell, app.char.rightCell) == "block")
                #and 
            if (map.getSquareType(app.char.botCell-1, app.char.leftCell) != "block"
                and map.getSquareType(app.char.topCell, app.char.leftCell) != "block"):
                app.char.vy = -10
        elif app.char.leftCell < 0:
            app.char.vy = 0

def onKeyRelease(app, keys):
    if "d" in keys:
        app.char.vy = 0
    if "a" in keys:
        app.char.vy = 0

def main():
    print("blehh")
    runApp()

main()


