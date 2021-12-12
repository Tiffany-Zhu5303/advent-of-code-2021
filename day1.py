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
  numbers = l
  total = []
  for number in numbers:
    index = numbers.index(number)
    if index < len(numbers) - 2:
      total.append(sum(l[index:index+3]))
      numbers[index] = 0
  return total



if __name__ == '__main__':
  print('part one')
  print('input given:', count(new_list))
  print('example given:', count(day_1_example), "\n")
  print('part two')
  print('example given:', count(total_sum(day_1_example)))
  print('input given:', count(total_sum(new_list))) 