'''

Jewels and Stones - 771

'''


def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in stones:
            if i in jewels:
                count += 1

        return count

'''

The answer is straight forward, you want to see if each stone in stones,
is a jewel or not. You simply just count the amount of jewels found in stones

'''


