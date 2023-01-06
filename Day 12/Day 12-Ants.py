import random
import math

with open('Day 12/Input_12.txt') as f:
  lines = f.read().split('\n')

alphabet = 'SabcdefghijklmnopqrstuvwxyzE'
input = []

for line in lines:
  temp_line = []
  for char in line:
    temp_line.append(alphabet.index(char))
  input.append(temp_line)


def find_index_2d(char, list = input):
  temp_list = []
  for i in range(len(list)):
    for j in range(len(list[i])):
      if(char == list[i][j]):
        temp_list.append(i)
        temp_list.append(j)
  return temp_list

start_point = find_index_2d(0)
end_point = find_index_2d(27)

feromone = [[0 for i in range(len(input[0]))] for j in range(len(input))]

class Ant:

  total_steps = 0
  x, y = 0, 0
  current_height = 0
  world = []
  visited_positions = []
  traveled_path = []
  feromone = []
  last_direction = ""
  random_strength = 2

  def __init__(self, world, start_position, feromone) -> None:
    self.x = start_position[0]
    self.y = start_position[1]
    self.world = world
    self.current_height = world[self.x][self.y]
    self.visited_positions = [[0 for i in range(len(world[0]))] for j in range(len(world))]
    self.feromone = feromone
    self.visited_positions[start_point[0]][start_point[1]] = 1
    
  def see_left(self, x, y, world, current_height, visited_positions, feromone):
    if(x - 1 < 0):
      return
    if(visited_positions[x - 1][y] > 0):
      return
    if(0 <= world[x - 1][y] <= current_height + 1):
      return ["left", feromone[x - 1][y]]
  
  def see_right(self, x, y, world, current_height, visited_positions, feromone):
    if(x + 1 > len(world) - 1):
      return
    if(visited_positions[x + 1][y] > 0):
      return
    if(0 <= world[x + 1][y] <= current_height + 1):
      return ["right", feromone[x + 1][y]]

  def see_up(self, x, y, world, current_height, visited_positions, feromone):
    if(y - 1 < 0):
      return
    if(visited_positions[x][y - 1] > 0):
      return
    if(0 <= world[x][y - 1] <= current_height + 1):
      return ["up", feromone[x][y - 1]]
    
  def see_down(self, x, y, world, current_height, visited_positions, feromone):
    if(y + 1 > len(world[0]) - 1):
      return
    if(visited_positions[x][y + 1] > 0):
      return
    if(0 <= world[x][y + 1] <= current_height + 1):
      return ["down", feromone[x][y + 1]]

  # finds out in which direction the ant can go
  def see(self, x, y, world, current_height, visited_positions, feromone):
    possible_directions = []

    possible_directions.append(self.see_left(x, y, world, current_height, visited_positions, feromone))
    possible_directions.append(self.see_right(x, y, world, current_height, visited_positions, feromone))
    possible_directions.append(self.see_up(x, y, world, current_height, visited_positions, feromone))
    possible_directions.append(self.see_down(x, y, world, current_height, visited_positions, feromone))

    # print(possible_directions)

    return possible_directions

  def decide(self, possible_directions, last_direction):

    temp_list = []
    for direction in possible_directions:
      if(not direction == None):
        temp_list.append(direction)
    possible_directions = temp_list
    


    if(len(possible_directions) == 0):
      match last_direction:
        case "left": return "right"
        case "right": return "left"
        case "up": return "down"
        case "down": return "up"


    for direction in possible_directions:
      # print(possible_directions)
      direction[1] += (random.randrange(10)/10) * self.random_strength

    sorted(possible_directions, key=lambda l:l[1], reverse=True)
    
    return possible_directions[0][0]

  def move(self, direction):
    match direction:
      case "left": self.x += -1
      case "right": self.x += 1
      case "up": self.y += -1
      case "down": self.y += 1

    self.last_direction = direction
    
  def check_endpoint_reached(self, current_height):
    if(current_height < 27):
      return False

    return True

  
  def update_feromone(self, traveled_path, feromone):

    feromone = [[0 for i in range(len(feromone[0]))] for j in range(len(feromone))]

    for path in traveled_path:
      self.feromone[path[0]][path[1]] = 1
        

  def do_action(self):
    x = self.x
    y = self.y
    world = self.world
    current_height = self.current_height

    self.move(self.decide(self.see(x, y, world, current_height, self.visited_positions, self.feromone), self.last_direction))

    self.current_height = world[x][y]
    self.total_steps += 1
    self.visited_positions[x][y] = 1
    self.traveled_path.append([x, y])

    if(self.check_endpoint_reached):
      self.update_feromone(self.traveled_path, self.feromone)

    if(self.total_steps % 1000 == 0):
      print(self.current_height)


ants = [Ant(input, start_point, feromone) for i in range(2)]

finished = False

while(not finished):
  for ant in ants:
    ant.do_action()
    if(ant.current_height == 27):
      finished = True
      print(f"total: {ant.total_steps}")
    