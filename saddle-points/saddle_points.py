def saddle_points(matrix):
  matrix = [[4, 5, 4], 
            [3, 5, 5], 
            [1, 5, 4]]

#For a saddle point to exist, it must be the highest number in its row, but also the lowest number in its compile
  possible_saddle = []
  for i, row in enumerate(matrix):
    print(f'Looking at row {i+1}')
    print(row)
    biggest_row_num = max(row)
    for col, el in enumerate(row):
      print(f'Looking at column {col+1}: {el}')
      if el == biggest_row_num:
        print(f'{el} is the biggest in row {i+1}')
        possible_saddle.append({"row":i+1, "column": col+1})
  return print(possible_saddle)
