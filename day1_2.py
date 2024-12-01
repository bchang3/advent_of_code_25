f = open("day_1_input.txt")
lines = f.readlines()
first = [int(x.split()[0].strip()) for x in lines]
second = [int(x.split()[1].strip()) for x in lines]
counts = dict()
for s in second:
  if s in counts:
    counts[s] += 1
  else:
    counts[s] = 1
print(sum([x * (0 if x not in counts else counts[x]) for x in first]))
  