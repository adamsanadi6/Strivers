""" 
Problem statement
Sam is planting trees on the upper half region (separated by the left diagonal) of the square shared field.

For every value of ‘N’, print the field if the trees are represented by ‘*’.

Example:
Input: ‘N’ = 3

Output: 
* * *
* *
*
"""

def pattern(n):
    for i in range(n, 0, -1):
        print("* " * i)

n = int(input())
pattern(n)