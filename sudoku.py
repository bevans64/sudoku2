#!/usr/bin/env python3
# 

class sudokuClass: 
    _sudokuMatrix = [0] * 81 # Create Sudoku Matrix
    _grid = [[0 for x in range(9)] for y in range(9)]

    # NumState
    # 0 - Unknown State (YELLOW)
    # 1 - Fixed Number (BOLD)
    # 2 - Unconflicted Number (CYAN)
    # 3 ..  - Conflicted Number

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
                print(' ' + str(self._grid[x][y]) + ' ',end='')
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
