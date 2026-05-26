class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m::] = nums2
        for i in range (len(nums1)) :
            for y in range (len(nums1)-1-i) :
                if nums1[y] > nums1[y+1]:
                    nums1[y], nums1[y+1] = nums1[y+1], nums1[y]
