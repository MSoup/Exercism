def recite(n, m):
  #Dict to make it easy to map number to day and phrase
  days = {
    1: ['first','a Partridge in a Pear Tree.'],
    2: ['second','two Turtle Doves'],
    3: ['third','three French Hens'],
    4: ['fourth','four Calling Birds'],
    5: ['fifth','five Gold Rings'],
    6: ['sixth','six Geese-a-Laying'],
    7: ['seventh','seven Swans-a-Swimming'],
    8: ['eighth','eight Maids-a-Milking'],
    9: ['ninth','nine Ladies Dancing'],
    10:['tenth','ten Lords-a-Leaping'],
    11: ['eleventh','eleven Pipers Piping'],
    12: ['twelfth','twelve Drummers Drumming']
  }

  #Helper function to generate list of phrases for corresponding day
  #Arg1: num, which represents the day (between n and m)
  #Arg2: days, pass whole dict to getPhrase
  def getPhrase(num, days):
    text = ""

    #Count downwards from num to create descending lyrics
    for i in range(num,0,-1):
      #Add "and" if we reach 1
      if i == 1:
        text += "and " + days[i][1]
      else:
      #Else, continue appending to the lyrics
        text += days[i][1] + ", "
    return text

  #For purposes of answering the question, make a list to store answer
  answer = []

  for i in range(n, m+1):
    #Cover the first case where n == 1, this ensures that "and" will never be added to the first day of Christmas
    if n == 1:
      return ['On the ' + days[i][0] + ' day of Christmas my true love gave to me: ' + days[i][1]]
    #If it's not day 1, then call helper function to generate lyrics and append "and" to the last lyric
    else:
      answer.append('On the ' + days[i][0] + ' day of Christmas my true love gave to me: ' + getPhrase(i, days))
  
  return answer