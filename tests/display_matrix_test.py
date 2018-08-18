#!/usr/bin/env python3

# Constructor tests

import sys
sys.path.insert(0,"/home/brad/src/sudoku")

from sudoku import *

def main():
   print("DEBUG: display_matrix test (expect no errors)")

   # Get Sample from file
   fileName = "/home/brad/src/sudoku/examples/test_matrix1.dat"
   print('DEBUG: fileName is (', fileName,')')
   with open(fileName) as f:
      stringMatrix = f.read().splitlines()

   matrix = list(map(int,stringMatrix)) # convert string to integer

   sudoku = sudokuClass(matrix)

   print("DEBUG: Bad type value (expect error)")
   sudoku.display_matrix(42)

   print("DEBUG: Display grid")
   sudoku.display_matrix(0)

   print("DEBUG: Display row and column conflicts")
   sudoku.display_matrix(1)

   print("DEBUG: Display square conflicts")
   sudoku.display_matrix(2)

# Main
if __name__ == '__main__': main()
