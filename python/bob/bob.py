# Bob is a lackadaisical teenager. In conversation, his responses are very limited.

# Bob answers 'Sure.' if you ask him a question, such as "How are you?".

# He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).

# He answers 'Calm down, I know what I'm doing!' if you yell a question at him.

# He says 'Fine. Be that way!' if you address him without actually saying
# anything.

# He answers 'Whatever.' to anything else.

def response(hey_bob):
  hey_bob = hey_bob.strip()

  if not hey_bob:
    return 'Fine. Be that way!'
  elif yell_question(hey_bob):
    return "Calm down, I know what I'm doing!"
  elif yell(hey_bob):
    return 'Whoa, chill out!'
  elif question(hey_bob):
    return 'Sure.'
  else:
    return "Whatever."

def yell_question(txt):
  return txt == txt.upper() and txt[-1] == '?' and any(i.isalpha() for i in txt)

def yell(txt):
  return txt == txt.upper() and any(i.isalpha() for i in txt)

def question(txt):
  return txt[-1] == "?"