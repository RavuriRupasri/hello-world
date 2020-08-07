'''
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

 

Example 1:

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
'''
s = input()
indices = list(map(int,input().split()))
print(''.join(s[indices.index(i)] for i in range(len(indices))))