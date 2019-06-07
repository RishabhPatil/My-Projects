def geoser(i, r, n=float("infinity")):
# If there are infinite terms
  if n == float("infinity"):
# If the sum converges
    if r>-1 and r<1:
      return i/(1-r)
# If the sum diverges
    elif r<-1 or r>1:
      return "UNDEFINED"
# If there is a finite amount of terms
  else:
# If the terms are all equal
    if r == 1:
      return i * n
# If the terms aren't all the same
    else:
      return (i * (1 - (r ** n))) / (1 - r)

print(geoser(3, 0.31415926535897))
print(geoser(4, 13))
print(geoser(12, 1, 11))
print(geoser(5, 3, 12))
