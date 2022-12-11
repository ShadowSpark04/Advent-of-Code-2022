with open('Day 7/Input_7.txt') as f:
  lines = f.read().split('\n')

cd = ['/']
full_dir = []

for i in range(len(lines)):
  if('$ cd' in lines[i]):
    para = lines[i][lines[i].index('d') + 2:]
    if(not '/' in para and not '..' in para): cd.append(para)
    if('..' in para): cd = cd[:-1]
    full_dir.append(cd[:] + ['dir'])
  if('$ ls' in lines[i]):
      no_command = True
      files = []
      j = 1
      while(no_command):
        if(len(lines) != i+j):
          if(not '$' in lines[i + j]):
            if(not 'dir ' in lines[i + j]):
              files.append(lines[i + j])
              j += 1
            else:
              j += 1
          else: no_command = False
        else: 
          files.append(lines[i + 1])
          break
      for file in files:
        full_dir.append(cd[:] + [file] + ['file'])
      
full_dir_set = list(set(map(tuple, full_dir)))

only_dir = []

for item in full_dir_set:
  # print(item)
  if(item[-1] == 'file'):
    size = item[-2][:item[-2].index(' ')]
    # print(size)
    # print(item)
    for k in range(len(item[:-2])):
      hasItem = None
      for item2 in only_dir:
        if(item[:(-2 - k)] == item2[0]): 
          hasItem = item2
          # print('same: ', str(dir), str(item2[0]), str(dir) == str(item2[0]))
      if(hasItem != None):
        # print('index: ', only_dir.index(hasItem))
        only_dir[only_dir.index(hasItem)][1] = int(only_dir[only_dir.index(hasItem)][1]) + int(size)
      else:
        only_dir.append([item[:-2 - k], size])
      


total = 0

for dir in only_dir:
  if(int(dir[1]) <= 100000):
    
    total += int(dir[1])

print(f"total: {total}")

# /       47052440
# total:  70000000
# update: 30000000
# needed: 7052440
#         7268994
#         15124476
#         21231784

space_needed = (30000000 - (70000000 - 47052440))

# sorted(only_dir, key=lambda l:int(l[1]))

smallest_dir = 70000000

for dir in only_dir:
  if(int(dir[1]) >= space_needed):
    if(int(dir[1]) < smallest_dir):
      smallest_dir = int(dir[1])

print(smallest_dir)