class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Start with the widest possible container
        left = 0
        right = len(height) - 1

        # Store the best (maximum) area found so far
        maxArea = 0

        # Keep checking until the pointers meet
        while left < right:

            # Width = distance between the two bars
            width = right - left

            # Water height is limited by the shorter bar
            currentHeight = min(height[left], height[right])

            # Area = Width × Height
            area = width * currentHeight

            # Save the maximum area found so far
            maxArea = max(maxArea, area)

            # Move the shorter wall
            # (Only moving the shorter wall can possibly increase the area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea