class Solution:
    def reverse(self, x: int) -> int:
        result=int(str(abs(x))[::-1])
        if x<0:
            result=-result
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result
x=int(input("Enter integer to reverse:\n"))
sol=Solution()
output=sol.reverse(x)
print(output)