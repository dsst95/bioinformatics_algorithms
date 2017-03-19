def skew(genome):
  nextval = 0
  for c in genome:
    print nextval
    if c == 'C':
      nextval -= 1
    elif c == 'G':
      nextval += 1
    else:
      pass
  print nextval

if __name__ == "__main__":
  genome = raw_input("Genome: ")
  skew(genome)
