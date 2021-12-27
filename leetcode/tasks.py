# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         numb_str = str(x)
#         rev_list = list(numb_str)
#         rev_list.reverse()
#         rev_str = ''
#         for i in rev_list:
#             rev_str += i
#         print(numb_str)
#         print(rev_str)
#         if numb_str == rev_str:
#             return True
#         else:
#             return False
#
#
# obj = Solution()
# print(obj.isPalindrome(121))


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         numb_str = str(x)
#         rev_list = list(numb_str)
#         rev_list.reverse()
#         rev_str = ''
#         for i in rev_list:
#             rev_str += i
#         print(numb_str)
#         print(rev_str)
#         if numb_str == rev_str:
#             return True
#         else:
#             return False
#
#
# obj = Solution()
# print(obj.isPalindrome(121))


# class Solution:
#     def romanToInt(self, s: str) -> int:
#         dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         a_list = list(s)
#         print(f'the value of array {a_list}')
#         summary = 0
#         for i in range(0, len(a_list)):
#             key = a_list[i]
#             val = dic.get(key)
#             if (key == 'I' and i + 1 < len(a_list) and (a_list[i + 1] in ["X", "V"])) or (
#                     key == 'X' and i + 1 < len(a_list) and (a_list[i + 1] in ["L", "C"])) or (
#                     key == 'C' and i + 1 < len(a_list) and (a_list[i + 1] in ["D", "M"])):
#                 val = -1 * val
#             summary += val
#         return summary
#
#
# obj = Solution()
# result = obj.romanToInt('IX')
# print(f'this is the result value : {result}')

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.


# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         size = len(strs)
#         f_word = strs[0]
#         if size == 1:
#             return f_word
#         order = -1
#         move = True
#
#         for i in range(0, len(f_word)):
#             for ow in range(1, size):
#                 if len(strs[ow]) < i + 1:
#                     move = False
#                     break
#                 elif f_word[i] != strs[ow][i]:
#                     move = False
#                     break
#                 else:
#                     continue
#             order = i
#             if move is False:
#                 order -= 1
#                 print(f'this is the max order reached before break : {order}')
#                 break
#         else:
#             print(f'Order reached : {order}')
#
#         if order == -1:
#             return ""
#         else:
#             return f_word[0:order + 1]
#
#
# obj = Solution()
# # target = obj.longestCommonPrefix(["a", "ac"])
# # target = obj.longestCommonPrefix(["ab", "a"])
# # target = obj.longestCommonPrefix(["flower", "flower", "flower"])
# target = obj.longestCommonPrefix(["flower", "flow", "flight"])
# print(f'The searching part of word equals to {target}')


class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        if len(s_list) % 2 != 0:
            print(f'the string is not given in pairs')
            return False
        dictionary = {"{": 0, "[": 0, "(": 0, ")": 0, "]": 0, "}": 0}
        for i in s_list:
            dictionary[i] += 1
            if dictionary["{"] < dictionary["}"] \
                    or dictionary["["] < dictionary["]"] \
                    or dictionary["("] < dictionary[")"]:
                return False
        if dictionary["{"] != dictionary["}"] \
                or dictionary["["] != dictionary["]"] \
                or dictionary["("] != dictionary[")"]:
            return False
        return True


obj = Solution()
print('=' * 40)
result = obj.isValid('([{}])')
print(f'The answer comes as being {result}')

print('=' * 40)
result = obj.isValid('()[]')
print(f'The answer comes as being {result}')

print('=' * 40)
result = obj.isValid('{}[]')
print(f'The answer comes as being {result}')

print('=' * 40)
result = obj.isValid("(]")
print(f'The answer comes as being {result}')

print('=' * 40)
result = obj.isValid("([)]")
print(f'The answer comes as being {result}')

print('=' * 40)
result = obj.isValid("(){}}{")
print(f'The answer comes as being {result}')

print('=' * 40)
result = obj.isValid("(([]){})")
print(f'The answer comes as being {result}')


