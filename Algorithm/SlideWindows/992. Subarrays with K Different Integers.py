class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def windows(nums , k):
            nums_count = defaultdict(int)
            res = 0
            left = 0
            right = 0

            for right , num in enumerate(nums):
                nums_count[num] += 1

                while len(nums_count) > k:
                    
                    nums_count[nums[left]] -= 1
                    if nums_count[nums[left]] == 0:
                        del nums_count[nums[left]]
                    left += 1

                res += right - left + 1
            return res
        

        return windows(nums, k) - windows(nums, k - 1)

            
               
