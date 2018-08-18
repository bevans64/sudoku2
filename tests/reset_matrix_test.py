#!/usr/bin/env python3

# Constructor tests

import sys
sys.path.insert(0,"/home/brad/src/sudoku")

from sudoku import *

def main():

   # Get Sample from file
   fileName = "/home/brad/src/sudoku/examples/test_matrix1.dat"
   print('DEBUG: fileName is (', fileName,')')
   with open(fileName) as f:
      stringMatrix = f.read().splitlines()

   print("DEBUG: reset_matrix Test (expect no errors)")
   matrix = list(map(int,stringMatrix)) # convert string to integer # Reset Matrix
   sudoku = sudokuClass(matrix)

   # Mischief
   sudoku._grid[5][7] = 42 # Hee hee hee
   sudoku._grid[1][6] = 42 # Hee hee hee

   print("DEBUG: Call reset_matrix")
   sudoku.reset_matrix() # reset

   export_list = sudoku.export_matrix()
   if export_list == matrix:
      print("DEBUG:  export list equals construction list")
   else:
      print("DEBUG ERROR:  export list does not equals construction list")

# Main
if __name__ == '__main__': main()
