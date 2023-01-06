with open('Day 13/Input_13.txt') as f:
  lines = f.read().split('\n')

package_pairs = []
numbers = '0123456789'

def string_to_list(input):
  out = []
  index_start = [i for i, x in enumerate(input) if x == "["]

  list_constrains = []
  level = 0
  for num in index_start:
    temp_list = [num]
    for i in range(num, len(input)):
      
      if(input[i] == ']'): level -= 1
      if(input[i] == '['): level += 1

      if(input[i] == ']' and level == 0): 
        temp_list.append(i)
        break

    
    list_constrains.append(temp_list)
  
  print(list_constrains)

string_to_list("[[1], [2,3,4]]")


temp_list = []
for i in range(0, len(lines)):
  if('[' in lines[i]):
    temp_line = lines[i][:]
    temp_line.split(',')
    list(filter(lambda a: a != ']', temp_line))
    for char in temp_line:
      if(char in numbers):
        int(char)
    print(temp_line)
  
  else:
    package_pairs.append(temp_list)
    temp_list = []

for line in package_pairs:
  print(line)

