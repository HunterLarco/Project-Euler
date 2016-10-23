"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def pythagorean_triplet_for_value(N):
  for a in range(2, N):
    for b in range(2, N):
      c = N - a - b
      if a + b + c == N and a**2 + b**2 == c**2:
        return (a, b, c)
  

def main():
  a, b, c = pythagorean_triplet_for_value(1000)
  print('Product:', a*b*c)

if __name__ == '__main__':
  main()
