class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bin=bin(start)[2:]
        goal_bin=bin(goal)[2:]
        max_len = max(len(start_bin), len(goal_bin))
        goal_bin=goal_bin.zfill(max_len)
        start_bin=start_bin.zfill(max_len)
        i=max_len-1
        count=0
        while(i>=0):
            if (start_bin[i]!=goal_bin[i]):
                count+=1
            i-=1

        return count
        
start=int(input("Enter starting number:\n"))
goal=int(input("Enter goal number:\n"))
sol=Solution()
output=sol.minBitFlips(start,goal)
print(f"The minimum bit flips required to convert {start} to {goal} are: {output}")