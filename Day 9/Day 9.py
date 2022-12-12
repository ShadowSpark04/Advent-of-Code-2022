with open('Day 9/Input_9.txt') as f:
  lines = f.read().split('\n')

field = [[' ' for y in range(6)] for x in range(6)]

motions = []
for line in lines:
  motions.append([line[:line.index(' ')], int(line[line.index(' ') + 1:])])

visited_positions = []

snake = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]


def move(direction):
  if(direction == 'R'):
    snake[0][0] += 1
  if(direction == 'L'):
    snake[0][0] -= 1
  if(direction == 'U'):
    snake[0][1] += 1
  if(direction == 'D'):
    snake[0][1] -= 1
  
  for i in range(1, len(snake) - 0):
    update_tail(i)

  print(f"snake: {snake}")
  visited_positions.append(snake[9][:])


def update_tail(body_part_index):
  global snake

  if(abs(snake[body_part_index][0] - snake[body_part_index - 1][0]) > 1 or abs(snake[body_part_index][1] - snake[body_part_index - 1][1]) > 1):
    movement_vector = [(x1 - x2) * -1 for (x1, x2) in zip(snake[body_part_index], snake[body_part_index - 1])]
    if(2 in movement_vector):
      occourance = [i for i, x in enumerate(movement_vector) if x == 2]
      for char in occourance:
        movement_vector[char] /= 2
    if(-2 in movement_vector):
      occourance = [i for i, x in enumerate(movement_vector) if x == -2]
      for char in occourance:
        movement_vector[char] /= 2
    print(movement_vector)
    snake[body_part_index][0] += movement_vector[0]
    snake[body_part_index][1] += movement_vector[1]
    
    

  


for motion in motions:
  print("--", motion)
  for i in range(motion[1]):
    move(motion[0])
    

visited_positions_set = list(set(map(tuple, visited_positions)))
print(len(visited_positions_set))
