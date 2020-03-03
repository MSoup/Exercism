def build_dict():
    score_map = {}
    for letter in ("A, E, I, O, U, L, N, R, S, T").split(", "):
        score_map[letter] = 1
    for letter in ("D, G").split(", "):
        score_map[letter] = 2
    for letter in ("B, C, M, P").split(", "):
        score_map[letter] = 3
    for letter in ("F, H, V, W, Y").split(", "):
        score_map[letter] = 4        
        score_map["K"] = 5
    for letter in ("J, X").split(", "):
        score_map[letter] = 8
    for letter in ("Q, Z").split(", "):
        score_map[letter] = 10
    return score_map
    

def score(word):
    #Build dictionary of letters and corresponding values as lazily as I can
    letter_value = build_dict()

    score = 0
    if not word:
        return score
    else:
        return sum([letter_value[char.upper()] for char in word]) 
