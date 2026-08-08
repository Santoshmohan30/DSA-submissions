class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Start searching from the entire array
        left = 0
        right = len(nums) - 1

        # Keep searching while there is a valid search space
        while left <= right:

            # Find the middle index
            mid = (left + right) // 2

            # If we found the target, return its index
            if nums[mid] == target:
                return mid

            # Check if the LEFT half is sorted
            if nums[left] <= nums[mid]:

                # Is the target inside the sorted left half?
                if nums[left] <= target < nums[mid]:
                    # Search the left half
                    right = mid - 1
                else:
                    # Search the right half
                    left = mid + 1

            # Otherwise, the RIGHT half must be sorted
            else:

                # Is the target inside the sorted right half?
                if nums[mid] < target <= nums[right]:
                    # Search the right half
                    left = mid + 1
                else:
                    # Search the left half
                    right = mid - 1

        # Target was not found
        return -1