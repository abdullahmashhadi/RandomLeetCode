class Solution:
    def getLucky(self, s: str, k: int) -> int:
        new_str=""
        for char in s:
            new_str+=str(ord(char) - ord('a') + 1)
        integer_sum=0
        for i in range(k):
            if i==0:
                integer_sum=sum(int(char) for char in new_str)
            else:
                integer_sum=sum(int(char) for char in str(integer_sum))
        return integer_sum

s=input("Enter string\n")
k=int(input("Enter the number of transforms\n"))
sol=Solution()
output=sol.getLucky(s,k)
print(f"sum od digits of string after conversion is: {output}")