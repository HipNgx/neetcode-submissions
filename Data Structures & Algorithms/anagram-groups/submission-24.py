class Solution:

    def Anagrams(self, x, y):
        return sorted(x) == sorted(y)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = []

        while len(strs) > 0:

            temp = []
            n = strs[0]

            temp.append(n)

            remove_list = [n]

            for x in strs[1:]:

                if self.Anagrams(n, x):
                    temp.append(x)
                    remove_list.append(x)

            ans.append(temp)

            for word in remove_list:
                strs.remove(word)

        return ans