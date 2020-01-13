class PhoneNumber:
  def __init__(self, number):
    self.number = self.getCleanNumber(number)
    self.area_code = self.number[:3]
    self.exchange_code = self.number[3:6]
    self.rest = self.number[6:]

  def getCleanNumber(self, number):
    cleaned = ""
    for i in number:
      if i.isdigit():
        cleaned += i
    
    #Check first digit
    if cleaned[0] == '1':
      if self.checkValidity(cleaned[1:]):
        return cleaned[1:]
    
    else:
      if self.checkValidity(cleaned):
        return cleaned

  
  def checkValidity(self, number):
    #Is area code + exchange code + the rest 10 digits?
    if len(number) != 10:
      raise ValueError('Invalid number')
    #Valid area code?
    elif number[0] in '01':
      raise ValueError('Invalid number')
    #Valid exchange code?
    elif number[3] in '01':
      raise ValueError('Invalid number')

    return True


  def pretty(self):
    return f"({self.area_code}) {self.exchange_code}-{self.rest}"