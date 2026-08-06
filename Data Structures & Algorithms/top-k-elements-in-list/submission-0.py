class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Count the frequency of every number.
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Create buckets.
        freq = [[] for i in range(len(nums) + 1)]

        # Put every number into its frequency bucket.
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Store the answer.
        result = []

        # Traverse from highest frequency to lowest.
        for i in range(len(freq) - 1, 0, -1):

            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result