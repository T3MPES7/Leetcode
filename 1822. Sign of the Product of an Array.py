class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product=1
        for i in nums:
            product=product*i
        if product>1:
            return 1
        if product==0:
            return 0
        return -1
