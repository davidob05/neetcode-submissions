class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)> 1:
            return "ɀ".join(strs)
        else:
            if len(strs)==0:
                return "ɨ"
            return strs[0]
    def decode(self, s: str) -> List[str]:
        if s == "ɨ":
            return []
        strings = s.split("ɀ")
        return strings