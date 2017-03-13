library(Brobdingnag)

factorial <- function(n) {
  if (n <= 1)
    return(1)

  return(n * factorial(n - 1))
}

binomial_coefficient <- function(m, k) {
  return(factorial(m)/(factorial(k)*factorial(m-k)));
}

message("m")
m <- scan("stdin", nlines=1)
message("k")
k <- scan("stdin", nlines=1)

print(as.numeric(binomial_coefficient(as.brob(m), as.brob(k))))
