"""O(n)"""
class solution(object):
    def maxProfit(self, prices):
        cur_max = 0       # переменная максимального профита
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:    # сравнение цены с предыдущей
                cur_max += prices[i] - prices[i-1]
        return cur_max        # возвращаем переменную