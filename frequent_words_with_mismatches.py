from computing_frequencies_with_mismatches import computing_frequencies_with_mismatches
from number_to_pattern import number_to_pattern

def frequent_words_with_mismatches(text, k, d):
  frequent_patterns = []
  frequency_array = computing_frequencies_with_mismatches(text, k, d)
  max_count = max(frequency_array)
  for i in range(0, 4**k - 1):
    if frequency_array[i] == max_count:
      pattern = number_to_pattern(i, k)
      frequent_patterns.append(pattern)
  return frequent_patterns

if __name__ == "__main__":
  text = raw_input("Text: ")
  k, d = map(int, raw_input("K / D: ").split(" "))
  print " ".join(frequent_words_with_mismatches(text, k, d))
