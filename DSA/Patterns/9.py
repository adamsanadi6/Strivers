"""

Problem statement
Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Diamond.

Example:
Input: ‘N’ = 3

Output: 

  *
 ***
*****
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
  *
 ***
*****
*****
 ***
  *    
Sample Input 2 :
1
Sample Output 2 :
*
*

"""

def nStarDiamond(n: int) -> None:
    # Write your code here.
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (i * 2 + 1))

    for i in range(n):
        print(' ' * i + '*' * ((n - i - 1) * 2 + 1))

n = int(input())

nStarDiamond(n)