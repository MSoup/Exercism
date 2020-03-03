def score(word):
  score_map = {}
  for letter in ("A, E, I, O, U, L, N, R, S, T").split(", "):
    score_map[letter] = 1
  for letter in ("D, G").split(", "):
    score_map[letter] = 2
  for letter in ("B, C, M, P").split(", "):
    score_map[letter] = 3
  for letter in ("F, H, V, W, Y").split(", "):
    score_map[letter] = 4
  
  #Only one 5 point letter
  score_map["K"] = 5
  for letter in ("J, X").split(", "):
    score_map[letter] = 8
  for letter in ("Q, Z").split(", "):
    score_map[letter] = 10
  
  return sum(score_map[char] for char in word.upper())