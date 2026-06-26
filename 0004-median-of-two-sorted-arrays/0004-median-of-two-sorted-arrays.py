class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lis = sorted(nums1 + nums2)
        length = len(lis)
        median = 0
        if length % 2 == 0:
            print(lis[length//2 - 1], lis[length//2])
            median = (lis[(length - 1)//2] + lis[length//2])/2
        else:
            print(lis[length//2])
            median = lis[(length)//2]

        return median