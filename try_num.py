
def fill_square(num,startx,starty,endx,endy):
   print "DEBUG: Filling square"
   print "DEBUG: Filling with number", num
   print "DEBUG: Dimensions: ", startx, starty, endx, endy

   # Does square already have the number fixed ?
   endx += 1
   endy += 1
   for x in range(startx, endx):
      for y in range(starty, endy):
         if Matrix[x][y] == num and NumState[x][y] == 1:
            print "DEBUG: Number (", num, ") is already in square. Exiting function"
            return

   # Filling Square
   print "DEBUG: Setting Number in square"
   for x in range(startx, endx):
      for y in range(starty, endy):
         if NumState[x][y] == 0:
            testState = 0
            for z in range(0, sudMatrixDim):
               if Matrix[x][z] == num and NumState[x][z] == 1:
                  testState = 1
               if Matrix[z][y] == num and NumState[z][y] == 1:
                  testState = 1
            if testState == 0:
               print "DEBUG: Setting ",x,y, " to ", num
               Matrix[x][y] = num
   return
# End Function

def analyze_square(num,startx,starty,endx,endy):
   print "DEBUG: Analyzing number", num
   print "DEBUG: Dimensions: ", startx, starty, endx, endy
   endx += 1
   endy += 1

   for x in range(startx, endx):
      for y in range(starty, endy):
         if Matrix[x][y] == num and NumState[x][y] != 1 and NumState[x][y] != 2:
            ## print "DEBUG: Number ",num, " found at (",x,",",y,")"
            NumState[x][y] = 2 # Set to unconflicted

            # Check Conflicts
            testState = 0
            for z in range(0, sudMatrixDim):
               if Matrix[x][z] == num:
                  testState += 1
               if Matrix[z][y] == num:
                  testState += 1
            if testState > 2:
               print "DEBUG: Setting ",num, " at ",x,y, " to conflicted"
               NumState[x][y] = 3 # conflicted
               boardConf[x][y] = testState - 2 # conflicted

   ## Count in Square Conflicts

   return
# End Function

##tryNum = 5 ## num to try ##
##print "DEBUG: trying - ", tryNum ##
 
for tryNum in range(1,10): ##
   fill_square(tryNum,0,0,2,2) # Square 1 ##
   fill_square(tryNum,0,3,2,5) # Square 2 ##
   fill_square(tryNum,0,6,2,8) # Square 3 ##
   fill_square(tryNum,3,0,5,2) # Square 4 ##
   fill_square(tryNum,3,3,5,5) # Square 5 ##
   fill_square(tryNum,3,6,5,8) # Square 6 ##
   fill_square(tryNum,6,0,8,2) # Square 7 ##
   fill_square(tryNum,6,3,8,5) # Square 8 ##
   fill_square(tryNum,6,6,8,8) # Square 9 ##

   analyze_square(tryNum,0,0,2,2) # Square 1 ##
   analyze_square(tryNum,0,3,2,5) # Square 2 ##
   analyze_square(tryNum,0,6,2,8) # Square 3 ##
   analyze_square(tryNum,3,0,5,2) # Square 4 ##
   analyze_square(tryNum,3,3,5,5) # Square 5 ##
   analyze_square(tryNum,3,6,5,8) # Square 6 ##
   analyze_square(tryNum,6,0,8,2) # Square 7 ##
   analyze_square(tryNum,6,3,8,5) # Square 8 ##
   analyze_square(tryNum,6,6,8,8) # Square 9 ##
