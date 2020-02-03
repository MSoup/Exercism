def slices(series, length):
  lst = []
  if length > len(series) or length < 1:
    raise ValueError("Please choose an appropriate length")

  for i in range(len(str(series))-length+1):
    lst.append(series[i:i+length])

  return lst