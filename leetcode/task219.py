a = 5
b = 9

c = abs(a - b)
print(f'this is the difference {c}')


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        found = False
        for i in range(0, len(nums)):
            if found:
                break
            for j in range(i + 1, len(nums)):
                tries = j
                print(f'j: {j} and nums[j]: {nums[j]} and nums[i]: {nums[i]}')
                if nums[i] == nums[j] and abs(nums[i] - nums[j]) <= k:
                    test = 1
                    found = True
                    test2 = 2
                    break
        return found


print('=' * 40)
obj = Solution()
print(obj.containsNearbyDuplicate([1, 2, 3, 1], 3))

print('=' * 40)
obj = Solution()
print(obj.containsNearbyDuplicate([1, 0, 1, 1], 1))

print('=' * 40)
obj = Solution()
print(obj.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
