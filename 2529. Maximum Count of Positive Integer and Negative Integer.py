class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg,pos=0,0 
        for i in range(len(nums)): #runs through each index in the array
            if nums[i]==0: # ignores 0
                continue #moves to next index
            elif nums[i]<0: #if the element is negative
                neg+=1
            else: #if its positive
                pos+=1
        return max(neg,pos) #returns the highest out of the two
