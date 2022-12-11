with open('Day 5/Input_5-2.txt') as f:
  lines_2 = f.read().split('\n')

instructions = []

for line in lines_2:
  char = []
  indices = [i for i, x in enumerate(line) if x == " "]
  char.append(line[indices[0]:indices[1]])
  char.append(line[indices[2]:indices[3]])
  char.append(line[indices[4]:])
  instructions.append(char)

with open('Day 5/Input_5-1.txt') as f:
  lines = f.read().split('\n')

table = [[], [], [], [], [], [], [], [], []]

j = 0
for line in lines:
  indices = [i+1 for i, x in enumerate(line) if x == "["]
  for ind in indices:
    table[int((ind-1)/4)].append(line[ind])
  j += 1

for i in range(len(table)):
  table[i].reverse()



def move_crate(start, end):
  table[end].append(table[start].pop(len(table[start]) - 1))

for instruction in instructions:
  for i in range(int(instruction[0])):
    move_crate(int(instruction[1]) - 1, int(instruction[2]) - 1)

print(table)

for row in table:
  print(row.pop())



table = [[], [], [], [], [], [], [], [], []]

j = 0
for line in lines:
  indices = [i+1 for i, x in enumerate(line) if x == "["]
  for ind in indices:
    table[int((ind-1)/4)].append(line[ind])
  j += 1

for i in range(len(table)):
  table[i].reverse()



def move_crate2(start, end, amount):
  liste = []
  print(table)
  for i in range(amount):
    liste.append(table[start].pop())
  for i in range(len(liste)):
    table[end].append(liste.pop())

for instruction in instructions:
  move_crate2(int(instruction[1]) - 1, int(instruction[2]) - 1, int(instruction[0]))

print(table)

for row in table:
  print(row.pop())