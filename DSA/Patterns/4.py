""" 
Problem statement
Sam is making a Triangular painting for a maths project.

An N-dimensional Triangle is represented by the lower triangle of the pattern filled with integers representing the row number.

For every value of ‘N’, help sam to print the corresponding Triangle.

Example:
Input: ‘N’ = 3

Output: 
1
2 2 
3 3 3
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1  <= N <= 25
Time Limit: 1 sec
Sample Input 1:
3
Sample Output 1:
1 
2 2 
3 3 3
Sample Input 2 :
1
Sample Output 2 :
1
"""


def pattern(n):
    for i in range(1, n + 1):
        print((str(i) + " ") * i )

n = int(input())
pattern(n)