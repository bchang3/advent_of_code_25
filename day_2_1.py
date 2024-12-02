#brute force
f = open("day_2_input.txt")
lines = f.readlines()
first = [[int(y) for y in x.split()] for x in lines]
count = 0
def checkGood(f):
  start = f[0]
  beginning = True
  success = True
  for i,num in enumerate(f[1:]):
    if num == start:
      success = False
    if beginning:
      increasing = num > start 
      if (abs(num - start) > 3 or abs(num - start) < 1):
        success = False
      beginning = False 
    elif increasing:
      if num <= f[i]:
        success = False
      if num - f[i] > 3:
        success = False
    elif not increasing:
      if f[i] <= num:
        success = False
      if f[i] - num > 3:
        success = False
  return success
for f in first:
  if (checkGood(f)):
    count += 1
print(count)
