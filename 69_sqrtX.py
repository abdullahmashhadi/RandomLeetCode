class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        l,r=0,x
        while l<=r:
            mid=(l+r)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                l=mid+1
            else:
                r=mid-1
        if abs(x-l*l)<abs(x-r*r):
            return int((x+l*l)/(2*l))
        else:
            return int((x+r*r)/(2*r))

x=int(input("Enter number you want square-root of:\n"))
sol=Solution()
output=sol.mySqrt(x)
print(f"The square root of {x} rounded off is {output}")