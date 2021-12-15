file = open('day2input.txt').readlines()

given = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

def clean(file):
  new_list = []
  for number in file:
    if '\n' in number:
      index = number.index('\n')
      number = number[:index]
      number = number.split(' ')
      new_list.append(number)
    else:
      number = number.split(' ')
      new_list.append(number)
  return new_list

#Part 1
def sum1(l):
  position = 0
  depth = 0
  for x in l:
    if x[0] == 'forward':
      position = position + int(x[-1])
    elif x[0] == 'down':
      depth = depth + int(x[-1])
    elif x[0] == 'up':
      depth = depth - int(x[-1])
  return position*depth

#Part 2
def sum2(l):
  position = 0
  depth = 0
  aim = 0
  for x in l:
    if x[0] == 'forward':
      position = position + int(x[-1])
      depth = depth + (aim * int(x[-1]))
    elif x[0] == 'down':
      aim = aim + int(x[-1])
    elif x[0] == 'up':
      aim = aim - int(x[-1])
  return position*depth

if __name__ == '__main__':
  #Part one
  print(sum1(clean(given)))
  print(sum1(clean(file)))
  #Part two
  print(sum2(clean(given)))
  print(sum2(clean(file)))