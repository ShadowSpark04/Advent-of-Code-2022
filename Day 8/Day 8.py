with open('Day 8/Input_8.txt') as f:
  lines = f.read().split('\n')

forest = []
sichtbare_bäume = []

# Creates the forest layout
for line in lines:
  row = []
  for char in line:
    row.append(int(char))
  forest.append(row)

# Creates a empty copy of the forest layout
for i in range(len(forest)):
  new_row = []
  for j in range(len(forest[i])):
    new_row.append(0)
  sichtbare_bäume.append(new_row)


def rotate_2dlist_90(matrix):
  rotated_matrix = []
  for i in range(len(matrix)):
    new_row = []
    for j in range(len(matrix[i])):
      new_row.append(matrix[j][i])
    new_row_reverse = []
    for j in range(len(new_row)):
      new_row_reverse.append(new_row[-j-1])
    rotated_matrix.append(new_row_reverse)
  return rotated_matrix


forest_cardinal_perspective = [forest, rotate_2dlist_90(forest), rotate_2dlist_90(rotate_2dlist_90(forest)), rotate_2dlist_90(rotate_2dlist_90(rotate_2dlist_90(forest)))]


# markiert sichtbare bäume mit einer 1
for perspective in forest_cardinal_perspective:
  for i in range(len(perspective)):
    höchste_zahl = -1
    for j in range(len(perspective[i])):
      if(perspective[i][j] > höchste_zahl):
        höchste_zahl = perspective[i][j]
        sichtbare_bäume[i][j] = 1
  sichtbare_bäume = rotate_2dlist_90(sichtbare_bäume)


total = 0
for row in sichtbare_bäume:
  for char in row:
    if(char == 1):
      total += 1

print(total, '\n')

scenic_score = []
for i in range(len(forest)):
  new_row = []
  for j in range(len(forest[i])):
    new_row.append(1)
  scenic_score.append(new_row)


for perspective in forest_cardinal_perspective:
  for i in range(len(perspective)):
    for j in range(len(perspective[i])):
      if(i == 0 or j == 0 or i == len(forest) - 1 or j == len(forest) - 1):
        scenic_score[i][j] = 0
      else:
        
        section = perspective[i][:j]
        section.reverse()
        scenic_score_direction = 0
        height = perspective[i][j]
        for k in range(len(section)):
          scenic_score_direction = k
          if(section[k] >= height): break
        scenic_score_direction += 1
        scenic_score[i][j] *= scenic_score_direction
        # print(i, j, scenic_score[i][j])
  scenic_score = rotate_2dlist_90(scenic_score)
  for row in scenic_score:
    print(row)
  print('-')



# prints forest perspective and scenic score
for perspective in forest_cardinal_perspective:
  for row in perspective:
    print(row)
  print('---')

for row in scenic_score:
  print(row)

total = 0
for row in scenic_score:
  for char in row:
    if(char > total): total = char

print(f": {total}")
