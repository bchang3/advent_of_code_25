f = open("day_1_input.txt")
lines = f.readlines()
first = [int(x.split()[0].strip()) for x in lines]
second = [int(x.split()[1].strip()) for x in lines]
first.sort()
second.sort()
print(sum([abs(first[i] - second[i]) for i in range(len(first))]))
