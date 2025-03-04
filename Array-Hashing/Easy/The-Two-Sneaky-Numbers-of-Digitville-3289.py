'''

The Two Sneaky Numbers of Digitville - 3289

'''

def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = dict()
        arr = []

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                arr.append(i)

        return arr


'''

Quite simple, moniter the frequency of the integers, if greater than 2. 
Add to the array and return the answer

'''