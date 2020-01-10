class Box():
  def __init__(self, number):
    self.number = self.getNumber(number)

  def getNumber(self, number):
    #Make a blank list first, store all numbers in it
    blank = []
    for i in number:
      if i.isdigit():
        blank.append(i)
    #Check for errors, but also omit leading 1 if no errors
    if self.isValid(blank):
      if blank[0] == '1':
        return "".join(blank[1:])
      #No errors, no leading 1, return whole number
      return "".join(blank)
  
  def getAreaCode(self):
    return self.number[:3]

  def isValid(self, lst):
    if lst[0] == '0':
      raise ValueError("Invalid number")
    elif len(lst) != 11 and len(lst) != 10:
      raise ValueError("Invalid number")
    return True
