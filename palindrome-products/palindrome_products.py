"""
Example 1
Given the range [1, 9] (both inclusive)...

And given the list of all possible products within this range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 15, 21, 24, 27, 20, 28, 32, 36, 25, 30, 35, 40, 45, 42, 48, 54, 49, 56, 63, 64, 72, 81]

The palindrome products are all single digit numbers (in this case): [1, 2, 3, 4, 5, 6, 7, 8, 9]

The smallest palindrome product is 1. Its factors are (1, 1). The largest palindrome product is 9. Its factors are (1, 9) and (3, 3).
"""

def largest(min_factor, max_factor):
  #Error if start > end
  if min_factor > max_factor:
    raise ValueError("Yooo")
  #Keep track of highest product
  highest_product, value = 0, []

  for end in range(max_factor,min_factor-1,-1):
    for possible_products in range(end, min_factor-1,-1):
      #Check that a product is a palindrome
      if str(end * possible_products) == str(end * possible_products)[::-1]:
        #Check that the palindrome is the highest
        if end * possible_products > highest_product:
          highest_product = end * possible_products
          value = [end, possible_products]

  #Return highest number in desired format, else return None if empty
  if highest_product == 0:
    return None
  else:
    return highest_product, value

def smallest(min_factor, max_factor):
  #Error if start > end
  if min_factor > max_factor:
    raise ValueError
  #Build list of possible palindromes
  palindromes = {}
    
  for start in range(min_factor,max_factor+1):
    for possible_products in range(start, max_factor+1):
      if str(start * possible_products) == str(start * possible_products)[::-1]:
        #Append to dict
        palindromes[start * possible_products] = [start, possible_products]

  #Get lowest number now that dict is constructed
  lowest_palindrome = min(palindromes)
  #Return lowest number in desired format, else return None if empty
  if lowest_palindrome:
    return lowest_palindrome, palindromes[lowest_palindrome]
  return None

