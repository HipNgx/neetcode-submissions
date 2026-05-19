class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        if len(strs) == 0 :
            return 'error'
        for i in range(len(strs)) :
            if i == len(strs) - 1:
                s = s + strs[i]
                return s
            s = s + strs[i]
            s = s + 'hiep'
    def decode(self, s: str) -> List[str]:
        if s == 'error' :
            return []
        strs = s.split('hiep')
        return strs