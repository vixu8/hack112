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

    app.width = 1100 #640
    app.height = 700 #400

    app.blockPx = 40
    
    app.map = None

    app.g = 10 #gravity, in terms of pixels

    app.maps = [None, None, None, None]
    app.selectedMap = None

    app.blockType = 0
    app.cellSize = None


    print(app.selectedMap)

    
    #buttons
    app.buttonLocations = set()
    app.buttonFunctions = {}

    restart(app)

def onStep(app):
    if app.state == 'build' and app.map == None: loadMap(app)

    elif app.state == "play":

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
    

def startPlay(app):
    app.char = Character("main", 0, 0, 80,30)
    app.cam = Camera(0, 0, app.width, app.height)


def restart(app):
    app.state = "intro" #intro, build, play

#Loading
def loadMap(app):
    app.rows = app.cols = 10
    changeMapWidth(app)
    changeMapHeight(app)

    app.map = Map(app.rows, app.cols)
    app.state = 'build'

def loadBuildOne(app):
    f = open('build1.txt', 'r')
    isEmpty = f.read() == ''
    f.close()
    if isEmpty:
        loadMap(app)
        return
    f = open('build1.txt', 'r')
    readMap = f.read()
    temp = parseMap(readMap)
    app.selectedMap = Map(len(temp), len(temp[0]))
    app.selectedMap.transfer(temp)
    app.cellSize = min((app.width-200)/(app.selectedMap.cols), (app.height-100)/(app.selectedMap.rows))
    app.state = 'build'
    f.close()
    return
def loadBuildTwo(app):
    f = open('build2.txt', 'r')
    isEmpty = f.read() == ''
    f.close()
    if isEmpty:
        loadMap(app)
        return
    f = open('build2.txt', 'r')
    readMap = f.read()
    temp = parseMap(readMap)
    app.selectedMap = Map(len(temp), len(temp[0]))
    app.selectedMap.transfer(temp)
    app.cellSize = min((app.width-200)/(app.selectedMap.cols), (app.height-100)/(app.selectedMap.rows))
    app.state = 'build'
    f.close()
    return
def loadBuildThree(app):
    f = open('build3.txt', 'r')
    isEmpty = f.read() == ''
    f.close()
    if isEmpty:
        loadMap(app)
        return
    f = open('build3.txt', 'r')
    readMap = f.read()
    temp = parseMap(readMap)
    app.selectedMap = Map(len(temp), len(temp[0]))
    app.selectedMap.transfer(temp)
    app.cellSize = min((app.width-200)/(app.selectedMap.cols), (app.height-100)/(app.selectedMap.rows))
    app.state = 'build'
    f.close()
    return
def loadBuildFour(app):
    f = open('build4.txt', 'r')
    isEmpty = f.read() == ''
    f.close()
    if isEmpty:
        loadMap(app)
        return
    f = open('build4.txt', 'r')
    readMap = f.read()
    temp = parseMap(readMap)
    app.selectedMap = Map(len(temp), len(temp[0]))
    app.selectedMap.transfer(temp)
    app.cellSize = min((app.width-200)/(app.selectedMap.cols), (app.height-100)/(app.selectedMap.rows))
    app.state = 'build'
    f.close()
    return

#End Loading

#Saving
def saveBuildOne(app):
    f = open('build1.txt', 'w')
    map = app.map.getMap()
    write = f'{map}'
    f.write(write)
    f.close()
def saveBuildTwo(app):
    f = open('build2.txt', 'w')
    map = app.map.getMap()
    write = f'{map}'
    print(write)
    f.write(write)
    f.close()
def saveBuildThree(app):
    f = open('build3.txt', 'w')
    map = app.map.getMap()
    write = f'{map}'
    f.write(write)
    f.close()
def saveBuildFour(app):
    f = open('build4.txt', 'w')
    map = app.map.getMap()
    write = f'{map}'
    f.write(write)
    f.close()

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
    newButton(app, app.width/2-editButtonSize/2-150, app.height/2-editButtonSize/2, app.width/2-editButtonSize/2-150+editButtonSize+300, app.height/2+editButtonSize/2, clickEditBuild, 'intro')
    
    #Load Button
    loadButtonSize = 80
    drawRect(app.width/2-loadButtonSize/2-150, app.height/2-loadButtonSize/2 + 100, loadButtonSize+300, loadButtonSize, fill='midnightblue', opacity=80, border='black', borderWidth=5)
    drawLabel('Load Build', app.width/2, app.height/2 + 100, size=loadButtonSize, fill='white', opacity=50)
    newButton(app, app.width/2-loadButtonSize/2-150, app.height/2-loadButtonSize/2 + 100, app.width/2-loadButtonSize/2-150+loadButtonSize+300, app.height/2+loadButtonSize/2 + 100, clickLoadBuild, 'intro')

def drawBuildUI(app):
    #Menus
    topMenuWidth = app.width-200
    borderWidth = 5
    drawRect(0, 0, topMenuWidth + borderWidth, 100, fill='darkblue', opacity=70, border='black', borderWidth=borderWidth) #top menu
    drawRect(topMenuWidth, 0, 200, 700, fill='darkblue', opacity=70, border='black', borderWidth=borderWidth) #side bar
    
    #Menu Button
    menuButtonSize = 100
    drawLabel('MENU', 150, 50, size=menuButtonSize, fill='white', opacity=50)
    newButton(app, 0, 0, 130+menuButtonSize+50, 50+menuButtonSize, clickMenu, 'build')

    #Save Button
    saveButtonSize = 100
    drawLabel('SAVE', 450, 50, size=saveButtonSize, fill='white', opacity=50)
    newButton(app, 450-saveButtonSize/2, 0, 450+saveButtonSize+50, 50+saveButtonSize, clickSaveBuild, 'build')

def drawLoad(app):
    drawRect(0, 0, app.width, app.height, fill='darkblue', opacity=70)
    drawLabel('Pick a map to load', app.width/2, app.height/4, bold=True, size=100, font='arial', fill='white', opacity=50)
    
    #Buttons to load in builds
    buttonWidth = 150
    gap = 200/3
    build1Empty = build2Empty = build3Empty = build4Empty = False
    
    build1 = open('build1.txt', 'r')
    if build1.read() == '':
        build1Empty = True
    build1.close()
    build2 = open('build2.txt', 'r')
    if build2.read() == '':
        build2Empty = True
    build2.close()
    build3 = open('build3.txt', 'r')
    if build3.read() == '':
        build3Empty = True
    build3.close()
    build4 = open('build4.txt', 'r')
    if build4.read() == '':
        build4Empty = True
    build4.close()
    empty = {1:build2Empty, 2:build3Empty, 3:build4Empty}

    for i in range(0, 4): #left two buttons
        loads = {1:loadBuildTwo, 2:loadBuildThree, 3:loadBuildFour}
        if i == 0:
            drawRect(150+i*buttonWidth, app.height/2, buttonWidth, 200, fill='midnightblue')
            newButton(app, 150+i*buttonWidth, app.height/2, 150+i*buttonWidth+buttonWidth, app.height/2+200, loadBuildOne, 'load')
            if build1Empty: drawLabel('Empty Build 1', 150+i*buttonWidth + 1/2*buttonWidth, app.height/2+100, fill='white', size=16)
            else: drawLabel('Build 1', 150+i*buttonWidth + 1/2*buttonWidth, app.height/2+100, fill='white', size=16)
        else:
            print(i, empty[i])
            drawRect(150+i*buttonWidth+gap*i, app.height/2, buttonWidth, 200, fill='midnightblue')
            newButton(app, 150+i*buttonWidth+gap*i, app.height/2, 150+i*buttonWidth+buttonWidth+gap*i, app.height/2+200, loads[i], 'load')
            if empty[i]: drawLabel(f'Empty Build {i+1}', 150+i*buttonWidth+gap*i + buttonWidth/2, app.height/2+100, fill='white', size=16)
            else: drawLabel(f'Build {i+1}', 150+i*buttonWidth+gap*i + buttonWidth/2, app.height/2+100, fill='white', size=16)


def drawBuildMap(app):
    if app.selectedMap == None:
        return
    drawRect(0,100,app.width-200,app.height-100, fill="gray")

    for r in range(app.selectedMap.rows):
            for c in range(app.selectedMap.cols):
                cell = app.selectedMap.getSquareType(r,c)
                if cell == "empty":
                    drawRect(app.cellSize*c, app.cellSize*r + 100, app.cellSize,app.cellSize,fill="white", border="black")
                if cell == "block":
                    drawRect(app.cellSize*c, app.cellSize*r + 100, app.cellSize,app.cellSize,fill="blue", border="black")
                


    pass

def drawMap(app):
    if app.selectedMap == None:
        return
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
def newButton(app, toplx, toply, botrx, botry, func, state):
    topLeft = (toplx, toply)
    botRight = (botrx, botry)
    location = (topLeft, botRight, state)
    app.buttonLocations.add(location)
    app.buttonFunctions[location] = func

def clickMenu(app): app.state = 'intro'
def clickEditBuild(app): app.state = 'build'
def clickLoadBuild(app): app.state = 'load'
def clickSaveBuild(app):
    saveBuilds = {1:saveBuildOne, 2:saveBuildTwo, 3:saveBuildThree, 4:saveBuildFour}
    buildNumber = app.getTextInput('Enter the number (integer) of the build you want to save to: ')
    isInt = buildNumber.isdigit()
    if buildNumber == '': return
    if not isInt:
        app.showMessage('Please enter an integer!')
        changeMapHeight(app)
        return
    buildNumber = int(buildNumber)
    if 0 >= buildNumber >= 5:
        app.showMessage('Please enter an integer between 1 and 4!')
        changeMapHeight(app)
        return
    saveBuilds[buildNumber](app)

#End Button Functions

def changeMapHeight(app):
    height = app.getTextInput('Enter the height of the map: ')
    isInt = height.isdigit()
    if height == '':
        return
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
    if width == '':
        return
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

def parseMap(map):
    returnMap = []
    map = map.strip('[[')
    map = map.strip(']]')
    listComas = map.split('], [')
    for comad in listComas:
        addList = []
        for c in comad:
            if c.isdigit():
                addList.append(int(c))
        returnMap.append(addList)
    return returnMap
   
def onKeyPress(app, keys):
    if 'escape' in keys and app.state == 'load': app.state = 'intro'
    if 'escape' in keys and app.state == 'build': app.state = 'intro'
    elif 'p' in keys and app.state == 'build': app.state = "play"
     
    if app.state == "play":
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
    if app.state == "build":
        if mouseY >= 100:
            cellR = (mouseY-100)//app.cellSize
        if mouseX <= 800:
            cellC = (mouseX-100)//app.cellSize
        app.selectedMap.setBlock(cellR, cellC, app.blockType)


    for location in app.buttonLocations:
        isBetweenX = location[0][0] <= mouseX <= location[1][0]
        isBetweenY = location[0][1] <= mouseY <= location[1][1]
        isState = app.state == location[2]
        if (isBetweenX) and (isBetweenY) and (isState):
            app.buttonFunctions[location](app)

def main():
    print("blehh")
    runApp()

main()


