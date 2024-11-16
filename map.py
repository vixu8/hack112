class Map:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.map = [[0 for i in range(cols)] for j in range(rows)]
        self.map[rows-1] = [1 for i in range(cols)]
        self.map[rows-2] = [1 for i in range(cols)]
    
    def getSquareType(self, row, col): #gets the type of block that coord is
        value = self.map[int(row)][int(col)]
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
        self.map[row][col] = block
    
    def getMap(self):
        return self.map