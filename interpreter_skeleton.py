#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the helper functions to push and pop values on the opstack (i.e, add/remove elements to/from the end of the Python list)
# Remember that there is a Postscript operator called "pop" so we choose different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():

    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

    if len(opstack) !=0:
        ret=opstack.pop()
        return ret
    else:
        raise Exception('empty stack')
    pass

def opPush(value):

   x=str(value)
   if(x[0]=='('):
        v=value[1:len(value)-1]
        opstack.append(v)
   else :
        opstack.append(value)
   pass

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to define name, and to lookup a name
def dictPop():
    pass
    # dictPop pops the top dictionary from the dictionary stack.
    dictstack.pop();

def dictPush(d):
    pass
    dictstack.append(d)
    #dictPush pushes the dictionary ‘d’ to the dictstack. Note that, your interpreter will call dictPush only when Postscript “begin” operator is called. “begin” should pop the empty dictionary from the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):

    d={name:value}

    dictstack.append(d)

    #add name:value pair to the top dictionary in the dictionary stack. Keep the '/' in the name constant. 
    # Your psDef function should pop the name and value from operand stack and call the “define” function.

def lookup(name):
    b=False
    ret=0;

    L1=[]
    look='/'+name

    for x in range(0,len(dictstack)):
        v=dictstack.pop()
        if look in v:
            ret=v[look]
            b=True
        L1.append(v)

    for y in range(0,len(L1)-1):
        dictstack.append(L1.pop)

    if(b):
        return ret
    else:

        return False



    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.

#--------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, div, mod, eq, lt, gt
#Make sure to check the operand stack has the correct number of parameters and types of the parameters are correct.

def isInt(v1, v2):


    if type(v1)==type(v2)==type(1):
        return True
    else:
        opPush(v1)
        opPush(v2)
        raise Exception("not int")


def add():

    n2 = opPop()
    n1 = opPop()
    if isInt(n1,n2):
        v = n1 + n2
        opstack.append(v)

def sub():
    n2=opPop()
    n1=opPop()
    if isInt(n1,n2):
        v=n1-n2
        opstack.append(v)


def mul():
    n2 = opPop()
    n1 = opPop()
    if isInt(n1, n2):
        v = n1 *n2
        opstack.append(v)

def div():
    n2 = opPop()
    n1 = opPop()
    if n2==0:
        opPush(n1)
        opPush(n2)
        raise exception("divide by zero")
    else:
        isInt(n1, n2)
        v = n1 / n2
        opstack.append(v)

def mod():
    n2 = opPop()
    n1 = opPop()
    if isInt(n1,n2):
        v= n1%n2
        opstack.append(v)

def eq():
    n2 = opPop()
    n1 = opPop()
    if isInt(n1,n2):
        v= n1==n2
        opPush(v)

def lt():
    n2 = opPop()
    n1 = opPop()
    if isInt(n1,n2):
        v =n1!=n2
        opstack.append(v)

def gt():
    n2 = opPop()
    n1 = opPop()
    if isInt(n1,n2):
        v = n1 > n2
        opstack.append(v)

#--------------------------- 15% -------------------------------------
# String operators: define the string operators length, get, getinterval, put
def length():
    x=opPop()
    if type(x)==type("ppp"):
        v=len(x)
        opstack.append(v)

def get():
    pos=opstack.pop()
    x=opstack.pop()
    v=x[pos]
    v=ord(v)
    opstack.append(v)

def getinterval():
    n1=opPop()
    n2=opPop()
    s=opPop()
    if(n1>n2):
        v = s[n2:n1]
        opstack.append(v)

def put():
    asci=opPop()
    place=opPop()
    word=opPop()

    ret=word[0:place]+chr(asci)+word[place+1:len(word)]
    return ret

#--------------------------- 25% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, pop, clear, exch, roll, stack
def dup():
    v=opPop()
    opstack.append(v)
    opstack.append(v)

def copy():
    x=opPop();
    if(x<=len(opstack)):
        for i in range(len(opstack)-x,len(opstack)):
            opstack.append(opstack[i])

def pop():
    return opPop()

def clear():
    for i in range(0,len(opstack)):
        opstack.pop();

def exch():
    n1=opPop()
    n2=opPop()
    opstack.append(n1)
    opstack.append(n2)

def roll():
    n1=opPop()
    n2=opPop()
    L1=[]
    L2=[]
    if isInt(n1,n2):
        if n1>0:
            for i in range(0,n1):
                L1.append(opPop())
            for j in range(0,(n2-n1)):
                L2.append(opPop())

            for x in range(0,len(L1)):
                opstack.append(L1.pop())
            for y in range(0,len(L2)):
                opstack.append(L2.pop())

        elif n1<0:
            v=n2-(0-n1)
            for i in range(0, v):
                L1.append(opPop())
            for j in range(0, (n2 - v)):
                L2.append(opPop())

            for x in range(0, len(L1)):
                opstack.append(L1.pop())
            for y in range(0, len(L2)):
                opstack.append(L2.pop())

def stack():

    for i in range(1,len(opstack)+1):
        if opstack[len(opstack)-i]=={}:
            print("--nostringval--")
        else:
            print(opstack[len(opstack)-i])

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    opPop()
    opPush({})

def begin():
    v=opPop()
    if type(v)==type(dict()):
        dictPush(v)
    else:
        opPush(v)
        raise exception("not a dictionary")

def end():
    dictPop()

def psDef():
    v1=opPop()
    v2=opPop()

    define(v2, v1)


# --------------------------------------------------------------------
## Sample tests #
# --------------------------------------------------------------------
def testAdd():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    return True

def testLookup():
    opPush("/n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3:
        return False
    return True

def testExch():
    opPush(10)
    opPush("/x")
    exch()
    if opPop()!=10 and opPop()!="/x":
        return False
    return True

def testPop():
    l1 = len(opstack)
    opPush(10)
    pop()
    l2= len(opstack)
    if l1!=l2:
        return False
    return True

def testRoll():
    clear()
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(6)
    opPush(4)
    opPush(-1)
    roll()
    if opPop()==3 and opPop()==6 and opPop()==5 and opPop()==4 and opPop()==2 and opPop()==1:
        return True
    return False

def testCopy():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    x=opstack
    copy()
    y=opstack
    if opPop()!=5 and opPop()!=4 and opPop()!=5 and opPop()!=4 and opPop()!=3 and opPop()!=2:
        return False
    return True

def testClear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opstack)!=0:
        return False
    return True

#dictionary stack operators
def testDict():
    opPush(1)
    psDict()
    if opPop()!={}:
        return False
    return True

def testBeginEnd():
    opPush("/x")
    opPush(3)
    psDef()
    opPush({})
    begin()
    x=dictstack
    opPush("/x")
    opPush(4)
    psDef()
    end()
    if lookup("x")!=3:
        return False
    return True

def testDivide():
    opPush(4)
    opPush(2)
    div()
    if opPop() != 2.0:
        return False
    return True

def testMod():
    opPush(4)
    opPush(2)
    mod()
    if opPop() != 0:
        return False
    return True

def testGt():
    opPush(4)
    opPush(2)
    gt()
    if opPop() != True:
        return False
    return True

def testEq():
    opPush(4)
    opPush(2)
    eq()
    x=opstack
    if opPop() != False:
        return False
    return True

def testSub():
    opPush(4)
    opPush(2)
    sub()
    if opPop() != 2:
        return False
    return True

def testMul():
    opPush(4)
    opPush(2)
    mul()
    if opPop() != 8:
        return False
    return True

def testDup():
    opPush(2)
    dup()
    if opPop()==opPop()==2:
        return True
    else:
        return False

def testPut():
    opPush("hello")
    opPush(1)
    opPush(111)

    if put()=="hollo":
        return True
    else:
        return False

def testGetInterval():
    opPush("(hello)")
    opPush(0)
    opPush(3)
    getinterval()
    x=opstack
    if opPop()=="hel":
        return True
    else:
        return False

def testPop():
    opPush(5)
    if pop()==5:
        return True
    else:
        return False

def testGet():
    opPush("(Hello)")
    opPush(1)
    get()
    if pop()==101:
        return True
    else:
        return False

def testLength():
    opPush("(hello)")
    length()
    if pop()==5:
        return True
    else:
        return False



# go on writing test code for ALL of your code here; think about edge cases,
# and other points where you are likely to make a mistake.

def main():

    testCases=[('add',testAdd),("lookup",testLookup),("exch",testExch),("pop",testPop),('Begin-end',testBeginEnd),
               ("Roll",testRoll),("copy",testCopy),("clear",testClear),("Dict",testDict),("divide",testDivide),
               ("Mod",testMod),("gt",testGt),("eq",testEq),("Sub",testSub),("Mul",testMul),("dup",testDup),("Put",testPut),
               ("getInterval",testGetInterval),("pop",testPop),("get",testGet),("Length",testLength)]


    for x in testCases:
        v=x[1]
        print(x[0]," success:",v())






main()




'''
def main_part1():
    testCases = [('define',testDefine),('lookup',testLookup),('add', testAdd), ('sub', testSub),('mul', testMul),
                 ('div', testDiv),  ('mod', testMod), ('lt', testLt), ('gt', testGt), ('eq', testEq),
                 ('length', testLength),('get', testGet), ('getinterval', testGetinterval),
                 ('put', testPut), ('dup', testDup), ('exch', testExch), ('pop', testPop), ('roll', testRoll),
                 ('copy', testCopy), ('clear', testClear), ('dict', testDict), ('begin', testBeginEnd),
                 ('psDef', testpsDef), ('psDef2', testpsDef2)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return ('Some tests failed', failedTests)
    else:
        return ('All part-1 tests OK')

if __name__ == '__main__':
    print(main_part1())
'''