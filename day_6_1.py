f = open("day_6_input.txt")
area = [list(x.strip()) for x in f.readlines()]
dir = "^"
for i,row in enumerate(area):
  if ("^" in row):
    pos = [i, row.index("^")]
visited = set()
while True:
  visited.add(pos)
  if (dir == "^"):
    if (pos[0] == 0):
      break 
    elif (area[pos[0] - 1][pos[1]] == "#"):
      dir = ">"
    else:
      pos[0] = pos[0] - 1
  elif (dir == ">"):
    if (pos[1] == len(area[0]) - 1):
      break 
    elif (area[pos[0]][pos[1] + 1] == "#"):
      dir = "v"
    else:
      pos[1] = pos[1] + 1
  elif (dir == "<"):
    if (pos[1] == 0):
      break 
    elif (area[pos[0]][pos[1] - 1] == "#"):
      dir = "^"
    else:
      pos[1] = pos[1] - 1
  elif (dir == "v"):
    if (pos[0] == len(area) - 1):
      break 
    elif (area[pos[0] + 1][pos[1]] == "#"):
      dir = "<"
    else:
      pos[0] = pos[0] + 1
print(len(visited))
    