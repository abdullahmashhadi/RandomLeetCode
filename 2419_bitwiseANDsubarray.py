from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num=max(nums)
        length=0
        maximum_length=0
        for i in range(len(nums)):
            if nums[i]==max_num:
                length+=1
                maximum_length=max(maximum_length,length)
            else:
                length=0
        return maximum_length

nums=list(map(int,input("Enter elements of your array (space-separated):\n").split()))
sol=Solution()
output=sol.longestSubarray(nums)
print(f"The length of subarray with maximum bitwise AND value is {output}")