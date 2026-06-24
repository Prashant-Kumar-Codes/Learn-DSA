class Solution:
    def isValid(self, s: str) -> bool:
        paran = {')':'(', '}':'{', ']':'['}
        paran_stack = []

        for i in s:
            if i in paran:
                if not paran_stack:
                    return False
                if paran_stack.pop() != paran[i]:
                    return False
            else:
                paran_stack.append(i)

        return not paran_stack