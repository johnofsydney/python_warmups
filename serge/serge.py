def serge(input):
  if says_nothing(input):
    return 'Fine. Be that way!'
  if is_a_question(input):
    return 'Sure.'
  if is_all_caps(input):
    return 'Woah, chill out!'
  return 'Whatever'

def is_a_question(input):
  return (input[-1] == '?')

def is_all_caps(input):
  return( input.isupper() )

def says_nothing(input):
  return ( input == '' )


print('foo', serge('foo'))
print('this is a question?', serge('this is a question?'))
print('YELLING', serge('YELLING'))
print('empty', serge(''))
print('learning python', serge('learning python'))
