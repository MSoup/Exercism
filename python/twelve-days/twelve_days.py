def recite(start_verse, end_verse):
  component = (['first','a Partridge in a Pear Tree.'],
              ['second','two Turtle Doves'],
              ['third','three French Hens'],
              ['fourth','four Calling Birds'],
              ['fifth','five Gold Rings'],
              ['sixth','six Geese-a-Laying'],
              ['seventh','seven Swans-a-Swimming'],
              ['eighth','eight Maids-a-Milking'],
              ['ninth','nine Ladies Dancing'],
              ['tenth','ten Lords-a-Leaping'],
              ['eleventh','eleven Pipers Piping'],
              ['twelfth','twelve Drummers Drumming'])

  
  #Helper function to build list of presents
  def get_song(parts):
    compile_presents = []

    if parts == 1:
      return 'a Partridge in a Pear Tree.'
    else:
      compile_presents.append(", ".join(present[parts-1:0:-1]))

    compile_presents.append(', and a Partridge in a Pear Tree.')

    return "".join(i for i in compile_presents)

  #Break into lists of days and presents
  day = [d[0] for d in component]
  present = [p[1] for p in component]

  song = []

  #For num in given start verse
  #Take index of component minus 1 since component index 0 is day 1
  for verse in range(start_verse, end_verse + 1):
    song.append(f'On the {day[verse-1]} day of Christmas my true love gave to me: {get_song(verse)}')

  return song