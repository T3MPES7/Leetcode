#time complexity of O(logn).

class Solution:
    def search(self, nums: List[int], target: int) -> int:
       start=0 #the start of the list
       end=len(nums)-1 #the end of the list
       while target in nums: #incase number dose not exist
           mid=(start+end)//2 #mid-point of the list
           if nums[mid]==target: #if the mid-point is the target
               return mid
           elif nums[mid]>target: #if the target is less then the midpoint
                end=mid-1 #the mid-point becomes the end
           else:
                start=mid+1 #the start becomes the midpoint when the upperhalf holds the target
       return -1 #incase the target does not exist

  
            
