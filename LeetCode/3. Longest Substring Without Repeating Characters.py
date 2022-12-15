class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0

        for i in range(len(s)):
            substring = ''
            for j in range(i, len(s)):
                if s[j] not in substring:
                    substring += s[j]
                else:
                    break
            answer = max(answer, len(substring))
        return answer
