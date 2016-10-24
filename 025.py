"""
The Fibonacci sequence is defined by the recurrence relation:

F(n) = F(n−1) + F(n−2), where F(1) = 1 and F(2) = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

from math import log

def fibonacci_numbers():
  yield 1
  past = [0, 1]
  while True:
    next_number = sum(past)
    yield next_number
    past.append(next_number)
    past.pop(0)

def main():
  for index, number in enumerate(fibonacci_numbers()):
    if int(log(number, 10)) + 1 >= 1000:
      print('Index:', index + 1)
      break

if __name__ == '__main__':
  main()
