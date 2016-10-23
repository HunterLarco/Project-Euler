"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def sum_even_fib_less_than(N):
  """
  Note that this problem is solved using DP due to the large scale required by the
  original problem.
  """
  accumulator = 0
  past = [1, 1]
  while True:
    curr = sum(past)
    if curr > N:
      return accumulator
    if curr % 2 == 0:
      accumulator += curr
    past.append(curr)
    del past[0]

def main():
  print(sum_even_fib_less_than(4000000))

if __name__ == '__main__':
  main()