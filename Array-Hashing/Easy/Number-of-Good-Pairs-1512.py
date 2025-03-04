'''

Number of Good Pairs - 1512

'''


def numIdenticalPairs(self, nums: List[int]) -> int:
        d = dict()
        count = 0

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                count += d[i]
                d[i] += 1

        return count


'''

The goal is to count the number of good pairs in the given list nums, where a pair (i, j) is 
considered good if nums[i] == nums[j] and i < j. The function efficiently computes this using 
a dictionary (d) to track the frequency of each number and a counter (count) to keep track of 
the total number of good pairs. As the function iterates through nums, it checks if the current
 number i is already in d. If not, it adds i to d with a frequency of 1. If i is already present, 
 it means all previous occurrences of i can form good pairs with the current occurrence, so the 
 count of good pairs is increased by d[i]. Then, d[i] is incremented to reflect the new occurrence. 
 Finally, the function returns count, which holds the total number of good pairs. 
 
'''