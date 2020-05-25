def equilateral(sides):
<<<<<<< HEAD
  return (all(sides[i] == sides[i+1] for i in range(len(sides)-1))) and (0 not in sides)

def isosceles(sides):
  return (count(sides[i]) == 2 for i in range(len(sides)))


def scalene(sides):
  pass
=======
  return check_inequality(sides) and check_type(sides) == 1

def isosceles(sides):
  return check_inequality(sides) and check_type(sides) <= 2

def scalene(sides):
  return check_inequality(sides) and check_type(sides) == 3

def check_type(sides):
  return len(set(sides))

def check_inequality(sides):
  return all(i > 0 for i in sides) and sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]
>>>>>>> d5e9ce3aae02598ab44d3dd0c1eb9c88876935c5
