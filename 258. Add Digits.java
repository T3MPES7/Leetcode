class Solution {
    public int addDigits(int num) {
        if(num==0)return 0; //When the integer is 0 returns 0
        
        if(num%9==0)return 9; //When the integer is divisible by 9, 9 is returned 
        
        else return num%9; //Returns the digital root of any other integer
    }
}
