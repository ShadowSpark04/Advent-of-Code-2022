with open('Day 11/Input_11.txt') as f:
  lines = f.read().split('\n')

monkey_lines = []
monkeys = []

for i in range(0, len(lines), 7):
  monkey_lines.append(lines[i:i+6])

for monkey in monkey_lines:
  temp_monkey = []
  temp_monkey.append(monkey[1][18:].split(', '))
  temp_monkey.append(monkey[2][19:])
  temp_monkey.append(int(monkey[3][21:]))
  temp_monkey.append(int(monkey[4][29:]))
  temp_monkey.append(int(monkey[5][30:]))
  temp_monkey[0] = [int(temp_monkey[0][i]) for i in range(len(temp_monkey[0]))]
  temp_monkey.append([])
  temp_monkey.append(0)
  monkeys.append(temp_monkey)

def operate(a, b, op):
  if(op == '+'): return a + b
  if(op == '-'): return a - b
  if(op == '*'): return a * b
  if(op == '/'): return a / b

def throw(monkey, item):
  monkey[5].append(item)

def find_new_value(op, item):
  op_symbol = ''
  first = 0
  second = 0
  if('old' in op[:op.index(' ')]):
      first = item
  else:
    first = op[:op.index(' ')]
  if('old' in op[op.index(' ') + 3:]):
    second = item
  else:
    second = int(op[op.index(' ') + 3:])
  op_symbol = op[op.index(' ') + 1]
  return operate(first, second, op_symbol)

def evaluate(item, num):
  if(item % num == 0):
    return True
  else:
    return False

modulo = 1
for monkey in monkeys:
    modulo *= monkey[2]

def do_action(monkey):
  monkey[0] = monkey[0][:] + monkey[5][:]
  monkey[5] = []
  for item in monkey[0]:
    monkey[6] += 1
    op = monkey[1]
    throwing = False
    new_worry = int(find_new_value(op, item) % modulo)
    throwing = evaluate(new_worry, monkey[2])
    if(throwing):
      throw(monkeys[monkey[3]], new_worry)
    else:
      throw(monkeys[monkey[4]], new_worry)
  monkey[0] = []

for i in range(10000):
  for monkey in monkeys:
    do_action(monkey)


totals = []
for monkey in monkeys:
  # print(monkey)
  totals.append(monkey[6])
  
totals.sort()
print(totals)
print(totals[-2] * totals[-1])

