class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_value = 0

        for n in num_set:
            if (n - 1) not in num_set:   # chỉ bắt đầu chuỗi mới tại đây
                length = 1
                while (n + length) in num_set:
                    length += 1
                max_value = max(max_value, length)

        return max_value