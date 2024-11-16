class Map:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.map = [[0 for i in range(cols)] for j in range(rows+10)] #10 extra hidden rows on top
        self.map[rows+9] = [1 for i in range(cols)]
        self.map[rows+8] = [1 for i in range(cols)]
    
    def getSquareType(self, row, col): #gets the type of block that coord is
        value = self.map[int(row)+10][int(col)]
        match value:
            case 0:
                return "empty"
            case 1: 
                return "block"
            case 2:
                return "death"
            case 3:
                return "spawn"
            case 4:
                return "end"
    
    def __repr__(self):
        res = "Map\n"
        for row in self.map:
            res += str(row)+"\n"
        return res
    
    def setBlock(self, row, col, block):
        self.map[row+10][col] = block