source("pattern_count.r")

kmer <- function(text, k) {
  frequent_patterns <- {}
  count <- {}
  for (i in 0:(nchar(text) - k)) {
    pattern <- substr(text, i + 1, i + k)
    count[i + 1] <- pattern_count(text, pattern)
  }
  max_count <- max(count)
  for (i in 0:(nchar(text) - k)) {
    if (count[i + 1] == max_count)
      frequent_patterns <- append(frequent_patterns, substr(text, i + 1, i + k))
  }
  return(unique(frequent_patterns))
}




message("Text")
text <- scan("stdin", what="character", nlines=1)
message("K")
k <- scan("stdin", nlines=1)

print(kmer(text, k))

