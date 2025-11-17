class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        return [s[i:i+k] if i + k < len(s) else (s[i:len(s)] + fill * (k - len(s) + i)) for i in range(0, len(s), k)]