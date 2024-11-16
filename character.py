class Charcter:
    def __init__(self, kind, initx, inity, height, width):
        self.type = kind
        self.x = initx
        self.y = inity
        self.height = height
        self.width = width
        self.vx = 0
        self.vy = 0
        self.top = self.x + height/2
        self.bot = self.x - height/2
        self.left = self.y - width/2
        self.right = self.y + width/2
    
    def __repr__(self):
        return f'{self.type.title()}(x: {self.x}, y: {self.y}, moving: {(self.vx, self.vy)})'

    def setPosition(self, x, y):
        if isinstance(x, float) and isinstance(y, float):
            self.x = x
            self.y = y
    
    def getPosition(self):
        return self.x, self.y
    
    def getVelocity(self):
        return self.vx, self.vy
    
    def physics(self, map):
        pass
