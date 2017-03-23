
def complement(p):
  if (p == "A"): return "T"
  if (p == "C"): return "G"
  if (p == "G"): return "C"
  if (p == "T"): return "A"

def reverse_complement(pattern):
  p = ""
  for i in pattern:
    p = complement(i) + p
  return p
