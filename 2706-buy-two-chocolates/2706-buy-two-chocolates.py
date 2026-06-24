class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sorted_prices = sorted(prices)
        low_price = sorted_prices[0] + sorted_prices[1]
        if money >= low_price: return money - low_price
        else: return money