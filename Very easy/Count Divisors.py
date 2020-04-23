# You have been given 3 integers - l, r and k. Find how many numbers between l and r (both inclusive) 
# are divisible by k. You do not need to print these numbers, you just have to find their count.

# Input Format
# The first and only line of input contains 3 space separated integers l, r and k.

# Output Format
# Print the required answer on a single line.

# Constraints


# SAMPLE INPUT 
# 1 10 1
# SAMPLE OUTPUT 
# 10

m, n, k = map(int, input().split(' '))
cnt = 0
for i in range(m, n+1):
    if(i % k == 0):
        cnt = cnt+1
print(cnt)
