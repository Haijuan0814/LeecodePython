class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        inter = Counter(nums1) & Counter(nums2)
        result = []
        for k, v in inter.items():
            result.extend([k] * v)
            
        return result


        