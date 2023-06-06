def coutPairs(self, nums: List[int], k: int) -> int:
    freq = Counter(gcd(num, k) for num in nums)
    ans = 0
    for x in freq:
        for y in freq:
            if x * y % k == 0:
                ans += freq[x]*freq[y]
        for num in nums:
            if num * num % k == 0:
                ans -= 1
    return ans // 2
