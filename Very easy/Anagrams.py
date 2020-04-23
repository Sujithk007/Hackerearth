#url:https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/anagrams-651/

# Given two strings, a and b, that may or may not be of the same length, 
# determine the minimum number of character deletions required to
# make a and b anagrams. Any characters can be deleted from either of the strings.

# Input:

# test cases, t
# two strings a and b, for each test case
# Output:

# Desired O/p

# Constraints:

# string lengths <= 10000

# Note:

# Anagram of a word is formed by rearranging the letters of the word.

# For e.g. -> For the word RAM - MAR, ARM, AMR, RMA etc. are few anagrams.

# SAMPLE INPUT
# 1
# cde
# abc
# SAMPLE OUTPUT
# 4

#Program Code
for i in range(int(input())):
    a = list(input())
    b = list(input())
    al = len(a)
    bl = len(b)
    cnt = 0
    for i in a:
        if(i in b):
            b.remove(i)
            cnt = cnt+2
    print(al+bl-cnt)
