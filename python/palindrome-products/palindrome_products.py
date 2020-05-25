def largest(min_factor, max_factor):
  #Error if start > end
  if min_factor > max_factor:
    raise ValueError("Min > max range")

  #Keep track of highest product
  highest, values = None, []

  #Get every possible product from min*min to max*max
  for num in range(min_factor,max_factor+1):
    for combination in range(min_factor,max_factor+1):
      #Check product for palindrome
      test_num = str(num*combination)

      if test_num == test_num[::-1]:
        #Palindrome found, set palindrome to highest or set new highest, else pass
        if highest == None or int(test_num) > highest:
          highest = int(test_num)
          values = [num, combination]
        if int(test_num) == highest:
          values.append([num, combination])
  
  #Clean up unnested duplicates
  factor = []
  for singles in values:
    if isinstance(singles, list):
      factor.append(singles)

  return highest, factor

def smallest(min_factor, max_factor):
  #Error if start > end
  if min_factor > max_factor:
    raise ValueError("Min > max range")

  #Keep track of smallest product
  lowest, values = None, []

  #Get every possible product from min*min to max*max
  for num in range(min_factor,max_factor+1):
    for combination in range(min_factor,max_factor+1):
      #Check product for palindrome
      test_num = str(num*combination)

      if test_num == test_num[::-1]:
        #Palindrome found, set palindrome to lowest or set new lowest, else pass
        if lowest == None or int(test_num) < lowest:
          lowest = int(test_num)
          values = [num, combination]
        if lowest == int(test_num):
          values.append([num, combination])

  #Clean up unnested duplicates
  factor = []
  for singles in values:
    if isinstance(singles, list):
      factor.append(singles)

  return lowest, factor
