# Anagram Detector
# Write a program that, given a word and a list of possible anagrams, selects the anagrams of the given word.

# In other words, given: "listen" and ["enlists" "google" "inlets" "banana"] the program should return "inlets".

# equivalent of require 'pry'
import code

def detector(array, word):
  results = []

  # equivalent of binding.pry
  # code.interact(local=dict(globals(), **locals()))

  for candidate in array:
    if are_anagrams(candidate, word):
      results.append(candidate)

  return results

def are_anagrams(word1, word2):
  W1 = "".join(sorted(word1.upper()))
  W2 = "".join(sorted(word2.upper()))

  return W1 == W2


print(detector(["enlists", "google", "inlets", "banana"], "listen"))
print(detector(["enlists", "google", "inlets", "banana", "listen", "nestli"], "listen"))
