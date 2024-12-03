import re
f = open("day_3_input.txt")
content = "".join(f.readlines())
enabled = True
summ = 0
for match in re.finditer(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', content):
    value = match.group(0)
    if (value == "do()"):
        enabled = True 
    elif (value == "don't()"):
      enabled = False
    elif (enabled):
       nums = [int(x) for x in value[4:-1].split(",")]
       summ += nums[0] * nums[1]
print(summ)

