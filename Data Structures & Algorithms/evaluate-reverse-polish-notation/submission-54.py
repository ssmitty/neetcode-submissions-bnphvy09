class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        i=0
        le=len(tokens)-1
        while i<=len(tokens)-1:
            while i<le and tokens[i]!="+" and tokens[i]!="-" and tokens[i]!="*" and tokens[i]!="/":
                stack.append(tokens[i])
                i+=1
            if tokens[i]=="+":
                f=int(stack.pop())
                s=int(stack.pop())
                stack.append(f+s)
            elif tokens[i]=="-":
                f=int(stack.pop())
                s=int(stack.pop())
                stack.append(s-f)
            elif tokens[i]=="*":
                f=int(stack.pop())
                s=int(stack.pop())
                stack.append(s*f)
            elif tokens[i]=="/":
                f=int(stack.pop())
                s=int(stack.pop())
                stack.append(int(s/f))
            else:
                stack.append(int(tokens[i]))
                break
            i+=1 
        return stack[0]





            
        