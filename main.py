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
    
    app.selectedMap = None

    #buttons
    app.buttonLocations = set()
    app.buttonFunctions = {}

    restart(app)

def restart(app):
    app.state = "intro" #intro, build, play
    app.buildNum = 0

#Loading
def loadMap(app):
    app.rows = app.cols = 10
    changeMapWidth(app)
    changeMapHeight(app)
    app.map = Map(app.rows, app.cols)
    app.state = 'build'
    print(app.map)

def loadBuildOne(app):
    f = open('build1.txt', 'r')
    isEmpty = f.read() == ''
    f.close()
    if isEmpty:
        loadMap(app)
        return
    f = open('build1.txt', 'r')
    readMap = f.read()
    app.map = parseMap(readMap)
    app.state = 'intro'
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
    app.map = parseMap(readMap)
    app.state = 'intro'
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
    app.map = parseMap(readMap)
    app.state = 'intro'
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
    app.map = parseMap(readMap)
    app.state = 'intro'
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
    newButton(app, 0, 0, 130+saveButtonSize+50, 50+saveButtonSize, clickMenu, 'build')

def drawLoad(app):
    drawRect(0, 0, app.width, app.height, fill='darkblue', opacity=70)
    drawLabel('Pick a map to load', app.width/2, app.height/4, bold=True, size=100, font='arial', fill='white', opacity=50)
    
    #Buttons to load in builds
    buttonWidth = 150
    gap = 200/3
    build1Empty = build2Empty = build3Empty = build4Empty = True
    empty = {1:build2Empty, 2:build3Empty, 3:build4Empty}
    build1 = open('build1.txt', 'r')
    if build1.read() != '':
        build1Empty = False
    build2 = open('build2.txt', 'r')
    if build2.read() != '':
        build2Empty = False
    build3 = open('build3.txt', 'r')
    if build3.read() != '':
        build3Empty = False
    build4 = open('build4.txt', 'r')
    if build4.read() != '':
        build4Empty = False

    for i in range(0, 4): #left two buttons
        loads = {1:loadBuildTwo, 2:loadBuildThree, 3:loadBuildFour}
        if i == 0:
            drawRect(150+i*buttonWidth, app.height/2, buttonWidth, 200, fill='midnightblue')
            newButton(app, 150+i*buttonWidth, app.height/2, 150+i*buttonWidth+buttonWidth, app.height/2+200, loadBuildOne, 'load')
            if build1Empty: drawLabel('Empty Build 1', 150+i*buttonWidth + 1/2*buttonWidth, app.height/2+100)
            else: drawLabel('Build 1', 150+i*buttonWidth + 1/2*buttonWidth, app.height/2+100)
        else:
            drawRect(150+i*buttonWidth+gap*i, app.height/2, buttonWidth, 200, fill='midnightblue')
            newButton(app, 150+i*buttonWidth+gap*i, app.height/2, 150+i*buttonWidth+buttonWidth+gap*i, app.height/2+200, loads[i], 'load')
            if empty[i]: drawLabel(f'Empty Build {i+1}', 150+i*buttonWidth+gap*i + buttonWidth/2, app.height/2+100)
            else: drawLabel(f'Build {i+1}', 150+i*buttonWidth+gap*i + buttonWidth/2, app.height/2+100)


def drawBuildMap(app):
    pass

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
        app.showMessage('Please enter a number greater than 10!')
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
        app.showMessage('Please enter a number greater than 10!')
        changeMapWidth(app)
        return
    app.cols = width

def parseMap(map):
    pass

def onStep(app):
    pass

def posToCell():
    pass

def onKeyPress(app, keys):
    if 'escape' in keys and app.state == 'load': app.state = 'intro'
    if 'escape' in keys and app.state == 'build': app.state = 'intro'


def onMousePress(app, mouseX, mouseY):
    #check buttons
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


