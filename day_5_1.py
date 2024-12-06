f1 = open("day_5_1_input.txt")
f2 = open("day_5_2_input.txt")
ordering_dict = dict()
orderings = [tuple([int(y) for y in x.strip().split("|")]) for x in f1.readlines()]
for o in orderings:
  if (o[0] in ordering_dict):
    ordering_dict[o[0]].append(o[1])
  else:
    ordering_dict[o[0]] = [o[1]]
updates = [[int(y) for y in x.strip().split(",")] for x in f2.readlines()]
correct = []
for u in updates:
  swapped = False
  seen = set()
  idxs = dict()
  for idx, i in enumerate(u):
    if (i in ordering_dict):
      for post in ordering_dict[i]:
        if post in seen:
          swapped = True 
          break 
    if (swapped):
      break
    idxs[i] = idx
    seen.add(i)
  if (not swapped):
    correct.append(u)
print(sum([arr[len(arr)//2] for arr in correct]))