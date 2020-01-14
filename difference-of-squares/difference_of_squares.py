"""
Introduction
Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.

The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025.

The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385.

Hence the difference between the square of the sum of the first ten natural numbers and the sum of the squares of the first ten natural numbers is 3025 - 385 = 2640.

You are not expected to discover an efficient solution to this yourself from first principles; research is allowed, indeed, encouraged. Finding the best algorithm for the problem is a key skill in software engineering.
"""

def squareDiff(n):
  sumSquares = 0
  squareSum = 0
  for i in range(1,n+1):
    #Take squares first and add
    sumSquares += i**2
    #Take sum first, square outside the loop
    squareSum += i
  
  squareSum = squareSum ** 2

  return abs(sumSquares - squareSum)
