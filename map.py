import copy
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
        if 0<= int(row)+10 < len(self.map) and 0<= int(col) < len(self.map[0]):
            self.map[int(row)+10][int(col)] = block
    
    def getMap(self):
        return self.map
    
    def transfer(self, array):
        self.rows = len(array)-10
        self.cols = len(array[0])

        self.map = copy.deepcopy(array)
        # self.map = [[0 for i in range(self.cols)] for j in range(len(array))]
        # for r in range(len(array)):
        #     for c in range(len(array[0])):
        #         self.map[r][c] = array[r][c]
