given = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

'''Find power consumption of submarine:
power consumption = gamma ray * epsilon rate
gamma ray = most common bit in the corresponding position'''

file = open("day3input.txt").readlines()

def clean(file):
  new_list = []
  for number in file:
    #print('this is the number', number)
    if '\n' in number:
      index = number.index('\n')
      number = number[:index]
      new_list.append(number)
    else:
      new_list.append(number)
  return new_list

#finds whether 0 or 1 is more common in a column
def loop(l):
  zero = 0
  one = 0

  for number in l:
    #print(number)
    if number[0] == '1':
      one += 1
      number = number[1:]
      #print(number, '\n')
    elif number[0] == '0':
      zero += 1
      number = number[1:]
      #print(number, '\n')

  if zero > one:
    return '0'
  else:
    return '1'

#outputs the new binary number
def each_term(l):
  newbinary = ''
  newbinary = newbinary + loop(l)
  
  newlist = []

  for term in l:
      term = term[1:]
      newlist.append(term)

  while len(newlist[0]) > 0:
    newbinary = newbinary + loop(newlist)
    for term in newlist:
      newterm = term[1:]
      index = newlist.index(term)
      newlist[index] = newterm
  return newbinary

def add (l): 
  total = 0
  for n in l:
    total = total + n
  return total

def binary_to_decimal(binary):
  base = 2
  length = len(binary)
  decimal_list = []
  l = []
  for n in binary:
    l.append(n)
    if n == '1':
      index = l.index(n)
      position = len(binary) - index - 1
      decimal = 1 * (base ** position)
      l[index] = '0'
      decimal_list.append(decimal)
  return add(decimal_list)


if __name__ == '__main__':
  print('new binary of given:',each_term(given))
  print('new binary of input text:',len(each_term(clean(file))), len(file[0]))
  print('decimal of given:',binary_to_decimal(each_term(given)))
  print('decimal of input text:',binary_to_decimal(each_term(clean(file))))