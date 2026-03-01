class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if strs == []:
            return ""

        prefix = strs[0]

        j = len(prefix) - 1
        for s in strs[1:]:
            while not s.startswith(prefix[:j+1]):
                if j == 0:
                    return ""
                j -= 1

        return prefix[:j + 1]
    

# review
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        understanding:
            input:
                arrays: strs

            output:
                a string that has the longest common prefix of all strings

        approach:
            if the array is empty return an empty string

            first example
            prefix = strs[0]
            ["bat","bag","bank","band", "sand"]
        """

        if strs == []:
            return ""

        prefix = strs[0]

        for s in strs:
            while not s.startswith(prefix):
                if prefix != "":
                    prefix = prefix[:len(prefix) - 1]
                else:  
                    return ""

        return prefix
    
# review: optimized
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        understanding:
            input:
                arrays: strs

            output:
                a string that has the longest common prefix of all strings

        approach:
            if the array is empty return an empty string

            first example
            prefix = strs[0]
            ["bat","bag","bank","band", "sand"]
                                        ""
        
        time: O(1)
        space: O(n)
        """

        if strs == []:
            return ""

        prefix = strs[0]
        j = len(prefix) - 1
        for s in strs:
            while not s.startswith(prefix[:j+1]):
                if j == 0:
                    return ""
                j -= 1

        return prefix[:j+1]
                

        