class Solution:
    def longestPalindrome(self, s: str) -> str:
              
        n = len(s)
        res_len, res_idx = 0, 0

        for i in range(n):

            #odd like we have aba like subarrays
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > res_len:
                    res_len = right - left + 1    
                    res_idx = left
                left -= 1
                right += 1

            #even like we have aa like subarrays
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right -left + 1 > res_len:
                    res_len = right - left + 1
                    res_idx = left
                left -= 1
                right += 1
        
        return s[res_idx: res_idx + res_len]




