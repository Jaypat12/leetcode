'''

Two Sum - 1

'''

def twoSum(self, nums: List[int], target: int) -> List[int]:    
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
            numMap[nums[i]] = i

        return []

'''

In this problem, we use a hashmap in a manner which will make the integer be the key 
and  index be the value. This will allow us to know where the index is for a certain 
integer. (That is the idea of the problem). Now the way this algo works, is that 
you try to see if the complement of the integer you currently have is in the hashmap
if it is you can easily return the index at which you are at, and then you can easily
numMap[complement] to get the complements index as well. At the end, if that complement
is not found, then you simply put integer with the index into the hashmap. 

finally if there is not a solution, you should retrun []

'''
