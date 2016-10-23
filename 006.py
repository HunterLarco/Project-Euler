"""
The sum of the squares of the first ten natural numbers is,

1 + 4 + ... + 100 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def main():
  N = 100
  print(sum(range(N+1))**2 - sum(map(lambda x: x**2, range(N+1))))
  

if __name__ == '__main__':
  main()
