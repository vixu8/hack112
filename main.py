from cmu_graphics import *
from map import *
from character import *
from camera import *

def onAppStart(app):
    app.stepsPerSecond = 100
    app.setMaxShapeCount(5000)

    #app.state = "testing" #home. build, play
  
    app.states = ["intro", 'build', 'play', 'load'] #intro, build, play, load

    app.width = 1100 #640
    app.height = 700 #400

    app.blockPx = 40

    app.selectedBlock = 0 #0 for air, 1 for wall, 2 for death, 3 spawn, 4 finish
    
    app.g = 10 #gravity, in terms of pixels
    app.deaths = 0

    app.selectedMap = None

    app.blockType = 0
    app.spawnPoint = None
    app.cellSize = None

    app.won = False

    print(app.selectedMap)

    
    #buttons
    app.buttonLocations = set()
    app.buttonFunctions = {}

    restart(app)

def onStep(app):
    print(app.state)

    if app.state == 'build' and app.selectedMap == None: loadMap(app)

    elif app.state == "play" and app.won == False:

        physics(app,app.char, app.selectedMap)
        die(app, app.char, app.selectedMap)
        win(app, app.char, app.selectedMap)

        app.char.x += app.char.vx
        app.char.y += app.char.vy
        app.char.updateCoords()
        
        app.cam.center(app.char.x, app.char.y)

def onFloor(app, character, map):
    if map.getSquareType(character.botCell, character.leftCell) == "block" or map.getSquareType(character.botCell, character.rightCell) == "block":
        return True
    return False

def die(app, character, map):
    if ((character.botCell < map.rows and map.getSquareType(character.botCell, character.leftCell) == "death"
         or map.getSquareType(character.botCell, character.rightCell) == "death") or
        (character.topCell >= 0 and map.getSquareType(character.topCell, character.leftCell) == "death"
          or map.getSquareType(character.topCell, character.rightCell) == "death")):
        print("DIEEE")
        app.deaths += 1
        character.goSpawn()

def win(app, character, map):
    if ((character.botCell < map.rows and map.getSquareType(character.botCell, character.leftCell) == "end"
         or map.getSquareType(character.botCell, character.rightCell) == "end") or
        (character.topCell >= 0 and map.getSquareType(character.topCell, character.leftCell) == "end"
          or map.getSquareType(character.topCell, character.rightCell) == "end")):
        print("won")
        app.won=True

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
    charLocation = findSpawn(app)
    print(charLocation, "SAWNB")
    app.cam = Camera(0, 0, app.width, app.height)
    app.won = False
    if charLocation != None:
        charR, charC = charLocation
        # charx = (charLocation[1]+1)*app.cellSize
        # chary = (charLocation[0]-10+1)*app.cellSize
        app.char = Character("main", (charR-1)*app.blockPx, app.blockPx*charC + 15, 70,30)
        print(app.char)
        print("cell size", app.cellSize)
    else:
        app.char = Character("main", 0, 0, 70,30)
    


def restart(app):
    app.state = "intro" #intro, build, play

#Loading
def loadMap(app):
    app.rows = app.cols = 10
    val1 = changeMapWidth(app)
    val2 = changeMapHeight(app)
    if val1 == None and val2 == None:
        app.selectedMap = Map(app.rows, app.cols)
        app.spawnPoint = findSpawn(app)

        app.cellSize = min((app.width-200)/(app.selectedMap.cols), (app.height-100)/(app.selectedMap.rows))
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
    print(f.read(), '', isEmpty)
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
    map = app.selectedMap.getMap()
    write = f'{map}'
    f.write(write)
    f.close()
def saveBuildTwo(app):
    f = open('build2.txt', 'w')
    map = app.selectedMap.getMap()
    write = f'{map}'
    print(write)
    f.write(write)
    f.close()
def saveBuildThree(app):
    f = open('build3.txt', 'w')
    map = app.selectedMap.getMap()
    write = f'{map}'
    f.write(write)
    f.close()
def saveBuildFour(app):
    f = open('build4.txt', 'w')
    map = app.selectedMap.getMap()
    write = f'{map}'
    f.write(write)
    f.close()

#Drawing
def redrawAll(app):
    if app.state == "play":

        drawMap(app)
        drawCharacter(app)
        if app.won:
            drawLabel("good job", 100,100, size=50, fill="green")
            drawLabel("p to go again", 100, 200, size=30, fill="purple")
        drawLabel(f"Deaths: {app.deaths}", 800, 100, fill="red", size=30)

    elif app.state == 'intro':
        drawIntro(app)
    elif app.state == 'load':
        drawLoad(app)
    elif app.state == 'build':
        drawBuildMap(app)
        drawBuildUI(app)

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

    #Air button
    airButtonSize = 100
    drawRect(1000-airButtonSize/2, 100-airButtonSize/2, airButtonSize, airButtonSize, fill='white')
    drawLabel('Air', 1000, 100, size=32, fill='black', opacity=50)
    newButton(app, 1000-airButtonSize/2, 100-airButtonSize/2, 1000-airButtonSize/2 + airButtonSize, 100-airButtonSize/2 + airButtonSize, clickAir, 'build')

    #Wall button
    wallButtonSize = 100
    drawRect(1000-wallButtonSize/2, 233-wallButtonSize/2, wallButtonSize, wallButtonSize, fill='blue')
    drawLabel('Wall', 1000, 233, size=32, fill='white', opacity=50)
    newButton(app, 1000-wallButtonSize/2, 233-wallButtonSize/2, 1000-wallButtonSize/2 + wallButtonSize, 233-wallButtonSize/2 + wallButtonSize, clickWall, 'build')

    #Death button
    airButtonSize = 100
    drawRect(1000-airButtonSize/2, 366-airButtonSize/2, airButtonSize, airButtonSize, fill='red')
    drawLabel('Death', 1000, 366, size=32, fill='black', opacity=50)
    newButton(app, 1000-airButtonSize/2, 366-airButtonSize/2, 1000-airButtonSize/2 + airButtonSize, 366-airButtonSize/2 + airButtonSize, clickDeath, 'build')

    #Spawn button
    airButtonSize = 100
    drawRect(1000-airButtonSize/2, 500-airButtonSize/2, airButtonSize, airButtonSize, fill='green')
    if app.spawnPoint == None: 
        drawLabel('Spawn', 1000, 500, size=32, fill='black', opacity=50)
        newButton(app, 1000-airButtonSize/2, 500-airButtonSize/2, 1000-airButtonSize/2 + airButtonSize, 500-airButtonSize/2 + airButtonSize, clickSpawn, 'build')
    else:
        drawLabel('Spawn Placed', 1000, 500, size=32, fill='black', opacity=50)

    
    #End button
    airButtonSize = 100
    drawRect(1000-airButtonSize/2, 633-airButtonSize/2, airButtonSize, airButtonSize, fill='yellow')
    drawLabel('End', 1000, 633, size=32, fill='black', opacity=50)
    newButton(app, 1000-airButtonSize/2, 633-airButtonSize/2, 1000-airButtonSize/2 + airButtonSize, 633-airButtonSize/2 + airButtonSize, clickEnd, 'build')

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
                elif cell == "block":
                    drawRect(app.cellSize*c, app.cellSize*r + 100, app.cellSize,app.cellSize,fill="blue", border="black")
                elif cell == 'death':
                    drawRect(app.cellSize*c, app.cellSize*r + 100, app.cellSize,app.cellSize,fill="red", border="black")
                elif cell == 'spawn':
                    drawRect(app.cellSize*c, app.cellSize*r + 100, app.cellSize,app.cellSize,fill="green", border="black")
                elif cell == 'end':
                    drawRect(app.cellSize*c, app.cellSize*r + 100, app.cellSize,app.cellSize,fill="yellow", border="black")
    pass



def drawMap(app):
    if app.selectedMap == None:
        return
    drawRect(0, 0, app.width, app.height, fill="gray")
    for r in range(app.selectedMap.rows):
        for c in range(app.selectedMap.cols):
            cell = app.selectedMap.getSquareType(r,c)
            if cell == "empty":
                drawRect(40*c-app.cam.offsetC, 40*r-app.cam.offsetR, 40,40,fill="white")
            elif cell == "block":
                drawRect(40*c-app.cam.offsetC, 40*r-app.cam.offsetR, 40,40,fill="blue")
            elif cell == 'death':
                drawRect(40*c-app.cam.offsetC, 40*r-app.cam.offsetR, 40,40,fill="red")
            elif cell == 'spawn':
                drawRect(40*c-app.cam.offsetC, 40*r-app.cam.offsetR, 40,40,fill="green")
            elif cell == 'end':
                drawRect(40*c-app.cam.offsetC, 40*r-app.cam.offsetR, 40,40,fill="yellow")

def drawCharacter(app):
    drawRect(app.char.left-app.cam.offsetC, app.char.top-app.cam.offsetR, app.char.width, app.char.height, fill="purple")

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
def clickAir(app): 
    app.selectedBlock = 0
    print(app.selectedBlock)
def clickWall(app): app.selectedBlock = 1
def clickDeath(app): app.selectedBlock = 2
def clickSpawn(app): 
    if app.spawnPoint == None:
        app.selectedBlock = 3
def clickEnd(app): app.selectedBlock = 4
def clickSaveBuild(app):
    saveBuilds = {1:saveBuildOne, 2:saveBuildTwo, 3:saveBuildThree, 4:saveBuildFour}
    buildNumber = app.getTextInput('Enter the number (integer) of the build you want to save to: ')
    isInt = buildNumber.isdigit()
    if buildNumber == '': return
    if not isInt:
        app.showMessage('Please enter an integer!')
        clickSaveBuild(app)
        return
    buildNumber = int(buildNumber)
    if 0 >= buildNumber >= 5:
        app.showMessage('Please enter an integer between 1 and 4!')
        clickSaveBuild(app)
        return
    saveBuilds[buildNumber](app)

#End Button Functions

def changeMapHeight(app):
    height = app.getTextInput('Enter the height of the map: ')
    isInt = height.isdigit()
    if height == '':
        return 'hi'
    if not isInt:
        app.showMessage('Please enter an integer!')
        changeMapHeight(app)
        return None
    height = int(height)
    moreThan5 = height >= 10
    if not moreThan5:
        app.showMessage('Please enter a number greater than 9!')
        changeMapHeight(app)
        return None
    app.rows = height
def changeMapWidth(app):
    width = app.getTextInput('Enter the width of the map: ')
    isInt = width.isdigit()
    if width == '':
        return 'hi'
    if not isInt:
        app.showMessage('Please enter an integer!')
        changeMapWidth(app)
        return None
    width = int(width)
    moreThan5 = width >= 10
    if not moreThan5:
        app.showMessage('Please enter a number greater than 9!')
        changeMapWidth(app)
        return None
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
    elif 'p' in keys and app.state == 'build': 
        startPlay(app)
        app.state = "play"
        app.won = False
        app.deaths = 0

    if app.state == "play":
        if 'p' in keys:
            startPlay(app)
            app.won = False
            app.deaths = 0


        if 'escape' in keys:
            app.state = 'intro'
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
    if app.state == "play":
        if "d" in keys:
            app.char.vy = 0
        if "a" in keys:
            app.char.vy = 0

def onMouseDrag(app, mouseX, mouseY):
    if app.state == "build":
        if app.height > mouseY > 100 and 0 < mouseX < app.width-200:
            cellR = (mouseY-100)//app.cellSize
            cellC = (mouseX)//app.cellSize
            app.selectedMap.setBlock(cellR, cellC, app.selectedBlock)
            print("clicked blokc", cellR, cellC)

def onMousePress(app, mouseX, mouseY):
    #check buttons
    if app.state == "build":
        if app.height > mouseY > 100 and 0 < mouseX < app.width-200:
            cellR = (mouseY-100)//app.cellSize
            cellC = (mouseX)//app.cellSize
            app.selectedMap.setBlock(cellR, cellC, app.selectedBlock)
            print("clicked blokc", cellR, cellC)

    for location in app.buttonLocations:
        isBetweenX = location[0][0] <= mouseX <= location[1][0]
        isBetweenY = location[0][1] <= mouseY <= location[1][1]
        isState = app.state == location[2]
        if (isBetweenX) and (isBetweenY) and (isState):
            app.buttonFunctions[location](app)

def findSpawn(app):
    if app.selectedMap != None:
        map = app.selectedMap.getMap()
        rows, cols = len(map), len(map[0])
        for row in range(rows):
            for col in range(cols):
                if map[row][col] == 3:
                    return (row-10, col)
    return None

def main():
    print("blehh")
    runApp()

main()


