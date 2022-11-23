"""O(n)"""
class solution:
    def getMaximumGenerated(self, n):
        num = [0] * (n + 2)
        num[1] = 1
        for i in range(2, n + 1):
            num[i] = num[i // 2] + num[(i // 2) + 1] * (i % 2)

        return max(num[:x + 1])