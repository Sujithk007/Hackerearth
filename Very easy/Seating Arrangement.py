# url: https: // www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/

# Akash and Vishal are quite fond of travelling. They mostly travel by railways. 
# They were travelling in a train one day and they got interested in the seating arrangement 
# of their compartment. The compartment looked something like

# So they got interested to know the seat number facing them and the seat type facing them. 
# The seats are denoted as follows:

# Window Seat: WS
# Middle Seat: MS
# Aisle Seat: AS

# You will be given a seat number, find out the seat number facing you and
# the seat type, i.e. WS, MS or AS.

# INPUT
# First line of input will consist of a single integer T denoting number of test-cases.
# Each test-case consists of a single integer N denoting the seat-number.

# OUTPUT
# For each test case, print the facing seat-number and the seat-type, 
# separated by a single space in a new line.

# CONSTRAINTS
# 1 <= T <= 105
# 1 <= N <= 108
# SAMPLE INPUT
# 2
# 18
# 40
# SAMPLE OUTPUT
# 19 WS
# 45 AS
# Time Limit:	1.0 sec(s) for each input file.
# Memory Limit:	256 MB
# Source Limit:	1024 KB


#Program Code

d = {1: [11, 'WS'], 2: [9, 'MS'], 3: [7, 'AS'], 4: [5, 'AS'], 5: [3, 'MS'], 6: [1, 'WS'], 
    0: [-11, 'WS'], 11: [-9, 'MS'], 10: [-7, 'AS'], 9: [-5, 'AS'], 8: [-3, 'MS'], 7: [-1, 'WS']}
for i in range(int(input())):
    m = int(input())
    s = d[m % 12]
    print(m+s[0],s[1])
