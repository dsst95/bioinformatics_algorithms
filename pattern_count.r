pattern_count <- function(text, pattern) {
  count <- 0
  pattern_length <- nchar(pattern)
  for (i in 0:(nchar(text) - pattern_length)) {
    if (substr(rep(text), i + 1, i + pattern_length) == pattern)
      count <- count + 1
  }
  return(count)
}

# message("Text")
# text <- scan("stdin", what="character", nlines=1)
# message("Pattern")
# pattern <- scan("stdin", what="character", nlines=1)

# print(pattern_count(text, pattern))
