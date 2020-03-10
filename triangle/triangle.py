#For a shape to be a triangle at all, all sides have to be of length > 0, and the sum of the lengths of any two sides must be greater than or equal to the length of the third side. See Triangle Inequality.

def equilateral(sides):
  return check_inequality(sides) and check_type(sides) == 1

def isosceles(sides):
  return check_inequality(sides) and check_type(sides) <= 2

def scalene(sides):
  return check_inequality(sides) and check_type(sides) == 3

def check_type(sides):
  return len(set(sides))

def check_inequality(sides):
  return all(i > 0 for i in sides) and sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]