class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        order = 0
        for i in nums:
            if target == i or i > target:
                return order
            else:
                order += 1
        return order


obj = Solution()
result = obj.searchInsert([1, 3, 4, 6, 7], 5)
print(f'this is the result => {result}')
