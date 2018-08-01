#!/usr/bin/env python3
# 

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class sudokuClass: 
    _sudokuMatrix = [0] * 81 # Create Sudoku Matrix
    _sudokuMatrixBkp = [0] * 81 # Create Sudoku Matrix Backup

    def __init__(self,matrix):
       print("DEBUG: sudoku class constructor called") ##
       ## print('DEBUG: matrix is (', matrix,')') ##

       self._sudokuMatrix = matrix.copy()
       self._sudokuMatrixBkp = matrix.copy()

    def reset_matrix(self):
       print("DEBUG: sudoku reset_matrix method called") ##
       self._sudokuMatrix = self._sudokuMatrixBkp.copy()

    def display_matrix(self):
       print("DEBUG: sudoku display_matrix method called") ##
       ## print('DEBUG: matrix is (', self._sudokuMatrix,')') ##


       x = 0 
       y = 0 
       for item in self._sudokuMatrix:
          value = item % 10
          numState = item // 10
          if value == 0:
             print('   ',end='')
          else:
             print(' ' + str(value) + ' ',end='')
          x += 1
          if x == 3 or x == 6:
              print("|", end='')
          if x == 9:
             print()
             x = 0
             y += 1
             if y == 3 or y == 6:
                print('-----------------------------')


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

   sudoku.display_matrix()


if __name__ == '__main__': main()
