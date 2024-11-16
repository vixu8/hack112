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
    restart(app)

def restart(app):
    app.rows = app.cols = 5
    changeMapWidth(app)
    changeMapHeight(app)
    app.map = Map(app.rows, app.cols)
    print(app.map)

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


def redrawAll(app):
    pass

def onKeyPress(app, keys):
    pass

def main():
    print("blehh")
    runApp()

main()


