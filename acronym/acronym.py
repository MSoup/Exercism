import re

def abbreviate(words):
  
  chunked = re.split('[^a-zA-Z\']', words)
  filtered = [i for i in chunked if i != ""]

  return "".join(i.upper()[0] for i in filtered)