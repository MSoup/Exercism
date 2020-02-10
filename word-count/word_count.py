from string import punctuation
import re

def count_words(sentence):
  catalog = {}
  #Split on any special character
  words = re.split(r"[^A-Za-z0-9']", sentence)

  #Punctuation includes all except apostrophe
  punc = set(punctuation) - {"'"}

  def cleaned(word):
    #Remove punctuation except apostrophe
    word = "".join([char for char in word if char not in punc])
    #Remove leading / trailing apostrophe
    word = word.strip(punctuation)
    #Return word in lower case (returning empty possible)
    return word.lower()

  for word in words:
    #Filter word
    check_word = cleaned(word)
    #Check against dict to build it; ignore empty check_word
    if not check_word:
      pass
    elif check_word in catalog:
      catalog[check_word] += 1
    else:
      catalog[check_word] = 1

  return catalog