#!/usr/bin/env python3

# Constructor tests

import sys
sys.path.insert(0,"/home/brad/src/sudoku")

from sudoku import *

def main():
   print("DEBUG: Staring Sudoku Constructor Tests")

   print("DEBUG: Boundary Tests")

   # Get Sample from file
   fileName = "/home/brad/src/sudoku/examples/test_matrix1.dat"
   print('DEBUG: fileName is (', fileName,')')
   with open(fileName) as f:
      stringMatrix = f.read().splitlines()

   matrix = list(map(int,stringMatrix)) # convert string to integer

   print("DEBUG:  Test matrix element out of bounds (expect failure)")
   matrix.append(5) # add extra element hee hee hee
   sudoku = sudokuClass(matrix) # Should fail
   print()

   print("DEBUG: Test if bad element in matrix (expect failure)")
   matrix = list(map(int,stringMatrix)) # convert string to integer # Reset Matrix
   matrix[10] = 42 # hee hee hee
   sudoku = sudokuClass(matrix) # Should fail
   print()

   print("DEBUG: Good Test (expect no errors)")
   matrix = list(map(int,stringMatrix)) # convert string to integer # Reset Matrix
   sudoku = sudokuClass(matrix)
   print()

# Main
if __name__ == '__main__': main()
