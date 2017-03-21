from neighbors import neighbors
from pattern_to_number import pattern_to_number
from number_to_pattern import number_to_pattern

def frequent_words_with_mismatches(text, k, d):
  frequent_patterns = []
  neighborhoods = []
  index = []
  count = []
  for i in range(0, len(text) - k):
    neighborhoods.append(neighbors(text[i:i + k], d))
  neighborhoods_array = [item for sublist in neighborhoods for item in sublist]
  for i in range(0, len(neighborhoods)):
    index.append(pattern_to_number(neighborhoods_array[i]))
    count.append(1)
  sorted_index = sorted(index)
  for i in range(0, len(neighborhoods) - 2):
    if (sorted_index[i] == sorted_index[i + 1]):
      count[i + 1] = count[i] + 1
  max_count = max(count)
  for i in range(0, len(neighborhoods) - 1):
    if count[i] == max_count:
      pattern = number_to_pattern(sorted_index[i], k)
      frequent_patterns.append(pattern)
  return frequent_patterns

if __name__ == "__main__":
  text = raw_input("Text: ")
  k, d = map(int, raw_input("K / D: ").split(" "))
  print " ".join(frequent_words_with_mismatches(text, k, d))
