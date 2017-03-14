symbol_to_number <- function(symbol) {
  switch(
    symbol,
    A = 0,
    C = 1,
    G = 2,
    T = 3
  )
}

pattern_to_number <- function(pattern) {
  pattern_length <- nchar(pattern)
  if (pattern_length == 0)
    return(0)

  symbol <- substr(pattern, pattern_length, pattern_length + 1)
  prefix <- substr(pattern, 0, pattern_length - 1)
  return(4 * pattern_to_number(prefix) + symbol_to_number(symbol))
}


# message("Pattern")
# pattern <- scan("stdin", what="character", nlines=1)
# 
# print(pattern_to_number(pattern))
