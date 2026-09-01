class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        i = 0
        max_len = 0

        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1
            max_freq = max(max_freq, count[s[j]])

            if (j - i + 1) - max_freq > k:
                count[s[i]] -= 1
                i += 1

            max_len = max(max_len, j - i + 1)

        return max_len