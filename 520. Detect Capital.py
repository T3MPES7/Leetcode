class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        listed=[*word]
        temp=""
        count=0
        for x in listed:
            temp=x.upper()
            if temp==x:
                count+=1
        if count==len(listed) or count==0:
            return True
        elif count==1 and listed[0]==listed[0].upper():
            return True
        else:
            return False
