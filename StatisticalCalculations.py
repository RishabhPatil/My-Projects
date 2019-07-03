# Sort the list
def sort(listy):
  while True:
    x = 0
    for i in range(0, len(listy) - 1):
      if listy[i] > listy[i + 1]:
        x += 1
        listy[i], listy[i + 1] = listy[i +1], listy[i]
    if x == 0:
      return listy

# Find the mean of the list
def mean(listy):
  ans = 0
  for i in listy:
    ans += i
  ans = ans / len(listy)
  ans = float(ans)
  return ans

# Find the median of the list
def median(listy):
  listy = sort(listy)
  if len(listy) % 2 == 0:
    return (listy[len(listy) / 2] + listy[len(listy) / 2 - 1]) / 2
  else:
    return listy[(len[listy] - 1) / 2]

# Find the mode of the list
def mode(listy):
  m = {}
  mx = 0
  index = 0
  for i in listy:
    if i not in m:
      m[i] = 0
    m[i] += 1
    if m[i] > mxOcc:
      mxOcc = m[i]
      md = i
    return md

# Reverse the list
def reverse(listy):
  a = 0
  b = len(listy) - 1
  while a < b:
    listy[a], listy[b] = listy[b], listy[a]
    a += 1
    b -= 1
  return listy

# Find the standard deviation
def standardDeviation(listy):
  add = 0
  for i in listy:
    add += (i - mean(listy)) ^ 2 / len(listy)
  return add ^ (1 / 2)
