class Matrix:
    def __init__(self, matrix_string):
        #Split string into list
        strList = matrix_string.split("\n")
        #Split list into lists of elements for easy indexing
        self.matrix = [i.split() for i in strList]
        
    def row(self, index):
        #Convert to int and display row
        return [int(i) for i in self.matrix[index-1]]

    def column(self, index):
        #Convert to int and display columns (= row[index])
        return [int(i[index-1]) for i in self.matrix]