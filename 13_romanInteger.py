class Solution:
    def romanToInt(self, s: str) -> int:
        values={'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}
        prev_value=0
        output=0
        for char in reversed(s):
            if values[char]<prev_value:
                output-=values[char]
            else:
                output+=values[char]
            prev_value=values[char]

        return output
sol=Solution()
s="MCMXCIV"
output=sol.romanToInt(s)
print(output)