with open('Day 2/Input_2.txt') as f:
  lines = f.read().split('\n')

total_score = 0

# A/X: Rock(1) | B/Y: Paper(2) | C/Z: Scissors(3) | loss: 0 | draw: 3 | win: 6

for line in lines:
  round = line.split(' ')
  if(round[1] == 'X'): total_score += 1
  if(round[1] == 'Y'): total_score += 2
  if(round[1] == 'Z'): total_score += 3

  round_repl = [round[0].replace('A', 'X').replace('B', 'Y').replace('C', 'Z'), round[1]]
  if(round_repl[0] == round_repl[1]): total_score += 3
  if(round_repl[0] == 'X' and round_repl[1] == 'Y'): total_score += 6
  if(round_repl[0] == 'X' and round_repl[1] == 'Z'): total_score += 0
  if(round_repl[0] == 'Y' and round_repl[1] == 'X'): total_score += 0
  if(round_repl[0] == 'Y' and round_repl[1] == 'Z'): total_score += 6
  if(round_repl[0] == 'Z' and round_repl[1] == 'Y'): total_score += 0
  if(round_repl[0] == 'Z' and round_repl[1] == 'X'): total_score += 6

print(total_score)

# X: lose | Y: draw | Z: win

total_score = 0

for line in lines:
  round = line.split(' ')
  round_repl = [round[0].replace('A', '1').replace('B', '2').replace('C', '3'), round[1]]
  if(round[1] == 'X'): total_score += 0
  if(round[1] == 'Y'): total_score += 3 + int(round_repl[0])
  if(round[1] == 'Z'): total_score += 6

  round_repl = [round[0].replace('A', 'X').replace('B', 'Y').replace('C', 'Z'), round[1]]
  if(round_repl[0] == 'X' and round_repl[1] == 'X'): total_score += 3
  if(round_repl[0] == 'X' and round_repl[1] == 'Z'): total_score += 2
  if(round_repl[0] == 'Y' and round_repl[1] == 'X'): total_score += 1
  if(round_repl[0] == 'Y' and round_repl[1] == 'Z'): total_score += 3
  if(round_repl[0] == 'Z' and round_repl[1] == 'X'): total_score += 2
  if(round_repl[0] == 'Z' and round_repl[1] == 'Z'): total_score += 1

print(total_score)

