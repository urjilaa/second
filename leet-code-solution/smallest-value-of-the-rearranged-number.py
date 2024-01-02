class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = list(str(num))
        st = sorted(nums)
        ans = 0

        if '-' in nums:
            nums.remove('-')
            n = sorted(nums, reverse=True)
            ans = int('-' + "".join(n))
        else:
            for i in range(len(st)):
                if st[0]== '0' and st[i] != 0:
                    st[0], st[i] = st[i], st[0]
                    ans = int("".join(st))
                else:
                    ans = int("".join(st))
                    
        return int(str(ans))
        