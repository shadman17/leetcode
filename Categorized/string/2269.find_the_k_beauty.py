class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        str_num = str(num)
        new_string = ''

        for i in range(k):
            new_string += str_num[i]

        length = len(str_num)
        count = 0
        for i in range(k, length):
            if int(new_string)!=0 and num % int(new_string) == 0:
                count += 1

            new_string = new_string[1:]
            new_string += str(str_num[i])

        if int(new_string)!=0 and num % int(new_string) == 0:
            count += 1


        return count
    
    # def k_beauty(num: int, k: int) -> int:
    #     num_str = str(num)
    #     n = len(num_str)
    #     count = 0
        
    #     for i in range(n - k + 1):
    #         substring = num_str[i:i+k]
    #         divisor = int(substring)
            
    #         # Check if divisor is not zero and is a divisor of num
    #         if divisor != 0 and num % divisor == 0:
    #             count += 1
        
    #     return count


s = Solution()
print(s.divisorSubstrings(430043, 2))