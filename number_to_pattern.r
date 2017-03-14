number_to_symbol <- function(number) {
  if (number == 0) return("A")
  if (number == 1) return("C")
  if (number == 2) return("G")
  if (number == 3) return("T")
}

number_to_pattern <- function(index, k) {
  if (k == 1)
    return(number_to_symbol(index))
  prefixIndex <- index %/% 4
  r <- index %% 4
  symbol <- number_to_symbol(r)
  return(paste(number_to_pattern(prefixIndex, k - 1), symbol, sep = ""))
}


# message("Index")
# index <- scan("stdin", nlines=1)
# message("k")
# k <- scan("stdin", nlines=1)
# 
# print(number_to_pattern(index, k))
