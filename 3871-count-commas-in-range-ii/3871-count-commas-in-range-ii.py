class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        result = 0
        start = 1000
        while start<=n:
            result += (n-start+1)
            start*=1000
        return result