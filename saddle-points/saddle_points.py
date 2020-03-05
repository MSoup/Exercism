def saddle_points(matrix):
  for i in matrix:
    if len(i) != len(matrix[0]):
      raise ValueError("Irregular matrix")

  #Store Candidates for Saddle Points
  result_list = []
  for row_count in range(len(matrix)):

    row = matrix[row_count]
    #max(row) is the number that will guarantee candidates since no other numbers will fulfill highest in row
    row_candidate = max(row)
    #Get index of all candidates
    for i, num in enumerate(row):
      #Highest num found
      if num == row_candidate:
        #Append index of num
        result_list.append([row_count, i])

  #True if a coordinate is less than or equal to all el in col
  def test_candidate(row, col):
    if all(matrix[row][col] <= i[col] for i in matrix):
      return True
    return False

  results = []

  for candidate in result_list:
    #Send coordinates to be tested against matrix
    #test_candidate: row, col
    if test_candidate(candidate[0], candidate[1]):
      #These are true saddle points, +1 to row/col index for human readable output
      results.append({"row": candidate[0]+1, "column": candidate[1]+1})

  return results