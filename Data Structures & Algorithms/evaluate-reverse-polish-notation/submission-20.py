class Solution:
    def evalRPN(self, token: List[str]) -> int:
        stack=[]
        for i in range(len(token)):
            
            if token[i]=="+" and len(stack)>1:
                print("madeit")
                num1= stack.pop()
                num2= stack.pop()
                stack.append(num1+num2)
            elif token[i]=="-" and len(stack)>1:
                num1= stack.pop()
                num2= stack.pop()
                stack.append(num2-num1)
            elif token[i]=="*" and len(stack)>1:
                num1= stack.pop()
                num2= stack.pop()
                stack.append(num2*num1)
            elif token[i]=="/" and len(stack)>1:
                num1= stack.pop()
                num2= stack.pop()
                stack.append(int(float(num2/num1)))
            else:
                stack.append(int(token[i]))
                
        print(stack)
        return stack[0]