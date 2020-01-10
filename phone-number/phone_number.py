class Box():
  def __init__(self, number):
    self.number = self.getNumber(number)

  def getNumber(self, number):
    blank = []
    for i in number:
      if i.isdigit():
        blank.append(i)

    if blank[0] == '1':
      return "".join(blank[1:])
    elif blank[0] == '0' or len(blank) != 10:
      raise ValueError("Invalid number")
    
    return "".join(blank)




x = Box("1-519.437-2526")

x.number
