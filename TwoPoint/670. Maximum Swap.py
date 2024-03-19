class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num
        num = [i for i in str(num)]
        maxP = minP = len(num) - 1
        swap = [minP , maxP]

        for i in range(len(num)-2 , -1 , -1):
            if num[i] < num[maxP]:
                minP = i
                swap = [minP , maxP]
            elif num[i] > num[maxP]:
                maxP = i
                minP = i

        num[swap[0]], num[swap[1]] = num[swap[1]], num[swap[0]]
        return int("".join(num))

        