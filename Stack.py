class stackNode(object) :
    info, sig = None, None;
    
class Stack(object) :
    def __init__(self) :
        self.top = None;
        self.size = 0;
        
def pushStack (stack, element) :
    node = stackNode()
    node.info = element
    node.sig = stack.top
    stack.top = node
    stack.size += 1
    
def unstack (stack) :
    unstacked = stack.top.info
    stack.top = stack.top.sig
    stack.size -= 1
    return unstacked

def emptyStack (stack) :
    return stack.top is None

def getSize (stack) :
    return stack.size

def onTop (stack) :
    if stack.top is None :
        return None
    else :
        return stack.top.info
        
def sweepStack (stack) :
    auxStack = Stack()
    while not emptyStack(stack) :
        data = unstack(stack)
        print(data)
        pushStack(auxStack, data)
    
    while not emptyStack(auxStack) :
        data = unstack(auxStack)
        pushStack(stack, data)
        

        