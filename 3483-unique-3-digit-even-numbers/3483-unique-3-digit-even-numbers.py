class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        result = [False]*1000
        ans = 0
        for i in range(n):
            if digits[i]==0:
                continue
            for j in range(n):
                if j==i:
                    continue
                for k in range(n):
                    if k==j or k==i or digits[k]%2!=0:
                        continue
                    x = digits[i]*100 + digits[j]*10 + digits[k]
                    if not result[x]:
                        result[x] = True
                        ans += 1
        return ans
