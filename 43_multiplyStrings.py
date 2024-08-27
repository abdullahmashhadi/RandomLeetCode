class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        length=len(num1)
        product=0
        for i in range(length):
            product+=(10**i)*int(num1[length-1-i])*int(num2)
        return str(product)
sol=Solution()
output=sol.multiply("123","456")
print(output)