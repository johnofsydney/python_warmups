# 99 bottles of beer
# "99 Bottles of Beer" is a traditional reverse counting song.
# It is popular to sing on long trips, as it is repetitive and easy to memorise but - - it can take a long time to sing.
# Lets try and make it run a little quicker using code:
# The song's lyrics are as follows:
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down, pass it around, 98 bottles of beer on the wall...
# The same verse is repeated, each time with one bottle fewer, until there are none left.
# Bear in mind, not all verses are the same:
# The verse for 1 bottle is as follows:
# 1 bottle of beer on the wall, 1 bottle of beer.
# Take it down and pass it around, no more bottles of beer on the wall.
# The verse for 0 bottles is as follows:
# No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, 99 bottles of beer on the wall.
# Bonus:
# Count through any number of bottles.
# Be able to count between a range of numbers(ie, 20 to 10).

def beer_song(num1, num2):
  for num in range(num1, num2 - 1, -1):
    print(song_line(num))

  return "finished"

def song_line(num):
  print(num)
  line = ""
  if num > 2:
    line = f"{num} bottles of beer on the wall, {num} bottles of beer. Take one down, pass it around, {num - 1} bottles of beer on the wall"
  elif num == 2:
    line = f"{num} bottles of beer on the wall, {num} bottles of beer. Take one down, pass it around, {num - 1} bottle of beer on the wall"
  elif num == 1:
    line = f"{num} bottle of beer on the wall, {num} bottle of beer. Take one down, pass it around, no more bottles of beer on the wall"
  elif num == 0:
    line = f"No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall."

  return line

print(10, 0, beer_song(10,0))
