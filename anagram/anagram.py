def find_anagrams(word, candidates):
  lst = []
  
  def is_anagram(w, e):
    #Make sure w != e
    w = w.lower()
    e = e.lower()

    if w == e:
      return False
    
    #Make sure every occurance of element exists in word
    return all([e.count(i) == w.count(i) for i in e])

  for el in candidates:
    if is_anagram(word, el):
      lst.append(el)
  
  return lst