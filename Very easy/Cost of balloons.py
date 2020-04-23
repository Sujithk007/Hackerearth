# You are conducting a contest at your college. This contest consists of two problems and  
# participants. You know the problem that a candidate will solve during the contest.

# You provide a balloon to a participant after he or she solves a problem. 
# There are only green and purple-colored balloons available in a market. 
# Each problem must have a balloon associated with it as a prize for solving that specific problem.
# You can distribute balloons to each participant by performing the following operation:

# Use green-colored balloons for the first problem and purple-colored balloons for the second problem
# Use purple-colored balloons for the first problem and green-colored balloons for the second problem
# You are given the cost of each balloon and problems that each participant solve. Your task is to
# print the minimum price that you have to pay while purchasing balloons.

# Input format

# First line:  that denotes the number of test cases ()
# For each test case: 
# First line: Cost of green and purple-colored balloons 
# Second line:  that denotes the number of participants ()
# Next  lines: Contain the status of users. For example, if the value of the  integer in the  row is , then it depicts that the  participant has not solved the  problem. Similarly, if the value of the  integer in the  row is , then it depicts that the  participant has solved the  problem.
# Output format
# For each test case, print the minimum cost that you have to pay to purchase balloons.

# SAMPLE INPUT 
# 2
# 9 6
# 10
# 1 1
# 1 1
# 0 1
# 0 0
# 0 1
# 0 0
# 0 1
# 0 1
# 1 1
# 0 0
# 1 9
# 10
# 0 1
# 0 0
# 0 0
# 0 1
# 1 0
# 0 1
# 0 1
# 0 0
# 0 1
# 0 0
# SAMPLE OUTPUT 
# 69
# 14

for i in range(int(input())):
    m, n = map(int, input().split(' '))
    r, g = 0, 0
    for j in range(int(input())):
        t, y = map(int, input().split(' '))
        r = r+t
        g = g+y
    if(m > n):
        m, n = n, m
    if(r > g):
        print(r*m+g*n)
    else:
        print(g*m+r*n)
