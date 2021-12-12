file = open("day1input.txt").readlines()

#part one
new_list = []
day_1_example = [199,200,208,210,200,207,240,269,260,263]

for number in file:
  if '\n' in number:
    index = number.index('\n')
    number = number[:index]
    new_list.append(int(number))
  else:
    new_list.append(int(number))

def count(list):
  count = -1
  previous = 0
  for number in list:
    if number > previous:
      count +=1
      previous = number
    else:
      previous = number
  return count

#part two

if __name__ == '__main__':
  print(count(new_list))
  print(count(day_1_example))