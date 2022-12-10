with open('Day 1/Input_1.txt') as f:
  calories = f.read().split('\n')

sub_calories = []
temp_list = []
for line in calories:
  x = 0
  if(line != ''):
    temp_list.append(int(line))
  if(line == ''):
    sub_calories.append(temp_list)
    x += 1
    temp_list = []
    
elfs = []
for elf in sub_calories:
  total = 0
  for num in elf:
    total += num
  elfs.append(total)

print(sorted(elfs))
print(sorted(elfs)[-1] + sorted(elfs)[-2] + sorted(elfs)[-3])