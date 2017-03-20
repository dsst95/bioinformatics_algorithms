from hamming_distance import hamming_distance

def pattern_matching(pattern, genome, d):
  pattern_length = len(pattern)
  pos = []
  for i in range(0, len(genome) - pattern_length + 1):
    _pattern = genome[i:i + pattern_length]
    if (hamming_distance(pattern, _pattern) <= d):
      pos.append(i)
  return pos


if __name__ == "__main__":
  filename = raw_input("Enter a file name: ")
  f = open(filename, "r")
  pattern = f.readline().rstrip('\r\n')
  genome = f.readline().rstrip('\r\n')
  d = int(f.readline())
  " ".join(map(str, pattern_matching(pattern, genome, d)))
