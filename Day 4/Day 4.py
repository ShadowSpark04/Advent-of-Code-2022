with open('Day 4/Input_4.txt') as f:
  lines = f.read().split('\n')

pairs = [line.split(',') for line in lines]
total_pairs = 0


for pair in pairs:
  elf1_start = int(pair[0][:pair[0].index('-')])
  elf1_end = int(pair[0][pair[0].index('-') + 1:])
  elf2_start = int(pair[1][:pair[1].index('-')])
  elf2_end = int(pair[1][pair[1].index('-') + 1:])
  
  # print(elf1_start, elf1_end, elf2_start, elf2_end)

  if(elf1_start <= elf2_start and elf1_end >= elf2_end): total_pairs += 1
  elif(elf2_start <= elf1_start and elf2_end >= elf1_end): total_pairs += 1

print(total_pairs)

total_pairs = 0

for pair in pairs:
  elf1_start = int(pair[0][:pair[0].index('-')])
  elf1_end = int(pair[0][pair[0].index('-') + 1:])
  elf2_start = int(pair[1][:pair[1].index('-')])
  elf2_end = int(pair[1][pair[1].index('-') + 1:])
  
  # print(elf1_start, elf1_end, elf2_start, elf2_end)

  if(elf1_end >= elf2_start and elf1_start <= elf2_end): total_pairs += 1

print(total_pairs)
