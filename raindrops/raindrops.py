def raindrops(number):
  result = ""
  if divisible_by_three(number):
    result += "pling"
  if divisible_by_five(number):
    result += "plang"
  if divisible_by_seven(number):
    result += "plong"
  if (result == ""):
    result = str(number)
  return result



def divisible_by_three(number):
  return (number % 3 == 0)

def divisible_by_five(number):
  return (number % 5 == 0)

def divisible_by_seven(number):
  return (number % 7 == 0)

print(2, raindrops(2))
print(3, raindrops(3))
print(5, raindrops(5))
print(7, raindrops(7))
print(17, raindrops(17))
print(28, raindrops(28))
print(35, raindrops(35))
print(365, raindrops(365))
