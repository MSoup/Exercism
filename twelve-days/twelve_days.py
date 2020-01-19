def recite(n, m):
  days = {
    1: 'first',
    2: 'second',
    3: 'third',
    4: 'fourth',
    5: 'fifth',
    6: 'sixth',
    7: 'seventh',
    8: 'eigth',
    9: 'nineth',
    10: 'tenth',
    11: 'eleventh',
    12: 'twelfth'
  }

  phrases = {
    12: 'twelve Drummers Drumming',
    11: 'eleven Pipers Piping',
    10:'ten Lords-a-Leaping',
    9: 'nine Ladies Dancing',
    8: 'eight Maids-a-Milking',
    7: 'seven Swans-a-Swimming',
    6: 'six Geese-a-Laying',
    5: 'five Gold Rings',
    4: 'four Calling Birds',
    3: 'three French Hens',
    2: 'two Turtle Doves',
    1: 'a Partridge in a Pear Tree.'
  }

  remember = []
  for i in range(1,n):
    if i == 1:
      print('On the ' + days[i] + ' day of Christmas my true love gave to me: ' + phrases[i])
      remember.insert(0, 'and ' + phrases[i])

    else:
      print('On the ' + days[i] + ' day of Christmas my true love gave to me: ' + phrases[i], end = ", ", flush=True) 
      print(*remember)
      remember.insert(0, phrases[i] + ',')
      print()
      
  return remember