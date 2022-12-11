with open('Day 3/Input_3.txt') as f:
  lines = f.read().split('\n')

values = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
prio_sum = 0

for line in lines:
  shared_item = ''
  comp1 = line[:int(len(line)/2)]
  comp2 = line[int(len(line)/2):]
  for char in comp1:
    if(char in comp2): shared_item = char
  prio_sum += values.index(shared_item) + 1
print(prio_sum)

prio_sum = 0

grouped_lines = []
for i in range(int(len(lines) / 3)):
  group = []
  group.append(lines[i * 3])
  group.append(lines[i * 3 + 1])
  group.append(lines[i * 3 + 2])
  
  grouped_lines.append(group)


for group in grouped_lines:
  shared_item = ''
  for char in group[0]:
    if(char in group[1] and char in group[2]): 
      shared_item = char
  prio_sum += values.index(shared_item) + 1

print(prio_sum)