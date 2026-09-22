class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        tot = (len(nums1)+len(nums2)+1)//2
        lower, upper = 0, len(nums1)
        while lower <= upper:
            i = lower + (upper - lower)//2
            j = tot-i

            l1 = float('-inf') if i==0 else nums1[i-1]
            r1 = float('inf') if i==len(nums1) else nums1[i]
            l2 = float('-inf') if j==0 else nums2[j-1]
            r2 = float('inf') if j==len(nums2) else nums2[j]

            if l1>r2:
                upper = i-1
            elif l2>r1:
                lower = i+1
            else:
                if (len(nums1)+len(nums2))%2==0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1,l2)
