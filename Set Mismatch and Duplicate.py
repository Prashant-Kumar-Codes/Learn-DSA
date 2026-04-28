'''
Que: You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.


Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
'''

# solution - 1 : using hashing approach
def findDuplicate(nums):
    n = len(nums)
    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1
    
    duplicate = -1
    missing = -1
    
    for i in range(1, n + 1):
        if i in counts:
            if counts[i] == 2:
                duplicate = i
        else:
            missing = i
            
    return [duplicate, missing]
        
print(findDuplicate([1,2,3,4,5,6,6,8,9,10]))
print(findDuplicate([2, 2]))
print(findDuplicate([3, 2, 2]))

