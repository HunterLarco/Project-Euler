"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

def memoize(funct):
  data = {}
  def helper(*args):
    if args in data:
      return data[args]
    result = funct(*args)
    data[args] = result
    return result
  return helper

@memoize
def possible_paths(x, y):
  if x == 0 and y == 0: return 1
  paths = 0
  if x > 0: paths += possible_paths(x - 1, y)
  if y > 0: paths += possible_paths(x, y - 1)
  return paths

def main():
  print(possible_paths(20, 20))

if __name__ == '__main__':
  main()
