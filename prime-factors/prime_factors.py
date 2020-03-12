import math as m

def factors(value):
  lst = []

  while value % 2 == 0:
    lst.append(2)
    value = value / 2

  #value must be  odd now

  for i in range(3,int(m.sqrt(value))+1,2):
    while value % i == 0:
      lst.append(i)
      value = value / i

  if value > 2:
    lst.append(int(value))
  print(lst)
  return lst