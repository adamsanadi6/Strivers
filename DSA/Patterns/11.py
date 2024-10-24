""" 

Problem statement
Aryan and his friends are very fond of the pattern. For a given integer ‘N’, they want to make the N-Binary Number Triangle.

You are required to print the pattern as shown in the examples below.

Example:
Input: ‘N’ = 3

Output: 

1
0 1
1 0 1
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1  <= N <= 20
Time Limit: 1 sec
Sample Input 1:
3
Sample Output 1:
1
0 1
1 0 1
Sample Input 2 :
4
Sample Output 2 :
1
0 1
1 0 1
0 1 0 1
Sample Input 3 :
6
Sample Output 3 :
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
0 1 0 1 0 1

"""


def nBinaryTriangle(n: int) -> None:
    # Write your solution here.

    for i in range(1, n + 1):
        digit = i % 2
        for j in range(i):
            print(digit, end = ' ')
            digit ^= 1
        print()


nBinaryTriangle(int(input()))