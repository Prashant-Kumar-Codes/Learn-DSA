class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        smallest, sec_smallest = float("inf"), float("inf")
        for i in prices:
            if i < smallest: smallest, sec_smallest = i, smallest
            else: sec_smallest = min(sec_smallest, i)
        
        left_money = smallest + sec_smallest

        return money - left_money if left_money <= money else money