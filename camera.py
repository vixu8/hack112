class Camera:
    def __init__(self, topR, leftC, width, height):
        self.top = topR
        self.bot = topR + height
        self.left = leftC
        self.right = leftC + width

        self.width = width
        self.height = height

        self.offsetR = self.height//2 + self.top
        self.offsetC = self.width//2 + self.left
    
    def center(self, centerR, centerC):
        self.top = centerR - self.height//2
        self.bottom = centerR + self.height//2
        self.left = centerC - self.width//2
        self.right = centerC + self.width//2
        self.offsetR = self.top + self.height//8
        self.offsetC = self.left + self.width//8