class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
            understanding:
                given array of nums every array in every test case will
                have a element that appears in more then half of the array
                I'm supposed to find that element

            linear time and o(n) space
            approach
            use a hashmap to count the occurance of each element then check 
            the hashmap to see which element has an occurance thats > [n / 2]

        """


        # my solution
        numCount = {}

        for n in nums:
            numCount[n] = numCount.get(n, 0) + 1

        for key in numCount:
            if (numCount[key]) >= (len(nums) / 2):
                return key


                # Time: O(n)
        # Space: O(1)
        # count = 0
        # res = 0

        # for n in nums:
        #     if res == n:
        #         count += 1
        #     elif res != n and count == 0:
        #         res = n
        #         count += 1
        #     else:
        #         count -= 1


        # for n in nums:
        #     numCount[n] = 1 + numCount.get(n, 0)
        #     res = n if numCount[n] > maxCount else res
        #     maxCount =  max(numCount[n], maxCount)
        # return res
        
        