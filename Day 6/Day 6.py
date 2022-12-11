with open('Day 6/Input_6.txt') as f:
  line = f.read()

for i in range(len(line) - 3):
  section = line[i:i+4]
  if (len(set(section)) == len(section)): 
    print(i + 4, set(section), section)
    break

for i in range(len(line) - 13):
  section = line[i:i+14]
  if (len(set(section)) == len(section)): 
    print(i + 14, set(section), section)
    break