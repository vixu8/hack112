class Character:

    blockPx = 40

    def __init__(self, kind, initx, inity, height, width):
        self.type = kind
        self.x = initx
        self.y = inity

        self.spawnx = initx
        self.spawny = inity


        self.height = height
        self.width = width
        self.vx = 0
        self.vy = 0
        self.top = self.x - height/2
        self.bot = self.x + height/2
        self.left = self.y - width/2
        self.right = self.y + width/2

        self.topCell = self.top //40
        self.botCell = self.bot//40
        self.leftCell = self.left//40
        self.rightCell = self.right//40
    
    def __repr__(self):
        return f'{self.type.title()}(x: {self.x}, y: {self.y}, moving: {(self.vx, self.vy)})'

    def updateCoords(self):
        self.top = self.x - self.height/2
        self.bot = self.x + self.height/2
        self.left = self.y - self.width/2
        self.right = self.y + self.width/2

        self.topCell = self.top //40
        self.botCell = self.bot//40
        self.leftCell = self.left//40
        self.rightCell = self.right//40

    def setPosition(self, x, y):
        self.x = x
        self.y = y
    
    def goSpawn( self):
        self.setPosition(self.spawnx, self.spawny)

    def getPosition(self):
        return (self.x, self.y)
    
    def getVelocity(self):
        return (self.vx, self.vy)
    
    def jump(self):
        self.vx = -25
        self.x -= 10
        self.updateCoords()