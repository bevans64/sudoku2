#!/usr/bin/env python3

import sys
sys.path.insert(0,"/home/brad/src/sudoku")

from sudoku import *

def main():
   print("DEBUG: Staring Sudoku")

   # Get Sample from file
   fileName = "/home/brad/src/sudoku/examples/test_matrix2.dat"
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

# Main
if __name__ == '__main__': main()
