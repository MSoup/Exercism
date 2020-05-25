def classify(number):
  if number < 1:
    raise ValueError("Please give me a natural number")
    
  factorLst = []

  for i in (range(1,number//2 + 1)):
    if number % i == 0:
      factorLst.append(i)

  total = sum(factorLst)

  if total == number:
    return "perfect"
  elif total < number:
    return "deficient"
  else:
    return "abundant"
  

