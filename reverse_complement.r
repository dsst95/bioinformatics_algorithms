complement <- function(p) {
  switch(
    p,
    A = "T",
    C = "G",
    G = "C",
    T = "A"
  )
}

reverse_complement <- function(pattern) {
  p <- ""
  for (i in 0:nchar(pattern)) {
    p <- paste(complement(substr(pattern, i + 1, i + 1)), p, sep = "")
  }
  return (p)
}

message("File")
file <- scan("stdin", what="character", nlines=1)
pattern <- scan(file, what="character", nlines=1)
cat(reverse_complement(pattern))
