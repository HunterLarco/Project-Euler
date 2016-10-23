"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrom(N):
  text = str(N)
  return text[:len(text)//2] == text[len(text)//2 + len(text) % 2:][::-1]

def main():
  pocket = 0
  for i in range(100, 1000):
    for j in range(100, 1000):
      total = i * j
      if total > pocket and is_palindrom(total):
        pocket = total
  print(pocket)

if __name__ == '__main__':
  main()
