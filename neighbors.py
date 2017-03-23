from hamming_distance import hamming_distance

def immediate_neighbors(pattern):
  neighborhood = [pattern]
  pattern_length = len(pattern)
  for i in range(0, pattern_length):
    symbol = pattern[i:i + 1]
    nucleodits = ["A", "C", "G", "T"]
    nucleodits.remove(symbol)
    for x in nucleodits:
      neighbor = pattern[0:i] + x + pattern[i + 1:pattern_length]
      neighborhood.append(neighbor)
  return neighborhood

def neighbors(pattern, d):
  neighborhood = [pattern]
  for j in range(0, d):
    for _pattern in neighborhood:
      neighborhood = list(set(neighborhood + immediate_neighbors(_pattern)))
  return neighborhood

if __name__ == "__main__":
  pattern = raw_input("Pattern: ")
  d = int(raw_input("D: "))
  print "\n".join(neighbors(pattern, d))
