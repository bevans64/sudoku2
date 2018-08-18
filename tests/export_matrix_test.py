#!/usr/bin/env python3

# Constructor tests

import sys
sys.path.insert(0,"/home/brad/src/sudoku")

from sudoku import *

def main():

   # Get Sample 1 from file
   fileName = "/home/brad/src/sudoku/examples/test_matrix1.dat"
   print('DEBUG: fileName is (', fileName,')')
   with open(fileName) as f:
      stringMatrix = f.read().splitlines()

   print("DEBUG: Export Test 1 (expect no error)")
   matrix = list(map(int,stringMatrix)) # convert string to integer # Reset Matrix
   sudoku = sudokuClass(matrix)
   export_list = sudoku.export_matrix()
   if export_list == matrix:
      print("DEBUG:  export list equals construction list")
   else:
      print("DEBUG ERROR:  export list does not equals construction list")
   print()

   # Get Sample 2 from file
   fileName2 = "/home/brad/src/sudoku/examples/test_matrix2.dat"
   print('DEBUG: fileName2 is (', fileName2,')')
   with open(fileName2) as f:
      stringMatrix = f.read().splitlines()

   print("DEBUG: Export Test 2 (expect no error)")
   matrix2 = list(map(int,stringMatrix)) # convert string to integer # Reset Matrix
   sudoku2 = sudokuClass(matrix2)
   export_list2 = sudoku2.export_matrix()
   if export_list2 == matrix2:
      print("DEBUG:  export list equals construction list")
   else:
      print("DEBUG ERROR:  export list does not equals construction list")
   print()

# Main
if __name__ == '__main__': main()
