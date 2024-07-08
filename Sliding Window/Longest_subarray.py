''' Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's. '''

def longestSubarray(nums):
    n = len(nums);
    left = 0;
    max_length = 0;
    zero_count = 0;
    
    
    
    for right in range(n):
        if nums[right] == 0:
            zero_count+=1;
            
        while (zero_count>1):
            if nums[left] == 0:
                zero_count -= 1;
            left+=1

        max_length = max(max_length, right-left+1)
        
    return max_length - 1

print(longestSubarray(nums=[1,1,0,1]))
print(longestSubarray(nums=[0,1,1,1,0,1,1,0,1]))
print(longestSubarray(nums=[1,1,1]))
    
    