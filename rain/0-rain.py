#!/usr/bin/python3
"""calculates the total rain water retained btw walls"""
def rain(walls):
    """Calculates the total rainwater retained between walls.

  Args:
    walls: A list of non-negative integers representing wall heights.

  Returns:
    The total amount of rainwater retained (integer).
  """
    if not walls:
        return 0

    n = len(walls)
    total_water = 0

    for i in range(1, n-1):
        max_left = max(walls[:i])
        max_right = max(walls[i+1:])

        potential_water = min(max_left, max_right) - walls[i]
        if potential_water > 0:
            total_water += potential_water

        return total_water
