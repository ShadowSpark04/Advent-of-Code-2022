with open('Day 10/Input_10.txt') as f:
  lines = f.read().split('\n')

Cycle_position = []
X = 1


for line in lines:
  if('noop' in line):
    Cycle_position.append(X)
  if('addx' in line):
    Cycle_position.append(X)
    Cycle_position.append(X)
    V = int(''.join([line[line.index(' ') + 1:]]))
    X += V
  if(len(Cycle_position) == 181):
    print('!! here: ', line)




# for char in Cycle_position[180:]:
  # print(char)

# print('---')

total = 0
for i in range(19, len(Cycle_position), 40):
  total += Cycle_position[i] * (i + 1)
  # print(Cycle_position[i] * (i + 1), Cycle_position[i])

print(f'total: {total}')


display = [['.' for i in range(40)] for j in range(6)]


for i in range(len(display)):
  for j in range(len(display[i])):
    x = Cycle_position[(i * 40) + j]
    if(j in [x - 1, x, x + 1]):
      display[i][j] = '#'


for line in display:
  print(line)