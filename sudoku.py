#!/usr/bin/env python3
# 

class sudokuClass: 
    _sudokuMatrix = [0] * 81

    def __init__(self,matrix):
       print("DEBUG: sudoku class constructor called") ##
       ## print('DEBUG: matrix is (', matrix,')') ##

       self._sudokuMatrix = matrix

    def display_matrix(self):
       print("DEBUG: sudoku display_matrix methodx called") ##
       ## print('DEBUG: matrix is (', self._sudokuMatrix,')') ##





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
