class Solution:
    def simplifyPath(self, path: str) -> str:
        stacks = []
        temp = ""
        for i in path + "/":
            if i == "/":
                if temp == "..":
                    if stacks: #if its .. and stacks is not empty we pop it
                        stacks.pop()
                    else: # we can jump this line it won't have any effect
                        pass #if stacks is empty we just pass it
                elif temp and temp != ".":
                    stacks.append(temp)
                temp = ""
            else:
                temp += i #first we add elements zt are between / to temporary variable

        return "/" + "/".join(stacks)   