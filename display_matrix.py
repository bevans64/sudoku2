print "DEBUG: Displaying Suduku Board"

for x in range(sudMatrixDim):
   for y in range(sudMatrixDim):
      if y == 3 or y == 6:
         print "|",
      if Matrix[x][y] == 0:
         print "   ",
      else:
         if NumState[x][y] == 1: # if fixed number
            print color.BOLD,
         ## elif NumState[x][y] > 2: # if conflicting number
         elif NumState[x][y] == 3: # if conflicting number
            print color.RED,
         else:
            print color.YELLOW, # Unconflicted number
         print Matrix[x][y],
         print color.END, # set colour normal
   if x == 2 or x == 5:
      print
      print "---------------------------------------",
   print

## Display boardConfs for Debug
print ##
for x in range(sudMatrixDim): ##
   for y in range(sudMatrixDim): ##
      if y == 3 or y == 6: ##
         print "|", ##
      if boardConf[x][y] == 0: ##
         print "   ", ##
      else: ##
         print color.CYAN, ##
         print boardConf[x][y], ##
         print color.END, # set colour normal ##
   if x == 2 or x == 5: ##
      print ##
      print "---------------------------------------", ##
   print ##

## Display squareConfs for Debug
print ##
for x in range(sudMatrixDim): ##
   for y in range(sudMatrixDim): ##
      if y == 3 or y == 6: ##
         print "|", ##
      if squareConf[x][y] == 0: ##
         print "   ", ##
      else: ##
         print color.GREEN, ##
         print squareConf[x][y], ##
         print color.END, # set colour normal ##
   if x == 2 or x == 5: ##
      print ##
      print "---------------------------------------", ##
   print ##
