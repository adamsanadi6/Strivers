""" 

Problem statement
Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Rotated Triangle.

Example:
Input: ‘N’ = 3

Output: 

*
**
***
**
*
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1  <= N <= 20
Time Limit: 1 sec
Sample Input 1:
3
Sample Output 1:
*
**
***
**
*
Sample Input 2 :
1
Sample Output 2 :
*

"""


def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(1, n + 1):
        print('*' * i)
    
    for i in range(1, n):
        print('*' * (n - i))

n = int(input())

nStarTriangle(n)