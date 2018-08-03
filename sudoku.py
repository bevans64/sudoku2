#!/usr/bin/env python3
# 

class constant:
   square_dim          = 3
   board_dim           = 9
   unknown_state       = 0
   fixed_number        = 1
   unconflicted_number = 2
   conflicted_number   = 3 

class color: 
   BLACK  = '\33[30m'
   RED    = '\33[31m'
   GREEN  = '\33[32m'
   YELLOW = '\33[33m'
   BLUE   = '\33[34m'
   VIOLET = '\33[35m'
   BEIGE  = '\33[36m'
   WHITE  = '\33[37m'
   END    = '\033[0m'

class sudokuClass: 
    _sudokuList = [0] * constant.board_dim**2 # Create Sudoku Matrix ## Change to _sudokuList
    _grid = [[0 for x in range(9)] for y in range(9)]

    # _numState
    # 0 - Unknown State (RED, constant.unknown_state)
    # 1 - Fixed Number (WHITE, constant.fixed_number)
    # 2 - Unconflicted Number (GREEN, constant.unconflicted_number)
    # 3 - Conflicted Number (YELLOW, constant.conflicted_number)

    _numState = [[constant.unknown_state for x in range(constant.board_dim)] for y in range(constant.board_dim)]


    # Number of conflicts across the board
    _boardConf = [[0 for x in range(constant.board_dim)] for y in range(constant.board_dim)]

    # Number of conflicts across the square
    _squareConf = [[0 for x in range(constant.board_dim)] for y in range(constant.board_dim)]


    def __init__(self,matrix):
       print("DEBUG: sudoku class constructor called")
       # print('DEBUG: matrix is (', matrix,')')

       self._sudokuList = matrix.copy()
       self.reset_matrix() # sets Grids

    # end of constructor

    def reset_matrix(self): 
       print("DEBUG: sudoku reset_matrix method called")
       
       # Initialize Arrays
       for x in range(constant.board_dim):
          for y in range(constant.board_dim):
             self._grid[x][y] = self._sudokuList[x*constant.board_dim+y] % 10
             self._numState[x][y] = self._sudokuList[x*constant.board_dim+y] // 10
             self._boardConf[x][y] = 0
             self._squareConf[x][y] = 0

    # end of reset_martix method

    def export_matrix(self):
       print("DEBUG: sudoku export_matrix method called")

       # export grids
       returnList = []
       for x in range(constant.board_dim):
          for y in range(constant.board_dim):
             returnList.append(self._grid[x][y] + self._numState[x][y] * 10)

       return returnList

    # end of export_martix method

    def display_matrix(self,type):
       # type 0 display grid, type 1 display boardConf, type 2 display squareConf
       print("DEBUG: sudoku display_matrix method called. type is (",type,")")

       # Select grid to display
       if type == 0:
          matrix = self._grid
       elif type == 1:
          matrix = self._boardConf
       elif type == 2:
          matrix = self._squareConf

       for x in range(constant.board_dim):
          for y in range(constant.board_dim):
             if y == 3 or y == 6:
                print("|",end='')
             if matrix[x][y] == 0:
                print("   ",end='')
             else:
                if self._numState[x][y] == constant.unknown_state: print(color.RED,end='')  # Set Color
                elif self._numState[x][y] == constant.fixed_number: print(color.WHITE,end='') 
                elif self._numState[x][y] == constant.unconflicted_number: print(color.GREEN,end='') 
                elif self._numState[x][y] == constant.conflicted_number: print(color.YELLOW,end='') 
                print(' ' + str(matrix[x][y]) + ' ',end='')
                print(color.END,end='') # Color to normal
          if x == 2 or x == 5:
             print()
             print( "----------------------------",end='')
          print()

    # end of display_matrix method

    def map_number(self,number): 
       # print("DEBUG: sudoku map_number method called. number is (", number, ")") 

       # Number must be between 1 and 9 inclusive
       if number <1 or number > 9:
          print("ERROR: map_number: number out of range")
          return 1

       for x in range(constant.board_dim):
          for y in range(constant.board_dim):
             ##if self._numState[x][y] == constant.fixed_number or self._numState[x][y] == constant.unconflicted_number: # Skip if fixed number or unconflicted number exists
             if self._numState[x][y] in (constant.fixed_number,constant.unconflicted_number): # Skip if fixed number or unconflicted number exists
                continue
             elif self.test_num_in_square(number,0,x,y): # test for fixed numbers
                continue
             elif self.test_board_conflict(number,0,x,y): # test for fixed numbers
                continue
             else:
                self._grid[x][y] = number
    # end of map_number method

    def test_board_conflict(self,number,type,x,y): # Does the number exist along the row or column ?
       # type = 0 test fixed numbers.  type = 1 test non fixed
       # print("DEBUG: sudoku test_board_conflict method called. coordinates are are (", x,",",y, "). Number is (",number,")") 

       for z in range(constant.board_dim):
          if type == 0:
             if number == self._grid[x][z] and self._numState[x][z] == constant.fixed_number: return True
             if number == self._grid[z][y] and self._numState[z][y] == constant.fixed_number: return True
          else:
             if number == self._grid[x][z] and self._numState[x][z] != constant.fixed_number: return True
             if number == self._grid[z][y] and self._numState[z][y] != constant.fixed_number: return True

       return False

    # end of test_board_conflict method

    def test_num_in_square(self,number,type,x,y): # Is number in same square?
       # type = 0 test fixed numbers.  type = 1 test non fixed
       # print("DEBUG: sudoku test_fixed_num_insquare method called. coordinates are are (", x,",",y, "). Number is (",number,")") 

       # What Square are the coordinates in ?
       a = x // constant.square_dim
       b = y // constant.square_dim
       square = (a) * constant.square_dim + (b)
       # print("DEBUG: square is ", square) 
       for j in range(a*constant.square_dim,a*constant.square_dim+constant.square_dim):
          for k in range(b*constant.square_dim,b*constant.square_dim+constant.square_dim):
             if type == 0:
                if number == self._grid[j][k] and self._numState[j][k] == constant.fixed_number:
                   # print("DEBUG: ", number, "found in square", square)
                   return True
             else:
                if number == self._grid[j][k] and self._numState[j][k] != constant.fixed_number:
                   # print("DEBUG: ", number, "found in square", square)
                   return True

       return False

    # end of test_fixed_num_in_square method


# End of sudokuClass
