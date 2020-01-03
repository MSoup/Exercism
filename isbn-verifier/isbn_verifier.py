def is_valid(isbn):
    #Convert to list
    strippedISBN = [i for i in isbn if i.isdigit()]
    #Check last digit
    if isbn and isbn[-1] in "xX":
      strippedISBN.append(10)

    #Can't let code continue if len != 10
    if len(strippedISBN) != 10:
      return False

    total = 0
    for i, j in enumerate(range(10,0,-1)):
      total += int(strippedISBN[i]) * j

    return total % 11 == 0