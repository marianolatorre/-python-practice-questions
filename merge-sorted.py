class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        to_write = m+n-1
        n1=m-1
        n2=n-1
        while n2 >= 0 and n1 >= 0:
            print("nums2[n2] > nums1[n1]",nums2[n2], nums1[n1], n2)
            if nums2[n2] > nums1[n1]:
                nums1[to_write]=nums2[n2]
                n2 -= 1
                to_write -= 1
            else:
                nums1[to_write]=nums1[n1]
                n1 -= 1
                to_write -= 1
            print(nums1)
        while n2 >= 0:
            nums1[to_write] = nums2[n2]
            to_write -= 1
            n2 -= 1
        print(nums1)

s=Solution()
# s.merge([1,2,3,0,0,0],3,[2,5,6],3)

s.merge([2,3,0],2,[1],1)