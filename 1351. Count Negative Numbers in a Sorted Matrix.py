#time complexity O(n^2)
#Brute Force Approuch
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0 
        for x in range(len(grid)):#goes through each array
            for i in range(len(grid[x])): #goes through each element of an array
                if grid[x][i]<0: #when the element is negative
                    count+=1
        return count
