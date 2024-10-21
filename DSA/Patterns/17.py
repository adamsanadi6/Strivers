""" 

Problem statement
Sam is curious about Alpha-Hills, so he decided to create Alpha-Hills of different sizes.

An Alpha-hill is represented by a triangle, where alphabets are filled in palindromic order.

For every value of ‘N’, help sam to return the corresponding Alpha-Hill.

Example:
Input: ‘N’ = 3

Output: 
    A
  A B A
A B C B A
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1  <= N <= 25
Time Limit: 1 sec
Sample Input 1:
3
Sample Output 1:
    A
  A B A
A B C B A
Sample Input 2 :
1
Sample Output 2 :
A

"""

def alphaHill(n: int):
    # Write your solution from here.
    for i in range(n):
        print(' ' * ((n - i - 1) * 2), end = '')
        for j in range(i + 1):
            print(chr(ord('A') + j), end = ' ')
        for j in range(i - 1, -1, -1):
            print(chr(ord('A') + j), end =' ')
        print()


alphaHill(int(input()))