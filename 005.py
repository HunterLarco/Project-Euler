"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from collections import Counter
from collections import defaultdict

def factorize(N):
  if N < 2: return []
  for i in range(2, int(N**0.5+1)):
    if N % i == 0:
      return [i] + factorize(N//i)
  return [N]

def smallest_possible_multiple(divisors):
  """
  Basically, if trying to find the smallest possible multiple of both 8 and 12 we can
  realize that 8=2*2*2 and 12 = 2*2*3. Therefore the answer is 2*2*2*3=24. By taking
  the largest amount of factors per divisor we can assert that each divisor is contained
  by the final set of divisors. Thus the product is the smallest possible multiple.
  """
  smallest_product_factors = defaultdict(int)
  for i in divisors:
    factors = Counter(factorize(i))
    for factor, count in factors.items():
      smallest_product_factors[factor] = max(smallest_product_factors[factor], count)
  accumulator = 1
  for factor, count in smallest_product_factors.items():
    accumulator *= factor**count
  return accumulator

def main():
  print(smallest_possible_multiple(range(1, 21)))

if __name__ == '__main__':
  main()
