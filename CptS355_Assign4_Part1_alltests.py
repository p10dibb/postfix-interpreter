import re
from  interpreter_skeleton import *
#global variables
#opstack = []  #assuming top of the stack is the end of the list
#dictstack = []  #assuming top of the stack is the end of the list




##########################################
#------- Part 1 TEST CASES--------------
def printTestInput(funcName, input):
    print("\n-------------------------")
    print(funcName,":")
    print("input:", input)

def clearStacks():
    del opstack[:]
    del dictstack[:]

# 2 pts
def testDefine():
    clearStacks()
    printTestInput("define-1",'/n1 4 def n1')
    dictPush({})
    define("/n1", 4)
    if lookup("n1") != 4:
        print("FAIL - deduct:",-2)
        return False
    print("PASS")
    return True

# 3 pts
def testDefine2():
    clearStacks()
    printTestInput("define-2", '/n1 4 def /n1 5 def n1')
    dictPush({})
    define("/n1", 4)
    define("/n1", 5)
    if lookup("n1") != 5:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True

# 3 pts
def testLookup():
    clearStacks()
    printTestInput("lookup-1", '/v 3 def /v 4 def /v 5 def v ')
    dictPush({'/v':3})
    dictPush({'/v':4})
    dictPush({'/v':5})
    if lookup("v") != 5:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True

#2 pts
def testLookup2():
    clearStacks()
    printTestInput("lookup-2", '/a 355 def /a (355) def a')
    dictPush({'/a':355})
    dictPush({'/a':'(355)'})
    if lookup("a") != '(355)':
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

#Arithmatic operator tests
#2 pts
def testAdd():
    clearStacks()
    printTestInput("add", '9 -2 add')
    opPush(9)
    opPush(-2)
    add()
    if opPop() != 7:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

#2 pts
def testSub():
    clearStacks()
    printTestInput("sub", '10 2 sub')
    opPush(10)
    opPush(2)
    sub()
    x = opPop()
    if x == -8:
        print("FAIL - The order of the arguments for 'sub' are reversed - deduct:", -1)
        return False
    elif x != 8:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True


#2 pts
def testMul():
    clearStacks()
    printTestInput("mul", '2 40 mul')
    opPush(2)
    opPush(40)
    mul()
    if opPop() != 80:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

#2 pts
def testDiv():
    clearStacks()
    printTestInput("div", '12 3 div')
    opPush(12)
    opPush(3)
    div()
    x = opPop()
    if x == 0.25:
        print("FAIL - The order of the arguments for 'div' are reversed - deduct:", -1)
        return False
    elif x != 4:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

#2 pts
def testMod():
    clearStacks()
    printTestInput("mod", '10 4 mod')
    opPush(10)
    opPush(4)
    mod()
    x = opPop()
    if x == 0:
        print("FAIL - The order of the arguments for 'mod' are reversed - deduct:", -1)
        return False
    elif x != 2:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

#Comparison operators tests
# 2 pts
def testEq1():
    clearStacks()
    printTestInput("eq", '6 6 eq')
    opPush(6)
    opPush(6)
    eq()
    if opPop() != True:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

# 1 pts
def testEq2():
    clearStacks()
    printTestInput("eq", '(6) (6) eq')
    opPush('(6)')
    opPush('(6)')
    eq()
    if opPop() != True:
        print("FAIL - deduct:", -1)
        return False
    print("PASS")
    return True

# 3 pts
def testLt():
    clearStacks()
    printTestInput("lt", '3 6 lt')
    opPush(3)
    opPush(6)
    lt()
    if opPop() != True:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True
# 3 pts
def testGt():
    clearStacks()
    printTestInput("gt", '4 5 gt')
    opPush(4)
    opPush(5)
    gt()
    if opPop() != False:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True

# 4 pts
#String operator tests
def testLength():
    clearStacks()
    printTestInput("length", '(CptS355 HW4) length')
    opPush("(CptS355 HW4)")
    length()
    l = opPop()
    if l == 13:
        print("FAIL - (should not count paranthesis as part of the string) deduct:", -2)
        return False
    elif l != 11:
        print("FAIL - deduct:", -4)
        return False
    print("PASS")
    return True

# 5 pts
def testGet():
    clearStacks()
    printTestInput("get", '(CptS355 HW4) 10 get')
    opPush("(CptS355 HW4)")
    opPush(10)
    get()
    c = opPop()
    if c == 87:
        print("FAIL - (delimiter paranthesis are not part of the string; the 10th character is 4 ; not W) deduct:", -3)
        return False
    elif c== 'W' or c =='4':
        print("FAIL - (get should push the ASCII value of the character onto the stack) deduct:", -3)
        return False
    elif c != 52:
        print("FAIL - deduct:", -5)
        return False
    print("PASS")
    return True

# 5 pts
def testGetinterval():
    clearStacks()
    printTestInput("getinterval", '(CptS355 HW4) 8 3 getinterval')
    opPush("(CptS355 HW4)")
    opPush(8)
    opPush(3)
    getinterval()
    c = opPop()
    if c == '( HW)':
        print("FAIL - (delimiter paranthesis are not part of the string; getinterval returns (HW4) ; not ( HW);  deduct:", -3)
        return False
    elif c == 'HW4':
        print("FAIL - (the returned substring should be enclosed in paranthesis;  deduct:", -3)
        return False
    elif c != '(HW4)':
        print("FAIL - (In this test case 8 is the starting index for the substring and 3 is the length of the substring. deduct:", -5)
        return False
    print("PASS")
    return True

#stack manipulation functions
# 3 pts
def testDup():
    clearStacks()
    printTestInput("dup", '(CptS355 HW4) dup')
    opPush("(CptS355 HW4)")
    dup()
    if opPop()!=opPop():
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True
# 5 pts
def testExch():
    clearStacks()
    printTestInput("exch", '"/x" 5 exch')
    opPush("/x")
    opPush(5)
    exch()
    if opPop()!="/x" and opPop()!=5:
        print("FAIL - deduct:", -5)
        return False
    print("PASS")
    return True
# 2 pts
def testPop():
    clearStacks()
    printTestInput("pop", '10 pop')
    l1 = len(opstack)
    opPush(10)
    pop()
    l2 = len(opstack)
    if l1!=l2:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

# 5 pts
def testCopy():
    clearStacks()
    printTestInput("copy", 'true 1 (12) 3 4 3 copy')
    opPush(True)
    opPush(1)
    opPush('(12)')
    opPush(3)
    opPush(4)
    opPush(3)
    copy()
    if opPop()!=4 and opPop()!=3 and opPop()!='(12)' and opPop()!=4 and opPop()!=3 and opPop()!='(12)' and opPop()!=1:
        print("FAIL - deduct:", -5)
        return False
    print("PASS")
    return True

# 3 pts
def testClear():
    clearStacks()
    printTestInput("clear", '10 clear')
    opPush(10)
    opPush("/x")
    clear()
    if len(opstack)!=0:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True

#dictionary stack operators
# 3 pts
def testDict():
    clearStacks()
    printTestInput("dict", '1 dict')
    opPush(1)
    psDict()
    if opPop()!={}:
        print("FAIL - deduct:", -3)
        return False
    elif len(opstack)>0:
        print("FAIL - psDict should pop the size argumen from the stack ; deduct:", -2)
        return False
    print("PASS")
    return True

# 5 pts
def testBeginEnd():
    clearStacks()
    printTestInput("begin-end", '/x 3 def 1 dict begin /x 4 end x')
    dictPush({})
    opPush("/x")
    opPush(3)
    psDef()
    opPush(1)
    psDict()
    begin()
    opPush("/x")
    opPush(4)
    psDef()
    end() #SUT
    if lookup("x")!=3:
        print("FAIL - deduct:", -5)
        return False
    print("PASS")
    return True

# 5 pts
def testpsDef():
    clearStacks()
    printTestInput("psDef", '/x 10 def /x 20 def x end')
    dictPush({})
    opPush("/x")
    opPush(10)
    psDef()
    opPush("/x")
    opPush(20)
    psDef()

    x=lookup("x")
    if lookup("x")==10:
        print("FAIL - deduct:", -4, "(psDef should overwrite the existing definition : -5 +1 partial points)")
        return False
    elif lookup("x")!=20:
        print("FAIL - deduct:", -5)
        return False

    print("PASS")
    return True

# 5 pts
def testpsDef2():
    clearStacks()
    printTestInput("psDef-2", '/x 10 def 2 dict begin /y 20 def x')
    dictPush({})
    opPush("/x")
    opPush(10)
    psDef()
    opPush(2)
    psDict()
    begin()
    opPush("/y")
    opPush(20)
    psDef()
    if lookup("x")!=10:
        end()
        print("FAIL - deduct:", -5)
        return False
    end()
    print("PASS")
    return True

# 6 pts
def testpsDef3():
    clearStacks()
    printTestInput("psDef3", '/x 3 def 1 dict begin /x 30 def 1 dict begin /x 300 def end x')
    # define x in the bottom dictionary
    opPush("/x")
    opPush(3)
    psDef()
    opPush(1)
    psDict()
    begin()
    # define x in the second dictionary
    opPush("/x")
    opPush(30)
    psDef()
    opPush(1)
    psDict()
    begin()
    # define x in the third dictionary
    opPush("/x")
    opPush(300)
    psDef()
    end()
    if lookup("x")!=30:
        end()
        print("FAIL - deduct:", -6)
        return False
    end()
    print("PASS")
    return True



def main_part1():
    testCases = [('define',testDefine),('define2',testDefine2),('lookup',testLookup),('lookup2',testLookup2),('add', testAdd), ('sub', testSub),('mul', testMul),('div', testDiv), \
                 ('mod', testMod),('eq-1',testEq1),('eq-2',testEq2),('lt',testLt),('gt', testGt),  ('length', testLength),('get', testGet),('getinterval', testGetinterval),
                 ('dup', testDup), ('exch', testExch), ('pop', testPop), ('copy', testCopy), \
                 ('clear', testClear), ('dict', testDict), ('begin_end', testBeginEnd), ('psDef', testpsDef), ('psDef2', testpsDef2),('psDef3', testpsDef3)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return ('Some tests failed\n', failedTests)
    else:
        return ('All part-1 tests OK\n')


#if __name__ == '__main__':
 #   print(main_part1())

