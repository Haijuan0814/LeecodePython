class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        if k == 0 or len(words) ==0 :
            return []
        
        result = {} # define a dictionary
        for i in words:
            if i in result:
                result[i] +=1
            else:
                result[i] =1

        # 按照字母出现频率倒序排列，相同顺序的记录按照keys的字母表顺序排序
        sorted_result = sorted(result.keys(), key = lambda x : (-result[x],x))[:k]
        return sorted_result
    
        #sorted_keys = sorted(result, key=result.get , reverse=True)[:k]
        #return sorted_keys

solution = Solution() 
result = solution.topKFrequent(['i','love','leecode','i','love','coding'],4)
# print(result)