def is_isogram(s):
  newS = "".join(i for i in s if i.isalpha())
  return len(set(newS.lower())) == len(newS.lower())
