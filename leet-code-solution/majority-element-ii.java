class Solution {
  // Returns a list of majority elements
  public List<Integer> majorityElement(int[] nums) {
        
        int candidate1 = -1, candidate2 = -1;
        int count1 = 0, count2 = 0;
        
        for (int e : nums) {
            if (e == candidate1)
                count1++;
            else if (e == candidate2)
                count2++;
          
            else if (count1 == 0) {
                candidate1 = e;
                count1 = 1;
            }
            
            else if (count2 == 0) {
                candidate2 = e;
                count2 = 1;
            }
            
            else {
                count1--;
                count2--;
            }
        }
        
        /* Find if the candidates are actually majority element or not */
        count1 = 0;
        count2 = 0;
        
        for (int e: nums) {
            if (e == candidate1)
                count1++;
            else if (e == candidate2)
                count2++;
        }
        
        List<Integer> res = new ArrayList<Integer>();
        
        if (count1 > nums.length/3)
            res.add(candidate1);
        
        if (count2 > nums.length/3)
            res.add(candidate2);
        
        return res;
    }
}