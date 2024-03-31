class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        # nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff
        # nums1[i] - nums1[j] - nums2[i] + nums2[j] <= diff
        # nums1[i] - nums2[i] - (nums1[j] - nums2[j] ) <= diff
        # 0 <= i < j <= n - 1 
        # find i-j <= diff
        """ 
        subs = []
        for i in range(len(nums1)):
            subs.append(nums1[i] - nums2[i]) 
        """
        
        def merge_sort(nums):
            if len(nums) <= 1:
                return 0
            mid = len(nums) // 2
            left = nums[:mid]
            right =nums[mid:]

            c_l = merge_sort(left)
            c_r = merge_sort(right)

            # count the pairs
            i = j = c = 0
            while i < len(left) and j < len(right):
                if left[i] - right[j] <= diff:
                    c += len(right) - j
                    i += 1
                else:
                    j += 1
            
            # regular merge
            i = j = k = 0
            while i < len(left) and j < len(right):
                if right[j] < left[i]:
                    nums[k] = right[j]
                    j += 1
                else:
                    nums[k] = left[i]
                    i += 1
                k += 1
            
            # append the left
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

            return c_l + c_r + c

        subs = [ a - b for (a , b) in zip(nums1 , nums2)]
        return merge_sort(subs) 
            
                
                
                



