class Allergies:

    def __init__(self, score):
      self.score_list = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
      }
      self.score = score

    def allergic_to(self, item):
      return '1' in bin(self.score_list[item] & (self.score))

    @property
    def lst(self):
        pass