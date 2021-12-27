class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        numb = ''
        for i in digits:
            numb += str(i)
        new_numb = int(numb) + 1
        new_string = str(new_numb)
        return list(new_string)