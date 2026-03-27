class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
            understand: 
                1. given an array nums
                2. return an array of the whole arrays product. except nums[i]
            
            example:
            input:   [1, 2, 3, 5]
            output:    [30, 15, 10, 6]

            approach:
                1. get prefix of the whole array where prefix[i] is the product of the whole array except it self
                2. get the suffix of the whole array where suffix[i] is the product of the whole array except it self
                3. then I'll multiply the suffix and prefix

            prefix: [1, 1, 2, 6]
            suffix: [30, 15, 5, 1]
            output: [30, 15, 10, 6]
        """



        # OPTIMAL suffix prefix approach
        n = len(nums)
        ans = [1] * n
        i = 0
        j = n - 1
        product_i = 1
        product_j = 1

        while i < n and j >= 0:
            ans[i] *= product_i
            ans[j] *= product_j

            product_i *= nums[i]
            product_j *= nums[j]


            i += 1
            j -= 1

        return ans

        # n = len(nums)
        # prefix = []
        # suffix = [1] * n
        # result = [0] * n

        # product_one = 1
        # for i in nums:
        #     prefix.append(product_one)
        #     product_one *= i

        # product_two = 1
        # for i in range(n - 1, -1, -1):
        #     suffix[i] = product_two
        #     product_two *=  nums[i]

        # print(prefix)
        # print(suffix)

        # for i in range(n):
        #     result[i] = prefix[i] * suffix[i] 

        # return result




class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n 
        post_product = [0] * n
        res = [0] * n

        prod1 = 1
        prod2 = 1

        # getting the prefix
        for i in range(n):
            prefix[i] = prod1
            prod1 *= nums[i]
        
        # getting suffix
        for i in range(n - 1, -1, -1):
            post_product[i] = prod2
            prod2 *= nums[i] 

        # prefix[i]: the product of all the items to the left of prefix[i] except prefix[i]
        # suffix[i]: the product of all the items to the right of suffix[i] except suffix[i]
        # multiplying prefix[i] and suffix[i] to get product of the array of except the item at i
        for i in range(n):
            res[i] = prefix[i] * post_product[i]

        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        right_prod = 1
        left_prod = 1
        L = 0
        R = n - 1

        res = [1] * n 

        while L < n:
            res[L] *= left_prod
            res[R] *= right_prod

            left_prod *= nums[L]
            right_prod *= nums[R]

            L += 1
            R -= 1


        return res
        