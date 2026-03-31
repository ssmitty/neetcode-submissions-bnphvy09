class Solution:
    def evalRPN(self, token: List[str]) -> int:
        stack=[]
        for i in range(len(token)):
            if token[i]=='+':
                stack.append(stack.pop()+stack.pop())
            elif token[i]=='-':
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
            elif token[i]=='*':
                stack.append(stack.pop()* stack.pop())
            elif token[i]=='/':
                a,b=stack.pop(),stack.pop()
                stack.append(int(float(b/a)))
            else:
                print(token[i])
                
                stack.append(int(token[i]))
                print(stack)

        return int(stack[0])