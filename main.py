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
    app.row, app.col = 0

def promptUser(app):
    

def redrawAll(app):
    pass

def onKeyPress(app, keys):
    pass

def main():
    print("blehh")
    runApp()

main()


