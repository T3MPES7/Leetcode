//Time Complexity O(N^2)
//Brute Force Method
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int length=nums.length; //Obtains the legnth of the array
        for(int i =0;i<length-1;i++){ //Loops starting from the first index
            for (int x=1+i;x<length;x++){ //Loops starting with the second index 
                if(nums[i]+nums[x]==target){ //Attempts all possible combinations 
                return new int[]{i,x}; //If the combination i correct the correct one is returned 
                }

            }
        }
        return new int[]{}; // Incase no solution exists a blank is returned 
    }
}
/////////////////////////////////////////////////////////////////////////////////////


//Hash Map Method
