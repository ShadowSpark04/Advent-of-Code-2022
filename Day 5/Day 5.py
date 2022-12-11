with open('Day 5/Input_5-1.txt') as f:
  lines = f.read().split('\n')

def print_table():
  for i in range(height):
    print(table[i])

width = 9
height = 100

table = [[' ' for x in range(width)] for i in range (height)]
instructions = []

j = 0
for line in lines:
  indices = [i+1 for i, x in enumerate(line) if x == "["]
  for ind in indices:
    table[j + height - 8][int((ind-1)/4)] = line[ind]
  j += 1

with open('Day 5/Input_5-2.txt') as f:
  lines_2 = f.read().split('\n')

for line in lines_2:
  char = []
  indices = [i for i, x in enumerate(line) if x == " "]
  char.append(line[indices[0]:indices[1]])
  char.append(line[indices[2]:indices[3]])
  char.append(line[indices[4]:])
  instructions.append(char)

def find_crate(line):
  for row in table:
    if(row[line] != ' '): return table.index(row)
    else: return 0


def move_crate(start, end):
  crate = table[find_crate(start)][start]
  table[find_crate(start)][start] = ' '
  table[find_crate(end) - 1][end] = crate
  
  


for instruction in instructions:
  for i in range(int(instruction[0])):
    move_crate(int(instruction[1]) - 1, int(instruction[2]) - 1)
  print_table()

top_crates = []
for i in range(width):
  top_crates.append(table[find_crate(i)][i])

print(top_crates)