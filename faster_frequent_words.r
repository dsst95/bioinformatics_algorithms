source("computing_frequencies.r")
source("number_to_pattern.r")

faster_frequent_words <- function(text, k) {
  frequent_patterns <- {}
  frequency_array <- computing_frequencies(text, k)
  max_count <- max(frequency_array)
  for (i in 0:(4^k-1)) {
    if (frequency_array[i + 1] == max_count) {
      pattern <- number_to_pattern(i, k)
      frequent_patterns <- append(frequent_patterns, pattern)
    }
  }
  return(frequent_patterns)
}




message("Text")
text <- scan("stdin", what="character", nlines=1)
message("K")
k <- scan("stdin", nlines=1)

print(faster_frequent_words(text, k))

