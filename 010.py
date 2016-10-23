"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def sieve_of_eratosthenes(N):
  sieve = [True] * N
  for i in range(2, int(N**0.5)):
    for j in range(2*i, N, i):
      sieve[j] = False
  for i, is_prime in enumerate(sieve):
    if i > 1 and is_prime:
      yield i

def main():
  print('Sum:', sum(sieve_of_eratosthenes(2000000)))

if __name__ == '__main__':
  main()
