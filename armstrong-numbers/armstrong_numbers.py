def is_armstrong_number(number):
  """
  #My original solution
  total = 0
  #1 - Find power
  pwr = len(str(number))

  #2 - Raise each digit to power
  for i in str(number):
    total += int(i)**pwr
  
  return total == number
  
  #Below is my one-line attempt for fun
  """
  return sum([int(i)**len(str(number)) for i in str(number)]) == number