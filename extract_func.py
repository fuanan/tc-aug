import re


code_str = '''
class Solution:
    def coutPairs(self, nums: List[int], k: int):
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
'''

final_str = re.sub('class Solution:\n', '', code_str)
final_str = re.sub('^[ ]{4}', '', final_str)
final_str = re.sub('\n[ ]{4}', '\n', final_str)
func_name = re.findall(r'def[ ]+([a-zA-Z_][a-zA-Z0-9_]*)\(', final_str)


print(final_str)
print("------------------------------")
print(func_name[0])
