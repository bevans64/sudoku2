#!/usr/bin/env python3

import sys

matrix = [0] * 81

fileArg = sys.argv[1]
print('DEBUG: Starting using argument (', fileArg, ')') ##

fileObject = open(fileArg, "rt")

for line in fileObject:

   # Work on Matrix Satements only
   if line[0] == 'M':
      ## print('DEBUG: line is (', line.rstrip(), ')') ##
      y = int(line[7])
      x = int(line[10])
      value = int(line[15])
      matrix[y * 9 + x] = value + 10 # 10 added to define fixed number
      ## print('DEBUG: Matrix statement ', x,y,value)

print('DEBUG: matrix is ...') ##
print(matrix)
