class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs and len(strs) != 0:
            return ""
        elif not strs and len(strs) == 0:
            return " "
        return "|&".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        elif s == " ":
            return []
        return s.split("|&")