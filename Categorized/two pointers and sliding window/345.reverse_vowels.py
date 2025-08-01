class Solution:
    def reverseVowels(self, s: str) -> str:
        list_of_char = list(s)

        # vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        # vowel_list = "AEIOUaeiou"
        vowel_list = set("AEIOUaeiou")
        # vowel_list = {
        #     "a": "a",
        #     "e": "e",
        #     "i": "i",
        #     "o": "o",
        #     "u": "u",
        #     "A": "A",
        #     "E": "E",
        #     "I": "I",
        #     "O": "O",
        #     "U": "U",
        # }

        left, right = 0, len(list_of_char) - 1

        while left < right:
            if list_of_char[left] not in vowel_list:
                left += 1

            if list_of_char[right] not in vowel_list:
                right -= 1

            if list_of_char[left] in vowel_list and list_of_char[right] in vowel_list:
                list_of_char[left], list_of_char[right] = (
                    list_of_char[right],
                    list_of_char[left],
                )
                left += 1
                right -= 1

        return "".join(list_of_char)


s = Solution()
print(s.reverseVowels("Random"))
print(s.reverseVowels("IceCreAm"))
print(s.reverseVowels("leetcode"))
