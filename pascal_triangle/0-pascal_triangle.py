#/usr/bin/python3
def pascal_triangle(n):
  """
  Generates Pascal's triangle up to n rows using an iterative approach.
  Args:
      n: The number of rows in the triangle.
  Returns:
      A list of lists representing the Pascal's triangle.
  """
  triangle = []
  for i in range(n):
    row = [1] * (i + 1)
    for j in range(1, i):
      row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)
  return triangle
