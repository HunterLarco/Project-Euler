#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def is_valid(n, power=5):
  digits = map(int, list(str(n)))
  return sum(digit**power for digit in digits) == n

def upper_bound(power=5):
  """
  " The upper bound is the point where the 9^power * total_digits is a number with fewer
  " digits than total_digits. For example: 9^4 * 1 is 6561. So there might be a 1 digit
  " number. However, 9^4 * 6 is 39366 which is less than 6 digits, so there cannot be an
  " applicable 6 digit number.
  """
  total_digits = 1
  while True:
    max_sum = 9**power * total_digits
    if len(str(max_sum)) < total_digits:
      return max_sum
    total_digits += 1

def all_numbers_for_power(power):
  for n in range(2, upper_bound(power=power)+1):
    if is_valid(n, power=power):
      yield n

def main():
  print sum(all_numbers_for_power(5))

if __name__ == '__main__':
  main()
