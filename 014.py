"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def memoize(funct):
  """ Note that only the *args are used as the memoization key. """
  data = {}
  def helper(*args, **kwargs):
    if args in data:
      return data[args]
    result = funct(*args, **kwargs)
    data[args] = result
    return result
  return helper

@memoize
def collatz_chain_length(value):
  if value == 1: return 1
  if value % 2 == 0:
    return collatz_chain_length(value // 2) + 1
  return collatz_chain_length(3*value + 1) + 1

def longest_collatz_chain_under(upper_bound):
  longest_chain = 0
  pocket = 0
  for i in range(1, upper_bound):
    chain_length = collatz_chain_length(i)
    if chain_length > longest_chain:
      longest_chain = chain_length
      pocket = i
  return pocket

def main():
  print(longest_collatz_chain_under(1000000))

if __name__ == '__main__':
  main()
