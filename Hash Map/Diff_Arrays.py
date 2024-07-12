''' Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]] '''

def findDifference(nums1, nums2):
    set1 = set(nums1);
    set2 = set(nums2);
    
    not_in_nums1 = list(set2 - set1)
    not_in_nums2 = list(set1 - set2)
    
    return [ not_in_nums1,not_in_nums2]
    
            
print(findDifference(nums1=[1,2,3],nums2=[2,4,6]))