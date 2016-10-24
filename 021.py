"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import ceil

def divisor_sum(N):
  accumulator = 1
  for i in range(2, int(N**0.5) + 1):
    if N % i == 0:
      accumulator += i + N//i
  # Correct perfect squares
  if N**0.5 % 1 == 0: accumulator -= int(N**0.5)
  return accumulator

def is_amicable_number(N):
  return divisor_sum(N) != N and divisor_sum(divisor_sum(N)) == N

def main():
  print(sum(filter(is_amicable_number, range(2, 10000))))

if __name__ == '__main__':
  main()
