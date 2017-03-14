source("pattern_to_number.r")

computing_frequencies <- function(text, k) {
  frequency_array <- array(0, 4^k)
  for(i in 0:(nchar(text) - k)) {
    pattern <- substr(text, i + 1, i + k)
    j <- pattern_to_number(pattern)
    frequency_array[j + 1] <- frequency_array[j + 1] + 1
  }
  return(frequency_array)
}


# message("Text")
# text <- scan("stdin", what="character", nlines=1)
# message("k")
# k <- scan("stdin", nlines=1)
# 
# cat(computing_frequencies(text, k))
