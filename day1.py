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

def count(l):
  count = -1
  previous = 0
  for number in l:
    if number > previous:
      count +=1
      previous = number
    else:
      previous = number
  return count

#part two
def total_sum(l):
  total = []
  for number in l:
    index = l.index(number)
    if index < len(l) - 2:
      total.append(sum(l[index:index+3]))
  return total



if __name__ == '__main__':
  #part one
  print(count(new_list))
  print(count(day_1_example))
  #part two
  print(count(total_sum(day_1_example)))
  print(count(total_sum(new_list))) #not 1731