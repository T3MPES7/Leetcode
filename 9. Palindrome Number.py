

# Solution 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx=str(x)
        palindrome=[]
        for i in strx:
           palindrome.insert(0,i)
        palindrome=("".join(map(str,palindrome)))
        return strx==palindrome

#Solution 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
