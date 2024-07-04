''' You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations. '''

def maxOperations(nums,k:int):
    nums.sort()
    
    left = 0
    right = len(nums) - 1
    count = 0
    
    while(left<right):
        current_sum = nums[left] + nums[right]
        
        if current_sum == k:
            count+=1
            left+=1
            right-=1
            
        elif current_sum<0:
            left+=1
        else:
            right-=1
            
    return count

print(maxOperations(nums=[0,1,2,3,4,5,6,7,8,9],k=9))
        