class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False

                elif s[i] == ")":
                    if stack.pop(-1) != "(":
                        return False

                elif s[i] == "]":
                    if stack.pop(-1) != "[":
                        return False

                elif s[i] == "}":
                    if stack.pop(-1) != "{":
                        return False
        if len(stack) == 0:
            return True
        return False