#!/usr/bin/env python3
# 

class color: 
   BLACK  = '\33[30m'
   RED    = '\33[31m'
   GREEN  = '\33[32m'
   YELLOW = '\33[33m'
   BLUE   = '\33[34m'
   VIOLET = '\33[35m'
   BEIGE  = '\33[36m'
   WHITE  = '\33[37m'
   END = '\033[0m'

class sudokuClass: 
    _sudokuMatrix = [0] * 81 # Create Sudoku Matrix
    _grid = [[0 for x in range(9)] for y in range(9)]

    # NumState
    # 0 - Unknown State (RED)
    # 1 - Fixed Number (WHITE)
    # 2 - Unconflicted Number (GREEN)
    # 3 ..  - Conflicted Number (YELLOW)

    _numState = [[0 for x in range(9)] for y in range(9)]


    # Number of conflicts across the board
    _boardConf = [[0 for x in range(9)] for y in range(9)]

    # Number of conflicts across the square
    _squareConf = [[0 for x in range(9)] for y in range(9)]


    def __init__(self,matrix):
       print("DEBUG: sudoku class constructor called") ##
       ## print('DEBUG: matrix is (', matrix,')') ##

       self._sudokuMatrix = matrix.copy()
       self.reset_matrix() # sets Grids
    # end of constructor

    def reset_matrix(self): 
       print("DEBUG: sudoku reset_matrix method called") ##
       
       # Initialize Arrays
       for x in range(9):
          for y in range(9):
             self._grid[x][y] = self._sudokuMatrix[x*9+y] % 10
             self._numState[x][y] = self._sudokuMatrix[x*9+y] // 10
             self._boardConf[x][y] = 0
             self._squareConf[x][y] = 0
    # end of reset_martix method

    def export_matrix(self):

       print("DEBUG: sudoku export_matrix method called") ##

       # export grids
       for x in range(9):
          for y in range(9):
             print(self._grid[x][y] + self._numState[x][y] * 10)
    # end of export_martix method

    def display_matrix(self):
       print("DEBUG: sudoku display_matrix method called") ##

       for x in range(9):
          for y in range(9):
             if y == 3 or y == 6:
                print("|",end='')
             if self._grid[x][y] == 0:
                print("   ",end='')
             else:
                if self._numState[x][y] == 0: print(color.RED,end='')  # Set Color
                elif self._numState[x][y] == 1: print(color.WHITE,end='') 
                elif self._numState[x][y] == 2: print(color.GREEN,end='') 
                elif self._numState[x][y] == 3: print(color.YELLOW,end='') 
                print(' ' + str(self._grid[x][y]) + ' ',end='')
                print(color.END,end='') # Color to normal
          if x == 2 or x == 5:
             print()
             print( "---------------------------------------",end='')
          print()

    # end of display_matrix method


# End of sudokuClass

# Main

def main():
   print("DEBUG: Staring Sudoku")

   # Get Sample from file
   fileName = "examples/test_matrix1.dat"
   print('DEBUG: fileName is (', fileName,')')
   with open(fileName) as f:
      stringMatrix = f.read().splitlines()

   matrix = list(map(int,stringMatrix)) # convert string to integer

   ## print('DEBUG: matrix is (', matrix,')') ##

   sudoku = sudokuClass(matrix)
   ## print('DEBUG: sudokuMatrix is (', sudoku._sudokuMatrix,')') ##

   ## sudoku._grid[0][0] = '4' ## test
   ## sudoku.reset_matrix() ##
   sudoku.display_matrix()
   ## sudoku.export_matrix() ##

if __name__ == '__main__': main()
