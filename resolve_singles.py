# Resolve Singles

tryNum = 5 ##
print "DEBUG: trying ", tryNum  ##

for x in range(0, sudMatrixDim):
    for y in range(0, sudMatrixDim):
       if Matrix[x][y] == tryNum and squareConf[x][y] == 1:
          print "DEBUG: Single Num ", tryNum, " found at (",x,",",y,")"
          NumState[x][y] = 2 # Set unconflicted

          # Find conflicts
          abort = 0
          for z in range(0, sudMatrixDim):
             if Matrix[x][z] == tryNum and z != y:
                print "DEBUG: Conflict num at ",x,",",z
                if squareConf[x][z] == 1:
                   print "DEBUG: This is another single in square conflict number. Aborting operation"
                   abort =1
             if Matrix[z][y] == tryNum and z != x:
                print "DEBUG: Conflict num at ",z,",",y
                if squareConf[z][y] == 1:
                   print "DEBUG: This is another single in square conflict number. Aborting operation"
                   abort =1

          # Eliminate conflicts
          for z in range(0, sudMatrixDim):
             if Matrix[x][z] == tryNum and z != y:
                print "DEBUG: Eliminate num at ",x,",",z
                Matrix[x][z] = 0
                squareConf[x][z] = 0
                boardConf[x][z] = 0
                
             if Matrix[z][y] == tryNum and z != x:
                print "DEBUG: Eliminate num at ",z,",",y
                Matrix[z][y] = 0
                squareConf[x][y] = 0
                boardConf[z][y] = 0
