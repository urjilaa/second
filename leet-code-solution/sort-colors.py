class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = nums.count(0)
        one = nums.count(1)
        two = nums.count(2)
        ze= [0]*zero
        on = [1]*one
        tw = [2]*two
       
        nums.clear()
        nums.extend(ze)
        nums.extend(on)
        nums.extend(tw)
       
        #zero = 0
        #one = 0
        #two = 0
        
        #for i in range(len(nums)):
            #if nums[i] == 0:
            #    zero += 1
            #elif nums[i] == 1:
           #     one += 1
          #  else:
         #       two += 1
        #s = "0"*zero + "1"*one + "2"*two
        #print(s)
        #res = []
        #for i in range(len(s)):
        #    nums[i] = s[i]
            #res.append(int(s[i]))
        #ans = list(map(int, res.))
        #ans = ans.strip
        #print(res)
        #return nums