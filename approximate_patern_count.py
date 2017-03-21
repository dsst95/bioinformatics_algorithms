from hamming_distance import hamming_distance

def approximate_pattern_count(text, pattern, d):
  count = 0
  pattern_length = len(pattern)
  for i in range(0, len(text) - pattern_length + 1):
    _pattern = text[i:i + pattern_length]
    if (hamming_distance(pattern, _pattern) <= d):
      count += 1
  return count


if __name__ == "__main__":
  text = raw_input("Text: ")
  pattern = raw_input("Pattern: ")
  d = int(raw_input("D: "))
  print approximate_pattern_count(text, pattern, d)
