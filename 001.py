"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def is_multiple_of_any(N, candidates):
  """ Returns true if N is a multiple of any of the provided candidates """
  for candidate in candidates:
    if N % candidate == 0:
      return True
  return False

def sum_of_multiples_below_n(N, multiples=()):
  return sum(filter(lambda n: is_multiple_of_any(n, multiples), range(N)))

def main():
  print(sum_of_multiples_below_n(1000, multiples=(3, 5)))

if __name__ == '__main__':
  main()
