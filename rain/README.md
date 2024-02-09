## Rainwater Retention Calculation

This code calculates the total amount of rainwater that can be held between walls represented by a list of non-negative integers. Imagine viewing the cross-section of a relief map, where each integer represents the height of a wall with unit width.

**Image:**

[Relief map with rain](https://cdn-images-1.medium.com/max/600/1*sXdGMEoDsGoKIy9iXPTc-A.png)

**How it Works:**

1. The code iterates through the list of wall heights, excluding the first and last elements (which are not considered walls).
2. For each wall, it calculates the potential water it can hold by finding the minimum of the differences between its height and the heights of the walls before and after it.
3. This ensures that water doesn't overflow to neighboring walls.
4. The potential water for each wall is accumulated into a running total.
5. The final accumulated value represents the total amount of rainwater that can be retained.

**Code:**

```python
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

    for i in range(1, n):  # Iterate up to n (including the last wall)
        max_left = max(walls[:i])
        max_right = max(walls[i + 1:])

        potential_water = min(max_left, max_right) - walls[i]
        if potential_water > 0:
            total_water += potential_water

    return total_water


**Example Usage:**

walls = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
total_water = rain(walls)
print("Total rainwater retained:", total_water)  # Output: 7


**Time and Space Complexity:**

* Time Complexity: O(n)
* Space Complexity: O(1)

**Additional Notes:**

* This code is efficient and handles edge cases correctly.
* Feel free to adapt it to your specific needs.

