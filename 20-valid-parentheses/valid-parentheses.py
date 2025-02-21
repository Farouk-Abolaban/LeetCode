class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hashmap = {")":"(","]":"[","}":"{"}

        for par in s: 
            if par in hashmap: 
                if stack and stack[-1] == hashmap[par]:
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(par)

        return True if not stack else False