
class Solution:
    def isPalindrome(self, x: int) -> bool:
        numb_str = str(x)
        rev_list = list(numb_str)
        rev_list.reverse()
        rev_str = ''
        for i in rev_list:
            rev_str += i
        print(numb_str)
        print(rev_str)
        if numb_str == rev_str:
            return True
        else:
            return False


obj = Solution()
print(obj.isPalindrome(121))
