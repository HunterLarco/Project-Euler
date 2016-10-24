"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def main():
  """
  Yay for python and the lack of overflows!! Note that sum and map are both implemented
  in C++, making this rather efficient.
  """
  print(sum(map(int, str(2**1000))))

if __name__ == '__main__':
  main()
