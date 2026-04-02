class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elem in tokens:
            if elem in "+-*/":
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                
                if elem == "+":
                    stack.append(n1+n2)
                if elem == "-":
                    stack.append(n2 - n1)
                if elem == "*":
                    stack.append(n1*n2)
                if elem == "/":
                    stack.append(n2 / n1)
            else:
                stack.append(int(elem))

            print(stack)
        return int(stack[0])
            
        