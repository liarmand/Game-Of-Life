field = [[0,1,1,0,1],[1,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0],[1,0,0,0,1]]
n = 5

def getNeighbourCount(field, i, j, n):
  result = 0
  if (i != 0 and j != 0 and field[i - 1][j - 1] == 1):
    result +=1
  if (i != 4 and j != 4 and field[i + 1][j + 1] == 1):
    result +=1
  if (i != 0 and j != 4 and field[i - 1][j + 1] == 1):
    result +=1
  if (i != 4 and j != 0and field[i + 1][j - 1] == 1):
    result +=1
  if (i != 0 and field[i - 1][j] == 1):
    result +=1
  if (i != 4 and field[i + 1][j] == 1):
    result +=1
  if (j != 0 and field[i][j - 1] == 1):
    result +=1
  if (j != 4 and field[i][j + 1] == 1):
    result +=1
  return result

def showField(field, n):
  for i in range(0,n):
    for j in range(0,n):
      print(field[i][j], end=' ')
    print("\n")

def fieldUpdate(field, n):
  for i in range(0,n):
    for j in range(0,n):
      if (field[i][j] == 1):
        if (getNeighbourCount(field, i, j, n) == 2 or getNeighbourCount(field, i, j, n) == 3):
          field[i][j] = 1;
        else:
          field[i][j] = 0;
      if (field[i][j] == 0):
        if (getNeighbourCount(field, i, j, n) == 3):
          field[i][j] = 1

for i in range(0,20):
  showField(field, n)
  fieldUpdate(field, n)


#Tests

def affirm(condition, testName):
  if(!condition):
    print("Failed in" + testName)
  else:
    print("Passed " + testName)
  
      
def fieldCreation(field):
  affirm(field)

def fieldSize(field):
  lines = 0
  columns = 0
  for i in field:
    lines += 1
    for j in i:
      columns += 1
  columns /= lines
  affirm(lines == columns)
  
def cellNeighbours(field, n):
  for i in range(0,n):
    for j in range(0,n):
      affirm(getNeighbourCount(field, i, j, n) >= 0 and getNeighbourCount(field, i, j, n) <= 8)

#main
fieldCreation(field, "fieldCreation")
fieldSize(field, "fieldSize")
cellNeighbours(field, 5, "cellNeighbours")
