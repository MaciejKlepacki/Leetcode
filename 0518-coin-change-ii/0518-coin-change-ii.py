class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        T = [0 for _ in range(amount+1)]
        T[0] = 1
        for c in coins:
            for i in range(c, amount+1):
                T[i] += T[i-c]
        return T[-1]