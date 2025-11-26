class Solution:
    def countFrequencies(self, nums):
        # Your code goes here
        visited=set()
        result=[]
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            count=0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            result.append([nums[i],count])
            visited.add(nums[i])
        return result
raw = input().strip()       # "[1,2,2,1,3]"
raw = raw.strip("[]")       # "1,2,2,1,3"
n = list(map(int, raw.split(",")))
print(Solution().countFrequencies(n))

