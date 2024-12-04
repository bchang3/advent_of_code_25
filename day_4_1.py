f = open("day_4_input.txt")
lines = [x.strip() for x in f.readlines()]
count = 0
for i,line in enumerate(lines):
  for j,c in enumerate(line):
    if (c == "S" or c == "X"):
      if (j <= len(line) - 4):
        if (line[j:j+4] == "XMAS" or line[j:j+4] == "SAMX"):
          count += 1
      if (i <= len(lines)- 4):
        vertical = lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j]
        if (vertical == "XMAS" or vertical == "SAMX"):
          count += 1
        if (j <= len(line) - 4):
          right_diag = lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3]
          if (right_diag == "XMAS" or right_diag == "SAMX"):
            count += 1
        if (j >= 3):
          left_diag = lines[i][j] + lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3]
          if (left_diag == "XMAS" or left_diag == "SAMX"):
            count += 1
        
print(count)
