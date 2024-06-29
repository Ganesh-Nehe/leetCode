public class Solution {
    public boolean isPalindrome(int x) {
        
        if(x>=0){
            int y = 0;
            int original = x;
            while (x!=0){
                int z=x%10;
                y = y*10 + z;
                x=x/10;
            }
    
        if(original == y)
            return true;
        else
            return false;
        }
        else{
            return false;
        }
    }

} 
