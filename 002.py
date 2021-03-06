"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def fibonacci_numbers():
  past = [0, 1]
  while True:
    next_number = sum(past)
    yield next_number
    past.append(next_number)
    past.pop(0)

def sum_even_fib_less_than(N):
  accumulator = 0
  for number in fibonacci_numbers():
    if number > N: return accumulator
    if number % 2 == 0:
      accumulator += number

def main():
  print(sum_even_fib_less_than(4000000))

if __name__ == '__main__':
  main()
