# Write a program that, given a word, computes the scrabble score for that word.

# scrabble("cabbage")
# # => 14
# Letter Values
# Letter                           Value
# A, E, I, O, U, L, N, R, S, T       1
# D, G                               2
# B, C, M, P                         3
# F, H, V, W, Y                      4
# K                                  5
# J, X                               8
# Q, Z                               10


# Version 2: 
# each letter score is an integer and the correspnding letters are
# a list which is all the letters with that score.
LETTER_SCORES = {
  1: "A E I O U L N R S T".split(),
  2: "D G".split(),
  3: "B C M P".split(),
  4: "F H V W Y".split(),
  5: ["K"],
  8: "J X".split(),
  10: "Q Z".split()
}

def scrabble(word):
  word = word.upper()
  letter_scores = transpose(LETTER_SCORES)
  score = 0

  for letter in word:
    score = score + letter_scores[letter]

  return score


def transpose(original):
  result = {}
  for score in original:
    for letter in original[score]:
      result[letter] = score
  
  return result



print(scrabble('cabbage'))
print(scrabble('CABBAGE'))
print(scrabble('cAbBaGe'))

# Version 1 each lwetter is a KEY, each letter's score is the VALUE
# LETTER_SCORES = {
#   "A": 1,
#   "E": 1,
#   "G": 2,
#   "B": 3,
#   "C": 3
# }

# def scrabble(word):
#   score = 0
#   for letter in word.upper():
#     score = score + LETTER_SCORES[letter]

#   return score

# print(scrabble('cabbage'))