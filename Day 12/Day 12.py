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


def distance(start, end):
  return math.sqrt(math.pow(start[0] - end[0], 2) + math.pow(start[1] - end[1], 2))

def find_index_2d(char):
  list = input
  temp_list = []
  for i in range(len(list)):
    for j in range(len(list[i])):
      if(char == list[i][j]):
        temp_list.append(i)
        temp_list.append(j)
  return temp_list
  

start_point = find_index_2d(0)
end_point = find_index_2d(27)
current_point = [i for i in end_point]





class Ant:

  steps = 0
  movement = []
  last_move = []
  current_level = 27
  mark = []

  def __init__(self, world, smell, x, y, end):
    self.x = x
    self.y = y
    self.world = world
    self.smell = smell
    self.end = end
    self.last_move = [self.x-1, self.y-1]
    self.visited = [[j for j in i] for i in world]
    self.mark = end


    
    

  def see(self):
    self.movement = []
    if(self.x -1 >= 0): # links
      if(0 <= self.world[self.x][self.y] <= self.world[self.x - 1][self.y] - 1): self.movement.append([self.x - 1, self.y])
    if(self.y -1 >= 0): # oben
      if(0 <= self.world[self.x][self.y] <= self.world[self.x][self.y - 1] - 1): self.movement.append([self.x, self.y - 1])
    if(self.x +1 <= len(self.world) - 1): # rechts
      if(0 <= self.world[self.x][self.y] <= self.world[self.x + 1][self.y] - 1): self.movement.append([self.x + 1, self.y])
    if(self.y +1 <= len(self.world[0]) - 1): # unten
      if(0 <= self.world[self.x][self.y] <= self.world[self.x][self.y + 1] - 1): self.movement.append([self.x, self.y + 1])
    
    

  def decide(self):
    for move in self.movement:
      hight = self.world[self.x][self.y] - self.world[move[0]][move[1]]

      distance_value = (distance(move, self.mark) / distance([self.x, self.y], self.mark)) / 5
      direction_value = distance(self.last_move, move) / 2
      height_value = hight * 1.2
      random_value = (random.randrange(0, 100) / 50) * 1

      # print(f"dist: {distance_value}, dir: {direction_value}, height: {height_value}, rand: {random_value}")
      move.append(distance_value + direction_value + height_value + random_value)
    self.movement = sorted(self.movement, key=lambda l:l[2])

    # for move in self.movement:
     # if(self.visited[move[0]][move[1]] == 'x' and len(self.movement) > 1): 
        # self.movement.remove(move)
        # print('Removed!')
    # print(self.movement)
    
    self.move(self.movement[0][:2])

  def move(self, point):
    if (not self.check()):
      self.steps += 1
      # print(input[self.x][self.y], input[point[0]][point[1]])
      self.last_move.append(self.x)
      self.last_move.append(self.y)
      
      self.x = point[0]
      self.y = point[1]

      self.visited[self.x][self.y] = 'x'

      # print(self.visited == self.world)

      

      if(self.steps % 1000 == 0): 
        print(self.world[self.x][self.y])
        # self.search_new_mark(self.x, self.y)

      if(self.current_level > self.world[self.x][self.y]):
        self.current_level = self.world[self.x][self.y]
        

  def check(self):
    return self.world[self.x][self.y] == 0


  def search_new_mark(self, X, Y):
    x = y = 0
    dx = 0
    dy = -1
    for i in range(max(X, Y)**2):
      if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
        # print (x, y)
        try:
          if(self.world[self.x + x][self.y + y] == self.current_level - 1):
            # self.current_level -= 1
            self.mark = [self.x + x, self.y + y]
        except IndexError:
          pass

      if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
          dx, dy = -dy, dx
      x, y = x+dx, y+dy

total = 10000

ants = [Ant(input, [], end_point[0], end_point[1], start_point) for i in range(10)]

test = True

while(test):
  for i in range(len(ants)):
    ants[i].see()
    ants[i].decide()

    # if(ants[i].steps % 100 == 0): print(i, ants[i].x, ants[i].y)

    if(ants[i].steps > 100000): test = False

for ant in ants:
  if(ant.steps < total): total = ant.steps
print(total)

  
    


"""
if(antx - 1 >= 0): 
  if(abs(input[antx][anty][0] - input[antx - 1][anty][0]) < 2): movement.append([-1, 0])
if(antx + 1 <= len(input) - 1):
  if(abs(input[antx][anty][0] - input[antx + 1][anty][0]) < 2): movement.append([1, 0])
if(anty - 1 >= 0):
  if(abs(input[antx][anty][0] - input[antx][anty - 1][0]) < 2): movement.append([0, -1])
if(anty + 1 <= len(input[0]) - 1):
  if(abs(input[antx][anty][0] - input[antx][anty + 1][0]) < 2): movement.append([0, 1])
"""