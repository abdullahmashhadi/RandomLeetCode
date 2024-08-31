from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        i=0
        length=len(nums)
        while(i<length-count):
            if nums[i]==val:
                found=nums.pop(i)
                nums.append(found)
                count+=1
            else:
                i+=1

        return length-count

nums=list(map(int,input("Enter your array (space-separated):\n").split()))
val=int(input("Enter the value you want to find:\n"))
sol=Solution()
output=sol.removeElement(nums,val)
print(f"The array after removing all occurences of {val} is: {nums[:output]}")        