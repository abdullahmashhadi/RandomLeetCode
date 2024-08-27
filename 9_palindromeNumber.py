class Solution:
    def isPalindrome(self, x: int) -> bool:
        number=str(x)
        i=0
        j=len(number)-1
        while(i<j):
            if number[i]==number[j]:
                i+=1
                j-=1
            else:
                return False
        return True
x=int(input("Enter a number to check for palindrome:\n"))
sol=Solution()
output=sol.isPalindrome(x)
print(output)