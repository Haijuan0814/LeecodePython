class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if not nums or k==0:
            return []

        count = {}
        for i in nums:
            if i in count:
                count[i] +=1
            else:
                count[i] =1

        res = sorted(count.keys() , key = lambda x : (count[x]) , reverse = True)
        return res[:k]

solution = Solution() 
result = solution.topKFrequent([1,2,2,3,3],2)
print(result)
        