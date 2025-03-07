'''

Two Out of Three - 2032

'''


def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        arr = []
        
        m = max(max(nums1),max(nums2),max(nums3))
        for i in range(m+1):
            if (i in nums1 and i in nums2) or (i in nums2 and i in nums3) or (i in nums1 and i in nums3):
                arr.append(i)

        return arr

"finish commenting"