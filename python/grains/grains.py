def square(number):
  if number < 1 or number > 64:
    raise ValueError("Invalid number")

  return 2**(number-1)

def total():
  return sum(square(i) for i in range(1,65))
