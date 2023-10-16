class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[1]
        last=1
        for r in range(1,rowIndex+1):
            nextt=last*(rowIndex-r+1)//r       
            ans.append(nextt)
            last=nextt
        return ans
