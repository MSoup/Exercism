def equilateral(sides):
  return (all(sides[i] == sides[i+1] for i in range(len(sides)-1))) and (0 not in sides)

def isosceles(sides):
  return (count(sides[i]) == 2 for i in range(len(sides)))


def scalene(sides):
  pass
