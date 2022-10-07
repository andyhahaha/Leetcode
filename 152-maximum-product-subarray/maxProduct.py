class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # T: O(N) M: O(1)
        # max_product is the max product value from any previous value to current value
        # min_product is the min product value from any previous value to current value
        
        res = max_product = min_product = nums[0]
        for i in xrange(1, len(nums)):
            max_tmp = max_product
            max_product = max(max_tmp * nums[i], nums[i],min_product * nums[i])
            min_product = min(max_tmp * nums[i], nums[i], min_product * nums[i])
            res = max(res, max_product)
            
        return res
