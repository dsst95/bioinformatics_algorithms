def minimizing_skew(genome):
  min = 0
  nextval = 0
  minimizing_i = []
  for i in range(0, len(genome)):
    if nextval < min:
      min = nextval
      minimizing_i = [i]
    elif nextval == min:
      minimizing_i.append(i)
    if genome[i] == 'C':
      nextval -= 1
    elif genome[i] == 'G':
      nextval += 1
  return minimizing_i


if __name__ == "__main__":
  filename = raw_input("Enter a file name: ")
  f = open(filename, "r")
  genome = f.readline()
  print minimizing_skew(genome)
