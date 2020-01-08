def convert(number):
    text = ""
    if number % 3 == 0:
        text += "Pling"
    if number % 5 == 0:
        text += "Plang"
    if number % 7 == 0:
        text += "Plong"

    return text if text.isalpha() else str(number)