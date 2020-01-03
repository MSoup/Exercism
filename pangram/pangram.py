def is_pangram(sentence):
    collect = {chr(97+i): 0 for i in range(26)}
    for i in sentence:
        if i.isalpha():
            collect[i.lower()] += 1
    return all([collect[chr(97+i)] > 0 for i in range(26)])
    