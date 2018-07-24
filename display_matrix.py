def display_matrix(mode):
   print "DEBUG: Displaying Suduku Board"
   print "DEBUG: mode is (", mode,")"

   # mode = 0 show only Sudoku board
   #        1 also show board conflicts
   #        2 also show square conflicts

   for x in range(sudMatrixDim):
      for y in range(sudMatrixDim):
         if y == 3 or y == 6:
            print "|",
         if Matrix[x][y] == 0:
            print "   ",
         else:
            if NumState[x][y] == 1: # if fixed number
               print color.BOLD,
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

   # Display boardConfs for Debug
   if mode > 0:
      print 
      for x in range(sudMatrixDim): 
         for y in range(sudMatrixDim): 
            if y == 3 or y == 6: 
               print "|", 
            if boardConf[x][y] == 0: 
               print "   ", 
            else: 
               print color.CYAN, 
               print boardConf[x][y], 
               print color.END, # set colour normal 
         if x == 2 or x == 5: 
            print 
            print "---------------------------------------", 
         print 

   # Display squareConfs for Debug
   if mode > 1:
      print 
      for x in range(sudMatrixDim): 
         for y in range(sudMatrixDim): 
            if y == 3 or y == 6: 
               print "|", 
            if squareConf[x][y] == 0: 
               print "   ", 
            else: 
               print color.GREEN, 
               print squareConf[x][y], 
               print color.END, # set colour normal 
         if x == 2 or x == 5: 
            print 
            print "---------------------------------------", 
         print 

   return
# End of function

display_matrix(2)
