f = open("day_4_input.txt")
lines = [x.strip() for x in f.readlines()]
count = 0
checker = { "MS", "SM" }
for i,line in enumerate(lines):
  if (i == 0 or i == len(lines) - 1):
    continue
  for j,c in enumerate(line):
    if (j == 0 or j == len(line) - 1):
      continue
    if (c == "A"):
      if (lines[i-1][j-1] + lines[i+1][j+1] in checker and lines[i+1][j-1] + lines[i-1][j+1] in checker):
        count += 1
print(count)
