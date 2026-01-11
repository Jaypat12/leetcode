'''

Top K Frequent Elements - 347

'''


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        b = k 
        arr = []
        
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        a = dict(sorted(d.items(),key=lambda item: item[1], reverse=True))

        for i in a.keys():
            if b > 0:
                arr.append(i)
                b -= 1

        return arr