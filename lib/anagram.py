class Anagram:
  def __init__(self, word):
    self.word_sorted = sorted(word.lower())  # Pre-sort the word for efficiency

  def is_anagram(self, word):
    return sorted(word.lower()) == self.word_sorted  # Compare sorted letters

  def match(self, words):
    return [word for word in words if self.is_anagram(word)]  # Use is_anagram method