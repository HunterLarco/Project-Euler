"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

[21]  22  23  24 [25]
 20  [7]  8  [9]  10
 19   6  [1]  2   11
 18  [5]  4  [3]  12
[17]  16  15  14 [13]

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

def layer_dimensions(layer):
  """ Returns the dimensions for a layer starting at 0 (the most inset). """
  return layer * 2 + 1

def corner_values(layer):
  if layer == 0:
    # The first layer has no corners.. Only 1 value.
    yield 1
  else:
    dimension = layer_dimensions(layer)
    internal_sum = sum(layer_dimensions(i)*4 - 4 for i in range(layer)) + 1
    yield internal_sum + (dimension - 1) * 1
    yield internal_sum + (dimension - 1) * 2
    yield internal_sum + (dimension - 1) * 3
    yield internal_sum + (dimension - 1) * 4

def main():
  TARGET_DIMENSION = 1001
  accumulator = 0
  layers = (TARGET_DIMENSION - 1) / 2 + 1
  for i in range(layers):
    accumulator += sum(corner_values(i))
  print accumulator

if __name__ == '__main__':
  main()
