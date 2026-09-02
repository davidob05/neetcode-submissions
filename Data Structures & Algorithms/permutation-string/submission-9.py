class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False

        counts = [0] * 26

        for char in s1:
            counts[ord(char) - 97] += 1

        for i in range(n1):
            counts[ord(s2[i]) - 97] -= 1

        not_matched = 0
        for count in counts:
            if count != 0:
                not_matched += 1

        if not_matched == 0:
            return True

        for i in range(n2 - n1):
            out_idx = ord(s2[i]) - 97
            if counts[out_idx] == 0:
                not_matched += 1
            elif counts[out_idx] == -1:
                not_matched -= 1
            counts[out_idx] += 1

            in_idx = ord(s2[i + n1]) - 97
            counts[in_idx] -= 1
            if counts[in_idx] == 0:
                not_matched -= 1
            elif counts[in_idx] == -1:
                not_matched += 1

            if not_matched == 0:
                return True

        return False