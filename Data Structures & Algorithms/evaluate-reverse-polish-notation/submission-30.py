class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i]=="+":
                d1=stack.pop()
                d2=stack.pop()
                stack.append(int(d2)+int(d1))
            elif tokens[i]=="-":
                d1=stack.pop()
                d2=stack.pop()
                stack.append(int(d2)-int(d1))
            elif tokens[i]=="*":
                d1=stack.pop()
                d2=stack.pop()
                stack.append((d2)*(d1))
            elif tokens[i]=="/":
                print("fail",stack)
                d1=stack.pop()
                d2=stack.pop()
                stack.append(int((d2)/(d1)))
            else:
                stack.append(int(tokens[i]))
                print("here")
        print(stack)
        return stack[0]

            