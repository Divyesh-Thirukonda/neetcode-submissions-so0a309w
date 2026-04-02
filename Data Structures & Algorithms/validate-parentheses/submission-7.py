class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairing = {
            "[": "]",
            "(": ")",
            "{": "}"
        }

        for el in s:
            if el in "[{(":
                stack.append(el)
            else:
                if el in "])}":
                    if stack and pairing.get(stack[-1]) != el:
                        return False
                    elif not stack:
                        return False
                    else:
                        stack.pop()
            print(stack)

        if len(stack) > 0:
            return False

        return True