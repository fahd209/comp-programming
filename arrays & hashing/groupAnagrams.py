class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        understanding:
            given a array of strs
            group the anagrams together into a 2d array

        approach:
            1. grouping with a hashmap
              - intilize a hashmap with key as string (Sorted string)
                and the value as a array for strings the match the 
                same sorted string
              - loop through the array and sort each string
              - if there is a key that matches add it the hashmap as value
              - loop through the hashmap and add each array into another array
                Time: O(n log n)
                space: O(n)
        """

        matching_strings = {}
        # anagram_groups = []

        for s in strs:
            sorted_str = "".join(sorted(s))
            # print(sorted_str)
            
            if sorted_str in matching_strings:
                matching_strings[sorted_str].append(s)
            else:
                matching_strings[sorted_str] = [s]
            
        return list(matching_strings.values())

        