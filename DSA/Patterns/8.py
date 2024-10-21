"""

Problem statement
Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the Reverse N-Star Triangle.

Example:
Input: ‘N’ = 3

Output: 

*****
 ***
  *
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1  <= N <= 20
Time Limit: 1 sec
Sample Input 1:
3
Sample Output 1:
*****
 ***
  *
Explanation Of Sample Input 1 :
The first row contains five stars.
The second row contains one space, followed by three stars.
The third row contains two spaces, followed by a star.
Sample Input 2 :
1
Sample Output 2 :
*

"""


def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(n):
        print(' ' * i, end = '')
        print('*' * ((n - i - 1) * 2 + 1))

# print(' ' * 0)

n = int(input())

nStarTriangle(n)