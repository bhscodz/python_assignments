import random
import numpy as np
class Grid:
    def __init__(self):
        self.grid = np.zeros((8, 8))
        self.queens = 0
    
    def display(self):
        print(self.grid.astype(int))
        print()

    def update(self, x, y):
        if self.grid[x][y] != -1:
            for i in range(8):
                self.grid[i][y] = -1
                self.grid[x][i] = -1
                if 0 <= x-i < 8 and 0 <= y-i < 8:
                    self.grid[x-i][y-i] = -1
                if 0 <= x-i < 8 and 0 <= y+i < 8:
                    self.grid[x-i][y+i] = -1
                if 0 <= x+i < 8 and 0 <= y+i < 8:
                    self.grid[x+i][y+i] = -1
                if 0 <= x+i < 8 and 0 <= y-i < 8:
                    self.grid[x+i][y-i] = -1
            self.grid[x][y] = 1
            self.queens += 1
              
    def is_valid(self, x, y):
        return self.grid[x][y] == 0
    
grid = Grid()