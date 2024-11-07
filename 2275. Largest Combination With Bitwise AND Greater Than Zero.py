

""" 
1. Loop through each bit position (from 0 to 23, assuming 24-bit integers).
2. For each bit position, count how many numbers have that bit set to 1 using (num >> bit) & 1, which checks if the bit in num is set.
3. Track the maximum count of numbers with a common bit set across all bit positions.
"""


class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        max_count = 0
        for bit in range(24):  # Assuming integers are within 24-bit range
            count = sum((num >> bit) & 1 for num in candidates)
            max_count = max(max_count, count)
        #print(max_count)
        return max_count


if __name__ == '__main__':
    sol = Solution()
    sol.largestCombination([10,72,58,33,36,70,12,88,9,48,78,97,87,19,78,9,47,73])
    

        