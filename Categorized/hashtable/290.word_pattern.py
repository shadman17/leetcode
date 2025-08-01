class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        new_list = s.split()
        print(new_list)

        if len(new_list) != len(pattern):
            return False

        dic1 = {}
        dic2 = {}
        for i, value in enumerate(pattern):
            if value in dic1 and dic1[value] != new_list[i]:
                return False

            dic1[value] = new_list[i]

        for i, value in enumerate(new_list):
            if value in dic2 and dic2[value] != pattern[i]:
                return False

            dic2[value] = pattern[i]

        return True
