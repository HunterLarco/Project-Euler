"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def all_factors(N):
  for i in range(2, int(N**0.5+1)):
    if N % i == 0:
      yield i
      while N % i == 0:
        N //= i
  yield N

def main():
  print(max(all_factors(600851475143)))

if __name__ == '__main__':
  main()
