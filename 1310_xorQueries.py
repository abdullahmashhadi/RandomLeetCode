from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix=[0]*(len(arr)+1)
        for i in range(1,len(arr)+1):
            prefix[i]=prefix[i-1]^arr[i-1]
        result=[]
        for left,right in queries:
            result.append(prefix[right+1]^prefix[left])
        return result

arr=list(map(int, input("Enter elements of your array (space-separated)\n").split()))
n = int(input("Enter the number of queries: "))
queries = []
for i in range(n):
    query = list(map(int, input(f"Enter query {i+1} (two integers separated by a space): ").split()))
    queries.append(query)
sol=Solution()
output=sol.xorQueries(arr,queries)
print(f"The XOR of queries {queries} for array {arr} is: {output}")
        