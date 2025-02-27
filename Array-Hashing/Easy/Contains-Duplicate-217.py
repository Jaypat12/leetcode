'''

Contains Duplicate - 217 

'''

def containsDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                return True
        return False

'''

The method above is known to be more time efficent, but require more memory. 
We want to find if there is duplicate integers in the List/Array. 
In this approach, you get the frequency of the different integers by using a hashmap
If you see the a integer for the first time you place it in the hashmap. Now if that same
number appears again, the first if statement will fail because the number is in the hashmap 
,thus you automatically retrun True. Now if you go through all the numbers, and there is 
no duplicates you return False

'''

def containsDuplicate(self, nums: List[int]) -> bool:
        answer = False
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                answer = True 
        return answer

'''

In this method you sort the array/list and using the range function, you check the 
current position/index integer with the next position/index number. If they are a match, 
retrun True. If you go through all numbers and nothing is found return False.
IMPORTANT - USE len(nums)-1 because, you don't want to check outside the list (goinging 
beyond the len(nums)

'''
