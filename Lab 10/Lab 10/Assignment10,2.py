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

attempts = 0
while grid.queens < 8:
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    attempts += 1
    if grid.is_valid(x, y):
        grid.update(x, y)
        print(f"Queen {grid.queens} placed at : ({x+1}, {y+1})")
        grid.display()
        attempts = 0 
    if attempts > 1000:
        print("Too much time taken finding a valid position\n")
        break
if grid.queens == 8:
    print("\nAll queens successfully placed!")
else:
    print("Can't place all queens!")
