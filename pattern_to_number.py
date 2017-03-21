def symbol_to_number(symbol):
  if symbol == "A":
    return 0
  elif symbol == "C":
    return 1
  elif symbol == "G":
    return 2
  elif symbol == "T":
    return 3

def pattern_to_number(pattern):
  pattern_length = len(pattern)
  if pattern_length == 0:
    return 0

  symbol = pattern[pattern_length - 1:pattern_length]
  prefix = pattern[0:pattern_length - 1]
  return 4 * pattern_to_number(prefix) + symbol_to_number(symbol)
