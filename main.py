def isIsogram(s):
  return len(set(s.lower())) == len(s.lower())

assert isIsogram("hello") == False
assert isIsogram("tomorrow") == False
assert isIsogram("anotherONE") == False
assert isIsogram("CAPSandSMALL") == False
assert isIsogram("") == True
assert isIsogram("another") == True
assert isIsogram("ANOTHER") == True
assert isIsogram("isogram") == True
assert isIsogram("AFK") == True
