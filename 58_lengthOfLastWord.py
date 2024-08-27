class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
s=input("Enter string:\n")
sol=Solution()
output=sol.lengthOfLastWord(s)
print(f"Length of last word in string: {s} is {output} ")