class Solution:
    def isValid(self, s: str) -> bool:
        paran = {')':'(', '}':'{', ']':'['}
        open_paran = paran.values()
        paran_stack = []

        for i in s:
            if i in open_paran:
                paran_stack.append(i)

            if i not in open_paran:
                if not paran_stack:
                    return False
                if paran_stack.pop() != paran[i]:
                    return False
            

        return len(paran_stack) == 0