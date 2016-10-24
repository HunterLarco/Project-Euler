"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

      (3)
    (7)  4
   2  (4)  6
 8   5  (9)  3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                            75
                          95  64
                        17  47  82
                      18  35  87  10
                    20  04  82  47  65
                  19  01  23  75  03  34
                88  02  77  73  07  63  67
              99  65  04  28  06  16  70  92
            41  41  26  56  83  40  80  70  33
          41  48  72  33  47  32  37  16  94  29
        53  71  44  65  25  43  91  52  97  51  14
      70  11  33  28  77  73  17  78  39  68  17  57
    91  71  52  38  17  14  91  43  58  50  27  29  48
  63  66  04  68  89  53  67  30  73  16  69  87  40  31
04  62  98  27  23  09  70  98  73  93  38  53  60  04  23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

import math

TREE = (75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4, 82, 47, 65, 19, 1, 23, 75, 3, 34, 88, 2, 77, 73, 7, 63, 67, 99, 65, 4, 28, 6, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23)

def memoize(funct):
  data = {}
  def helper(*args):
    if args in data:
      return data[args]
    result = funct(*args)
    data[args] = result
    return result
  return helper

def level_for_index(index):
  """
  At each level, there are level*(level-1)/2 items above that level (starting at 1). Thus
  we can say that at each level, level*(level-1)/2 = start index of that level. Solve this
  in reverse and we can then find the level for a given index.
  """
  return int((-1 + math.sqrt(1 + 8*index)) / 2)

def get_left_index(tree, index):
  left_index = index + level_for_index(index) + 1
  if left_index >= len(tree): return None
  return left_index

def get_right_index(tree, index):
  right_index = index + level_for_index(index) + 2
  if right_index >= len(tree): return None
  return right_index

@memoize
def largest_sum(tree, node_index):
  left_index = get_left_index(tree, node_index)
  right_index = get_right_index(tree, node_index)
  if left_index and right_index:
    left_sum = largest_sum(tree, left_index)
    right_sum = largest_sum(tree, right_index)
    if left_sum > right_sum:
      return left_sum + tree[node_index]
    return right_sum + tree[node_index]
  elif left_index:
    return largest_sum(tree, left_index) + tree[node_index]
  elif right_index:
    return largest_sum(tree, right_index) + tree[node_index]
  return tree[node_index]

def main():
  print(largest_sum(TREE, 0))

if __name__ == '__main__':
  main()
