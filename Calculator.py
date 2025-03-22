import operator
import numpy as np
import ArrayStack
 
 
class Calculator:
    def __init__(self):
        self.dict = None #ChainedHashTable.ChainedHashTable(DLList.DLList)
 
    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)
 
    def matched_expression(self, s: str) -> bool:
        if s.find (")") and s.find("(") == -1: #use find()
                return True
 
        hashmap = {")":"("}
        stack = []
 
        for i in s:
            if i not in "()":
                continue
            if i in hashmap:
                if stack and stack[-1] == hashmap[i]:
                    stack.pop()
                else:
                    print(i)
                    return False
            else:
                stack.append(i)
                #print(stack)
    
        return True if not stack else False
 
 
    
        # todo
        
        #pass
 
    def build_parse_tree(self, exp: str) -> str:
        # todo
        pass
 
    def _evaluate(self, root):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        # todo
        pass
 
    def evaluate(self, exp):
        parseTree = self.build_parse_tree(exp)
        return self._evaluate(parseTree.r)
 
g = Calculator()
print(g.matched_expression("(3+x)(2(x-1)+7)"))
