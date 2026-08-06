class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Store all the triplets we find.
        # We use a list because we will keep APPENDING answers.
        result = []

        # Sort the array.
        # WHY?
        # Because two pointers only work on a sorted array.
        # Sorting lets us know:
        # Move left  -> Bigger number
        # Move right -> Smaller number
        nums.sort()

        # Fix ONE number at a time.
        # WHY?
        # Three Sum = One fixed number + Two Sum
        for i in range(len(nums)):

            # Skip duplicate fixed numbers.
            # WHY?
            # Example:
            # [-4,-1,-1,0,1,2]
            # If we start from both -1's,
            # we'll generate the same triplets twice.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Left pointer starts AFTER the fixed number.
            # WHY?
            # We already chose nums[i].
            # We need two DIFFERENT indices.
            left = i + 1

            # Right pointer starts from the last element.
            # WHY?
            # We want the biggest possible number first.
            right = len(nums) - 1

            # Continue searching until pointers meet.
            while left < right:

                # Current sum of the three numbers.
                total = nums[i] + nums[left] + nums[right]

                # We found a valid triplet.
                if total == 0:

                    # Store the answer.
                    result.append([nums[i], nums[left], nums[right]])

                    # Move both pointers.
                    # WHY?
                    # We already used these three numbers.
                    left += 1
                    right -= 1

                    # Skip duplicate numbers on the left.
                    # WHY?
                    # To avoid returning duplicate triplets.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate numbers on the right.
                    # WHY?
                    # Same reason.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # Sum is too small.
                # WHY?
                # Since the array is sorted,
                # move left to get a bigger number.
                elif total < 0:
                    left += 1

                # Sum is too large.
                # WHY?
                # Since the array is sorted,
                # move right to get a smaller number.
                else:
                    right -= 1

        # Return all unique triplets.
        return result
        