def slices(series, length):
  lst = []
  if length > len(series) or length < 1:
    raise ValueError("Please choose an appropriate length")

  for i in range(len(str(series))-length+1):
    lst.append(series[i:i+length])

  return lst



print(slices("918493904243", 5))


#["91849", "18493", "84939", "49390", "93904", "39042", "90424", "04243"],

#["91", "14", "42"])