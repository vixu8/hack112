import numpy as np
from cmu_graphics import *
from types import SimpleNamespace
import os
import time
import random
from map import *
from character import *
from camera import *

msg = "Roll for initiative:"
print(msg)

print(np.random.randint(1,20))

def onAppStart(app):
    app.stepsPerSecond = 100

    #app.state = "testing" #home. build, play
  
    app.states = ["intro", 'build', 'play', 'load'] #intro, build, play, load

    app.width = 640
    app.height = 400

    app.blockPx = 40
    
    app.g = 10 #gravity, in terms of pixels

    app.maps = [None, None, None, None]
    app.selectedMap = None

    print(app.selectedMap)

    app.char = Character("main", 100, 100, 70,30)
    app.cam = Camera(0, 0, 10*40, 16*40)

    #buttons
    app.buttonLocations = set()
    app.buttonFunctions = {}

    restart(app)

def onStep(app):
    if app.state == "testing":

        physics(app,app.char, app.selectedMap)

        app.char.x += app.char.vx
        app.char.y += app.char.vy
        app.char.updateCoords()
        
        app.cam.center(app.char.x, app.char.y)

def onFloor(app, character, map):
    if map.getSquareType(character.botCell, character.leftCell) == "block" or map.getSquareType(character.botCell, character.rightCell) == "block":
        return True
    return False
        
def physics(app, character, map):
    
    if character.botCell >= map.rows or map.getSquareType(character.botCell, character.leftCell) == "block" or map.getSquareType(character.botCell, character.rightCell) == "block":
        character.vx = 0
        character.x = (character.botCell)*app.blockPx - character.height/2
    else: character.vx += app.g/5
    
    if character.topCell >= 0:
        if map.getSquareType(character.topCell, character.leftCell) == "block" or map.getSquareType(character.topCell, character.rightCell) == "block":
            character.vx = 0
            character.x = (character.topCell+1)*app.blockPx + character.height/2

    if character.vy < 0:
        if character.left+character.vy < 0 or map.getSquareType(character.botCell- (1 if onFloor(app, character, map) else 0), (character.left+character.vy)//40) == "block" or map.getSquareType(character.topCell, (character.left+character.vy)//40) == "block":
            character.vy = 0
            character.y = (character.leftCell)*app.blockPx + character.width/2

    if character.vy >= 0:
        if character.right+character.vy >= app.blockPx*map.cols or map.getSquareType(character.botCell- (1 if onFloor(app, character, map) else 0), (character.right+character.vy)//40) == "block" or map.getSquareType(character.topCell, (character.right+character.vy)//40) == "block":
            character.vy = 0
            character.y = (character.rightCell+1)*app.blockPx - (character.width/2 + 2)
    

# def startPlay(app):
#     loadMap()
#     app.char = Character("main", 0, 0, 80,30)


def restart(app):
    app.state = "testing" #intro, build, play
    loadMap(app)

#Loading
def loadMap(app):
    app.rows = app.cols = 5
    changeMapWidth(app)
    changeMapHeight(app)
    app.selectedMap = Map(app.rows, app.cols)
    print(app.selectedMap)

#End Loading

#Drawing
def redrawAll(app):
    if app.state == "play":
        drawMap(app)
        drawCharacter(app)
    elif app.state == 'intro':
        drawIntro(app)
    elif app.state == 'load':
        drawLoad(app)
    elif app.state == 'build':
        drawBuildUI(app)
        drawBuildMap(app)

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

def drawMap(app):
    drawRect(0, 0, app.width, app.height, fill="gray")
    for r in range(app.selectedMap.rows):
        for c in range(app.selectedMap.cols):
            cell = app.selectedMap.getSquareType(r,c)
            if cell == "empty":
                drawRect(40*c-app.cam.offsetC, 40*r-app.cam.offsetR, 40,40,fill="white", border="black")
            if cell == "block":
                drawRect(40*c-app.cam.offsetC, 40*r-app.cam.offsetR, 40,40,fill="blue", border="black")

def drawCharacter(app):
    drawRect(app.char.left-app.cam.offsetC, app.char.top-app.cam.offsetR, app.char.width, app.char.height, fill="red")

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

def changeMapHeight(app):
    height = app.getTextInput('Enter the height of the map: ')
    isInt = height.isdigit()
    if not isInt:
        app.showMessage('Please enter an integer!')
        changeMapHeight(app)
        return
    height = int(height)
    moreThan5 = height >= 10
    if not moreThan5:
        app.showMessage('Please enter a number greater than 9!')
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
    moreThan5 = width >= 10
    if not moreThan5:
        app.showMessage('Please enter a number greater than 9!')
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
    
    if "p" in keys:
        print(map)

def onKeyRelease(app, keys):
    if "d" in keys:
        app.char.vy = 0
    if "a" in keys:
        app.char.vy = 0

def onMousePress(app, mouseX, mouseY):
    #check buttons
    if app.state == "testing":
        cellR = mouseY//40
        cellC = mouseX//40
        app.selectedMap.setBlock(cellR, cellC, 1)


    for location in app.buttonLocations:
        isBetweenX = location[0][0] <= mouseX <= location[1][0]
        isBetweenY = location[0][1] <= mouseY <= location[1][1]
        if (isBetweenX) and (isBetweenY):
            app.buttonFunctions[location](app)

def main():
    print("blehh")
    runApp()

main()


