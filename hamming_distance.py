def hamming_distance(p, q):
  distance = 0
  for i in range(0, len(p)):
    if p[i] != q[i]:
      distance += 1
  return distance

if __name__ == "__main__":
  filename = raw_input("Enter a file name: ")
  f = open(filename, "r")
  p = f.readline()
  q = f.readline()
  print hamming_distance(p, q)
