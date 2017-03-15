pattern_matching <- function(pattern, genome) {
  pattern_length <- nchar(pattern)
  for (i in 0:nchar(genome) - pattern_length) {
    if (substr(genome, i + 1, i + pattern_length) == pattern)
      print(i)
  }
}


message("File")
file <- scan("stdin", what="character", nlines=1)
pattern <- scan(file, what="character", nlines=1)
genome <- scan(file, what="character", skip=1, nlines=1)

pattern_matching(pattern, genome)
