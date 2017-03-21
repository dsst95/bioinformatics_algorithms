def number_to_symbol(number):
  if (number == 0): return "A"
  if (number == 1): return "C"
  if (number == 2): return "G"
  if (number == 3): return "T"


def number_to_pattern(index, k):
  if (k == 1):
    return number_to_symbol(index)
  prefix_index = index / 4
  r = index % 4
  symbol = number_to_symbol(r)
  return number_to_pattern(prefix_index, k - 1) + symbol
