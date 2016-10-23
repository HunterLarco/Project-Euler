"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def is_prime(N):
  for i in range(2, int(N**0.5+1)):
    if N % i == 0:
      return False
  return True

def prime(N):
  primes_found = 0
  i = 2
  while True:
    if is_prime(i):
      primes_found += 1
      if primes_found == N:
        return i
    i += 1

def main():
  print(prime(10001))

if __name__ == '__main__':
  main()
