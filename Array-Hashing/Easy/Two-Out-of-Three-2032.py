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

'''

Basically the goal was to see if there are numbers within the arrays that are present
within 2 out of three array. So what I do is get the max number amongst all the arrays
Form there, i did did a range from 0 to the highest number. For every single number i checked
if that number belonged to 2 of the following arrays. So (1,2) or (2,3) or (1,3). If it was there
I added to arry

'''


def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        arr = []
        a = set(nums1)
        b = set(nums2)
        c = set(nums3)

        d = list(a) + list(b) + list(c)

        di = {}
        for i in d:
            if i not in di:
                di[i] = 1
            else:
                if i not in arr:
                    arr.append(i)
        
        return arr


'''

For this one, what I did is get the set of each array. this would remove any duplicated in
the array. And from there I added the sets together by making them a array. So then,
from there I put ino tthe dictionary, if the integer is not in dict, then we place it and record
the frequecny. Now if the integer is the dictionary but not in the arr. Then we append into array
meaning it would be final answer.

a = [1,1,3,2]
b = [2,3]
c = [3]

after set

{1,3,2} {2,3} {3}

not cover into list and add them together

[1,3,2,2,3,3]

then put in dict, and if it appeared again check if in arr, if not then
we pust that answer in the arr.

so [2,3] is th answer

'''