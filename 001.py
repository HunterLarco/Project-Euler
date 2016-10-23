"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_of_multiples_below_n(N, multiples=()):
  accumulator = 0
  for i in range(N):
    for multiple in multiples:
      if i % multiple == 0:
        break
    else:
      continue
    accumulator += i
  return accumulator

def main():
  print(sum_of_multiples_below_n(1000, multiples=(3, 5)))

if __name__ == '__main__':
  main()
