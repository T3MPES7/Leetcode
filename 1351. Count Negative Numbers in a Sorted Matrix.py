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
##################################################################
#Second Solution
#time complexity O(N+M)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        r=len(grid)-1 #number of arrays in a matrix
        s=0
        while s<len(grid[0]) and r>=0: #runs through each element of each array following the constraits of non-increasing order
            if grid[r][s]<0: #when a negative element is met
                count+=len(grid[0])-s #obtains the umber of negative elements in the array without having to go through them
                r-=1
            else:
                s+=1 #when no negative is met, following the constraits of non increasing order in the matrix
        return count
            
