class Solution:
    def isValid(self, s: str) -> bool:
        stack=['']
        
        for i in range(len(s)):
            print(i)
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                print("here")
                stack.append(s[i])
                continue
            if s[i]==')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            if s[i]=='}':
                if stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            if s[i]==']':
                print(i)
                if stack[-1]=='[':
                    stack.pop()
                else:
                    return False
        print(len(stack))
        return len(stack)==1