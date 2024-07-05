class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        for i in range(k,n):
            current_sum += nums[i]-nums[i-k]
            max_sum = max(max_sum,current_sum)
            
        return max_sum/k

solution = Solution()
print(solution.findMaxAverage(nums=[1,12,-5,-6,50,3], k=4))
print(solution.findMaxAverage(nums=[5], k=1))