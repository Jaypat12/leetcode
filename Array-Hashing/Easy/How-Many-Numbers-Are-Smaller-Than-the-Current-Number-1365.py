'''

How Many Numbers Are Smaller Than the Current Number - 1365

'''

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        a = sorted(nums)
        d={}

        for i in range(len(a)):
            if a[i] not in d:
                d[a[i]] = i

        print(d)

        for i in nums:
            arr.append(d[i])

        return arr
    
'''

For this problem, what I did was sort the array which makes it super easy to tell
which number is greater than the other. The index of each interger would represent
how many numbers are lower than it. Now to combat like duplicate integers. You simply
create a hashmap which will only hold the index of each integer for the first time that number
comes. This allows you easily get the number of integers which are lower

arr = [1,1,2,7,3,4]

sarr = [1,1,2,3,4,7]

d = {1:0, 2:2, 3:3, 4:4, 7:5}

answer = [0,0,2,5,3,4]

'''