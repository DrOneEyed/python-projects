def sum_series(n):
  if n < 1:
    return n
  else:
    return n + sum_series(n - 2)

def geometric_sum(n):
  if n < 0:
    return 0
  else:
    return (1 / (pow(2, n))) + geometric_sum(n - 1)

def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return (1/n)+ harmonic_sum(n-1)

