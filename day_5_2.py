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
incorrect_updates = []
for u in updates:
  #bubble sort
  swapped = True
  incorrect = False
  while swapped:
    seen = set()
    idxs = dict()
    swapped = False
    for idx, i in enumerate(u):
      if (i in ordering_dict):
        for post in ordering_dict[i]:
          if post in seen:
            temp = u[idxs[post]]
            u[idxs[post]] = i 
            u[idx] = post
            swapped = True 
            incorrect = True
            break 
      if (swapped):
        break
      idxs[i] = idx
      seen.add(i)
  if (incorrect):
    incorrect_updates.append(u)
print(incorrect_updates)
print(sum([arr[len(arr)//2] for arr in incorrect_updates]))