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
    _sudokuList = [0] * 81 # Create Sudoku Matrix ## Change to _sudokuList
    _grid = [[0 for x in range(9)] for y in range(9)]

    # _numState
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

       self._sudokuList = matrix.copy()
       self.reset_matrix() # sets Grids
    # end of constructor

    def reset_matrix(self): 
       print("DEBUG: sudoku reset_matrix method called") ##
       
       # Initialize Arrays
       for x in range(9):
          for y in range(9):
             self._grid[x][y] = self._sudokuList[x*9+y] % 10
             self._numState[x][y] = self._sudokuList[x*9+y] // 10
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

    def map_number(self,number): ## Under construction
       ## print("DEBUG: sudoku map_number method called. number is (", number, ")") ##

       # Number must be between 1 and 9 inclusive
       if number <1 or number > 9:
          print("ERROR: map_number: number out of range")
          return 1

       for x in range(9):
          for y in range(9):
             if self._numState[x][y] == 1 or self._numState[x][y] == 2: # Skip if fixed number or unconflicted number exists
                continue
             elif self.test_fixed_num_in_square(number,x,y):
                continue
             elif self.test_board_conflict(number,x,y):
                continue
             else:
                self._grid[x][y] = number
    # end of map_number method

    def test_board_conflict(self,number,x,y): # Does the number exist along the row or column ?
       ## print("DEBUG: sudoku test_board_conflict method called. coordinates are are (", x,",",y, "). Number is (",number,")") ##

       for z in range(9):
          if number == self._grid[x][z] and self._numState[x][z] == 1: return True
          if number == self._grid[z][y] and self._numState[z][y] == 1: return True
       return False

    # end of test_board_conflict method

    def test_fixed_num_in_square(self,number,x,y): # Is number in same square?
       ## print("DEBUG: sudoku test_fixed_num_insquare method called. coordinates are are (", x,",",y, "). Number is (",number,")") ##

       # What Square are the coordinates in ?
       a = x // 3
       b = y // 3
       square = (a) * 3 + (b)
       ## print("DEBUG: square is ", square) ##
       for j in range(a*3,a*3+3):
          for k in range(b*3,b*3+3):
             if number == self._grid[j][k] and self._numState[j][k] == 1:
                ## print("DEBUG: ", number, "found in square", square)
                return True

       return False

    # end of test_fixed_num_in_square method


# End of sudokuClass
