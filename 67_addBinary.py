class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
a=input("Enter 1st binary number :\n")
b=input("Enter 2nd binary number :\n")
sol=Solution()
output=sol.addBinary(a,b)
print(f"Sum of {a} and {b} is {output}")