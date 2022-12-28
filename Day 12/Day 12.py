import random

with open('Day 12/Input_12.txt') as f:
  lines = f.read().split('\n')

alphabet = 'SabcdefghijklmnopqrstuvwxyzE'
input = []

for line in lines:
  temp_line = []
  for char in line:
    temp_line.append([alphabet.index(char), 0])
  input.append(temp_line)


def find_index_2d (char):
  list = input
  temp_list = []
  for i in range(len(list)):
    for j in range(len(list[i])):
      if(char == list[i][j][0]):
        temp_list.append([i, j, list[i][j][0]])
  return temp_list
  

start_point = find_index_2d(0)[0]
end_point = find_index_2d(27)[0]
current_point = [i for i in end_point]


ants =[[i for i in start_point] for j in range(100)]

def move_ant(ant):
  antx = ant[0]
  anty = ant[1]
  movement = []
  if(antx - 1 >= 0): 
    if(abs(input[antx][anty][0] - input[antx - 1][anty][0]) < 2): movement.append([-1, 0])
  if(antx + 1 <= len(input) - 1):
    if(abs(input[antx][anty][0] - input[antx + 1][anty][0]) < 2): movement.append([1, 0])
  if(anty - 1 >= 0):
    if(abs(input[antx][anty][0] - input[antx][anty - 1][0]) < 2): movement.append([0, -1])
  if(anty + 1 <= len(input[0]) - 1):
    if(abs(input[antx][anty][0] - input[antx][anty + 1][0]) < 2): movement.append([0, 1])
  direction = random.randrange(0, (len(movement)))
  # print(f"m: {movement[direction]}")
  return movement[direction]

for line in input:
  print(line)

k = 0
not_found = True
test = [0, 0]
while (not_found):
  k += 1
  move = move_ant(test)
  test[0] += move[0]
  test[1] += move[1]
  print(test)
  if(input[test[0]][test[1]][0] == 27): not_found = False

print("found!", k)