class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        understanding:
            nums: array
            val: integer

            i have to remove all elements that are equal to val in place and return
            the number of elements are not equal to val

            ex 
            Input: nums = [0,1,2,2,3,0,4,2], val = 2
            Output: [0,1,3,0,4]
            Explanation: You should return k = 5 as we have 5 elements which are not equal to val = 2.

            in this example if we take all elements that are not equal to val and place them at the begining of
            the array and return k = 5 which means there is 5 elements in the begining of the array that
            are not equal to val the output will be array[:5] -> [0,1,3,0,4]

            approach:
                [0,1,3,0,4,2,2,2] val = 2
                           l
                                  r
        """

        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                if nums[l] == val:
                    temp = nums[r]
                    nums[r] = nums[l]
                    nums[l] = temp
                    l += 1
                else:
                    l += 1
        return l 

        