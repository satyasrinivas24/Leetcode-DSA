class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(len(prefix)):
            for d  in strs[1:]:
                if i >= len(d) or d[i] != prefix[i]:
                    return prefix[:i]
        return prefix
        