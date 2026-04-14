#https://leetcode.com/problems/longest-substring-without-repeating-characters/

solution:
#using hash table and sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_map:
                #moving left pointer to avoid duplicates
                left = max(left, char_map[s[right]] + 1)

            char_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
        return max_length
