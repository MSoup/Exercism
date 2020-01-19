def square_of_sum(number):
    return int(((number * (number + 1)) / 2)**2)
    
def sum_of_squares(number):
    return int((number * (number + 1) * (2 * number + 1)) / 6)

def difference_of_squares(number):
    return abs(square_of_sum(number) - sum_of_squares(number))


#Thanks Carl Friedrich Gauss