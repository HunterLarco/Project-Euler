"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

# This solution requires 'inflect' to be installed and because of this, the 2.7 runtime.
import inflect
import re

number_to_words = inflect.engine().number_to_words

def count_words(start, end):
  """ Note that start and end are inclusive. """
  for i in range(start, end + 1):
    words = number_to_words(i)
    count = len(re.sub(r'[^a-zA-Z]', '', words))
    yield count

def main():
  print sum(count_words(1, 1000))

if __name__ == '__main__':
  main()
