'''
******
PART 4
******
The triangle inequality theorem states that in any triangle, the sum of the lengths of any two sides of a triangle must be greater than the length of the third side.
For example, 3, 4, 6 works because:
3 + 4 > 6 
3 + 6 > 4
4 + 6 > 3
However, 2, 3, 5 doesn't work because 2 + 3 is not greater than 5.
Define a function possibletriangle that takes 3 arguments (side1, side2, side3). The function RETURNS (not print) True (Boolean value, not the string, so no quotes necessary) if the sides satisfy the triangle inequality, and False (Boolean value, not the string, so no quotes necessary) if it does not. 
'''

def possibletriangle(side1, side2, side3): 
  x = bool(0)
  y = 0
  z = 0
  a = 0
  if side1 + side2 > side3: 
    y = 1
  if side2 + side3 > side1:
    z = 1
  if side3 + side1 > side2:
    a = 1
  if y + z + a == 3:
    x = bool(1)   
  return x