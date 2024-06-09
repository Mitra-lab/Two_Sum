class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        f=0
        l=len(nums)-1

        while f < l:
            # Check the sum of the two pointers
            sum_val = nums[f] + nums[l]
            if sum_val == target:
                return [f, l]
            elif sum_val < target:
                f += 1
            else:
                l -= 1
        
        # If no solution is found (though the problem guarantees one)
        return []

nums = [1,2,4,5,6,9]
result=Solution().twoSum(nums,9)

print(result)