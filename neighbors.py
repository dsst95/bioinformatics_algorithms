from hamming_distance import hamming_distance

def neighbors(pattern, d):
  neighborhood = [pattern]
  for j in range(1, d):
    for _pattern in neighborhood:
      neighbors = list(set(neighbors + immediate_neighbors(_pattern)))
  return neighborhood

def immediate_neighbors(pattern):
  neighborhood = [pattern]
  pattern_length = len(pattern)
  for i in range(1, pattern_length):
    symbol = pattern[i:i + 1]
    for x in ["A", "C", "G", "T"].remove(symbol):
      neighbor = pattern[0:i] + x + pattern[i + 1:pattern_length]
      neighborhood.append(neighbor)
  return neighborhood

if __name__ == "__main__":
  pattern = raw_input("Pattern: ")
  d = int(raw_input("D: "))
  print "\n".join(neighbors(pattern, d))
