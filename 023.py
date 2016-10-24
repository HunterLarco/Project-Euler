"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
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

def is_abundant(N):
  return divisor_sum(N) > N

def is_abundant_sum(i, applicable_numbers):
  for number in applicable_numbers:
    if i - number in applicable_numbers:
      return True
  return False

def main():
  abundant_numbers = set(filter(is_abundant, range(1, 28124)))
  accumulator = 0
  for i in range(1, 28124):
    if not is_abundant_sum(i, abundant_numbers):
      accumulator += i
  print(accumulator)

if __name__ == '__main__':
  main()
