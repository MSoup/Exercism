def steps(number):
  count = 0
  if number < 1:
    raise ValueError("Invalid number")
  
  while number != 1:
    count += 1
    if number % 2 == 0:
      number = number / 2
    else:
      number = (number * 3) + 1
  return count