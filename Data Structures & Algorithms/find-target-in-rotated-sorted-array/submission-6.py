class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Left pointer
        left = 0

        # Right pointer
        right = len(nums) - 1

        # Continue until pointers cross
        while left <= right:

            # Find the middle element
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Check if the LEFT half is sorted
            if nums[left] <= nums[mid]:

                # Target lies inside the left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                # Otherwise search the right half
                else:
                    left = mid + 1

            # Otherwise the RIGHT half is sorted
            else:

                # Target lies inside the right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                # Otherwise search the left half
                else:
                    right = mid - 1

        # Target not found
        return -1


         
