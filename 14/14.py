class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
            
        common = ""

        new_words = sorted(strs)

        first_word = new_words[0]
        last_word = new_words[-1]

        for i, letter in enumerate(first_word):
            
            if first_word[i] == last_word[i]:
                common += letter
            else:
                break

        return common