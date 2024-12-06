f = open("day_6_input.txt")
area = [list(x.strip()) for x in f.readlines()]
for i,row in enumerate(area):
  if ("^" in row):
    pos = [i, row.index("^")]

start = pos.copy()
count = 0
#brute force by trying every obstacle location...
for i in range(len(area)):
  for j in range(len(area[i])):
    dir = "^"
    visited = set()
    pos = start.copy()
    obstructions = set()
    if (area[i][j] == "."):
      area[i][j] = "#"
      while True:
        if ((pos[0], pos[1], dir) in visited):
          count += 1
          break
        if (dir == "^"):
          visited.add((pos[0], pos[1], "^"))
          if (pos[0] == 0):
            break 
          elif (area[pos[0] - 1][pos[1]] == "#"):
            dir = ">"
          else:
            pos[0] = pos[0] - 1
        elif (dir == ">"):
          visited.add((pos[0], pos[1], ">"))
          if (pos[1] == len(area[0]) - 1):
            break 
          elif (area[pos[0]][pos[1] + 1] == "#"):
            dir = "v"
          else:
            pos[1] = pos[1] + 1
        elif (dir == "<"):
          visited.add((pos[0], pos[1], "<"))
          if (pos[1] == 0):
            break 
          elif (area[pos[0]][pos[1] - 1] == "#"):
            dir = "^"
          else:
            pos[1] = pos[1] - 1
        elif (dir == "v"):
          visited.add((pos[0], pos[1], "v"))
          if (pos[0] == len(area) - 1):
            break 
          elif (area[pos[0] + 1][pos[1]] == "#"):
            dir = "<"
          else:
            pos[0] = pos[0] + 1
      area[i][j] = "."
print(count)