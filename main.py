import numpy as np
from cmu_graphics import *
from types import SimpleNamespace
import os
import time
import random

msg = "Roll for initiative:"
print(msg)

print(np.random.randint(1,20))

def onAppStart(app):
    restart(app)

def restart(app):
    app.row, app.col = 5

def changeMapHeight(app):
    height = app.getTextInput('Enter the height of the map: ')
    isInt = isinstance(height, int)
    if not isInt:
        app.showMessage('Please enter an integer!')
        changeMapHeight(app)
        return
    height = int(height)
    moreThan5 = height >= 5
    elif not moreThan5:
        app.showMessage('Please enter a number greater than 5!')
        changeMapHeight(app)
        return
    app.row = height

def changeMapWidth(app):
    width = app.getTextInput('Enter the width of the map: ')
    isInt = isinstance(width, int)
    if not isInt:
        app.showMessage('Please enter an integer!')
        changeMapWidth(app)
        return
    width = int(width)
    moreThan5 = width >= 5
    elif not moreThan5:
        app.showMessage('Please enter a number greater than 5!')
        changeMapWidth(app)
        return
    app.row = width


def redrawAll(app):
    pass

def onKeyPress(app, keys):
    pass

def main():
    print("blehh")
    runApp()

main()


