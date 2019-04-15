#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list


# Now define the helper functions to push and pop values on the opstack (i.e, add/remove elements to/from the end of the Python list)
# Remember that there is a Postscript operator called "pop" so we choose different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

#from lucas on stackoverflow
def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False




def opPop():

    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

    if len(opstack)>0:
        ret=opstack.pop()
        return ret
    else:
        raise Exception('empty stack')
    pass

def opPush(value):

   x=str(value)

   val = intTryParse(x)
   if(x[0]=='('):
        v=value[1:len(value)-1]
        opstack.append(value)
   elif(val[1]):
       opstack.append(val[0])
   else :
        opstack.append(value)


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
    d = {name: value}
    #global setnum
    x=dictstack.pop()
    x[1][name]=value
    dictstack.append(x)


    #add name:value pair to the top dictionary in the dictionary stack. Keep the '/' in the name constant. 
    # Your psDef function should pop the name and value from operand stack and call the “define” function.

current=0
def lookup(name, scope):
    look="/"+name
    global current
    temp=current
    if scope=="dynamic":
        ret="Falses"
        for i in range(0,len(dictstack)):
            if dictstack[len(dictstack)-i-1][1].__contains__(look):
                ret=dictstack[len(dictstack)-i-1][1][look]


                if type(ret)==type([]):
                    if type(ret) == type([]):
                        current += 1
                        if (current - 1 < 0):
                            dictstack.append((0, {}))
                        else:
                            dictstack.append((current - 1, {}))

                        interpretSPS(ret, scope)
                        dictstack.pop()
                        ret =opPop()
                        current-=1

                return ret

            else:
                current -= 1


    elif scope=="static":
        searcher=len(dictstack)-1

        while(1):
            k=len(dictstack)
            if len(dictstack)-1<current:
                current-=1;
            else:
                if dictstack[searcher][1].__contains__(look):

                    ret=dictstack[searcher][1][look]

                    if type(ret) == type([]):

                        current += 1
                        if (current - 1 < 0):
                            dictstack.append((0, {}))
                        else:
                            dictstack.append((current - 1, {}))

                        interpretSPS(ret, scope)
                        dictstack.pop()
                        current-=1
                        ret = opPop()
                    current = temp
                    return ret
                elif(current!=0):
                    searcher=dictstack[searcher][0]
                    current=searcher
                else:
                    current=temp
                    return "Falses"

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
        raise Exception("divide by zero")
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
  #  if isInt(n1,n2):
    v= n1==n2
    opPush(v)

def lt():
    n2 = opPop()
    n1 = opPop()
    if isInt(n1,n2):
        v =n1<n2
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
        opstack.append(v-2)

def get():
    pos=1+opstack.pop()
    x=opstack.pop()
    v=x[pos]
    v=ord(v)
    opstack.append(v)

def getinterval():
    n2=opPop()
    n1=opPop()

    s=opPop()
    s=s[1:len(s)-1]

   # if(n1>n2):
    v = "("+s[n1:n2+n1]+")"
    opstack.append(v)

def put():
    asci=opPop()
    place=opPop()
    word=opPop()
    word2=word[1:len(word)-1]

    ret=word[0:place+1]+chr(asci)+word[place+2:len(word)]
    for x in range(0,len(opstack)):
        if opstack[x]==word:
            opstack[x]=ret
    for y in dictstack:
        for z in y:
            if y[z]==word:
                y[z]=ret

    #opPush(ret)
    return ret

def clear():
    del opstack[:]
    del dictstack[:]


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

def stack(scope):


    print("===========")
    print("  "+scope)
    print("===========")
    for i in range(1, len(opstack) + 1):
        if opstack[len(opstack) - i] == {}:
            print("--nostringval--")
        else:
            print(opstack[len(opstack) - i])
    for i  in range(0,len(dictstack)):
        #+str(dictstack[len(dictstack)-i-1][0])+
        print("=="+str(len(dictstack)-i-1)+"====="+str(dictstack[len(dictstack)-i-1][0])+"==")
        for x in dictstack[len(dictstack)-i-1][1] :
            print(x+" "+str(dictstack[len(dictstack)-i-1][1][x]) )

    print("===========")


def psIfelse(scope):
    global current
    ifFalse=opPop()
    ifTrue=opPop()
    val=opPop()
    pusher=0
    if type(val)!=type(True):
        opPush(val)
        opPush(ifTrue)
        opPush(ifFalse)
        Exception("Not a valid Boolean value")
    elif(type(ifTrue)==type([]))and (type(ifFalse)==type([])):
     #  current-=1
        if(val):
            interpretSPS(ifTrue,scope)
        else:
            interpretSPS(ifFalse,scope)
    else:
        opPush(val)
        opPush(ifTrue)
        opPush(ifFalse)

def psIf(scope):
    ifTrue=opPop()
    val=opPop()

    if(type(val)!=type(True)):
        opPush(val)
        opPush(ifTrue)
        Exception("invalid bool")
    elif(val):
        interpretSPS(ifTrue,scope)



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
        raise Exception("not a dictionary")

def end():
    dictPop()

def psDef():
    v1=opPop()
    v2=opPop()

    define(v2, v1)


func={"pop":pop,"add":add,"sub":sub,"mul":mul,"div":div,"eq":eq,"lt":lt,"gt":gt,"length":length,"get":get,"getinterval":getinterval,
      "put":put,"dup":dup,"copy":copy,"clear":clear,"exch":exch,"roll":roll,"dict":psDict,"begin":begin,"end":end,
      "def":psDef}
scopefunc={"ifelse":psIfelse,"if":psIf,"stack":stack}



def interpretSPS(code,scope): # code is a code array



    for x in code:

        if type(x)==type([]):
            opPush(x)
        else:
            #val=intTryParse(x)
            if scopefunc.__contains__(x):

                scopefunc.get(x)(scope)
            elif func.__contains__(x):
                func.get(x)()
            elif (type(x) == type(1)):
                opPush(x)
            elif(type(x)==type(True)):
                opPush(x)
            elif((x[0]=="("and x[len(x)-1]==")") or(x[0]=="/")or(type(x)==type([]))):
                opPush(x)

            else:

                look=lookup(x,scope)

                if (look!="Falses"):
                    opPush(look)
                #else:
                   # opPush(x)



def psFor(scope):
    doer=opPop()
    max=opPop()
    itter=opPop()
    strt=opPop()

    if type(max)==type(itter)==type(strt)==type(1)and type(doer)==type([]):
        if itter <0:
            while strt>=max:
                opPush(strt)
                interpretSPS(doer,scope)
                strt=strt+itter
        else:
            while strt<=max:
                opPush(strt)
                interpretSPS(doer,scope)
                strt=strt+itter

    else:
        Exception("not valid variables for psFor")


scopefunc["for"]=psFor


# go on writing test code for ALL of your code here; think about edge cases,
# and other points where you are likely to make a mistake.




import re
def tokenize(s):
    return re.findall("/?[a-zA-Z()][a-zA-Z0-9_()]*|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)


# complete this function
# The it argument is an iterator.
# The sequence of return characters should represent a list of properly nested
# tokens, where the tokens between '{' and '}' is included as a sublist. If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatching2(it):
    res = []
    for c in it:
        x=intTryParse(c)
        if c == '}':
            return res
        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code array for the inner
            # paranthesis, it will be appended to the list we are constructing
            # as a whole.
            res.append(groupMatching2(it))
        elif c == "true":
            res.append(True)
        elif c == "false":
            res.append(False)
        elif x[1]:
            res.append(x[0])
        else:
            res.append(c)
    return False


# Complete this function
# Function to parse a list of tokens and arrange the tokens between { and } braces
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested lists.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        x=intTryParse(c)

        if c=='}':  #non matching closing paranthesis; return false since there is
                    # a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(groupMatching2(it))
        elif c=="true":
            res.append(True)
        elif c=="false":
            res.append(False)

        elif x[1]:
            res.append(x[0])

        else:
            res.append(c)
    return res

input10= "/square { dup mul } def"



# Write the necessary code here; again write
# auxiliary functions if you need them. This will probably be the largest
# function of the whole project, but it will have a very regular and obvious
# structure if you've followed the plan of the assignment.
#


# Copy this to your HW4_part2.py file>
def interpreter(s,scope): # s is a string
     dictstack.append((0,{}))
   # if scope=="static":
     interpretSPS(parse(tokenize(s)),scope)
 #   else:
       # dyingterptetersps(parse(tokenize(s)),scope)



#interpreter(input0,"static")

def testInput20():
    input20 = '''/x 4 def /g {x stack} def   /f {/x 7 def g } def f'''
    interpreter(input20, "static")
    clear()

    interpreter(input20, "dynamic")
    clear()

def testInput21():
    # added the end
    input21='''/m 50 def
/n 100 def
/egg1 {/m 25 def n } def 
/chic {
 /n 1 def
 /egg2 { n } def
 m n
 egg1
 egg2
 stack } def
n
chic'''
    interpreter(input21, "static")

    clear()
    interpreter(input21, "dynamic")
    clear()

def testInput22():
    input22='''/x 10 def
/A { x } def
/C { /x 40 def A stack } def
/B { /x 30 def /A { x } def C } def
B'''
    interpreter(input22, "static")

    clear()

    interpreter(input22, "dynamic")

    clear()

def testInput23():
    input23='''/out true def
/xand { true eq {pop false} {true eq { false } { true } ifelse} ifelse
dup /x exch def stack} def
/myput { out dup /x exch def xand } def
/f { /out false def myput } def
false f'''
    interpreter(input23, "static")

    clear()

    interpreter(input23, "dynamic")

    clear()

def testInput24():
    input24="/x {/y 4 def y } def /z {x /x 5 def x stack} def z"

    interpreter(input24,"static")
    clear()
    interpreter(input24,"dynamic")
    clear()

    '''
    predicted outcome
    ==============
    static
    ============
    4
    5
    ============
    ====1====0
    /x 5
    ===0====0
    /x [...]
    /z [...]
    
    
    '''

def testInput25():
    input25="/x {/x {/x {/x 5 def x stack} def x} def x} def x"

    interpreter(input25, "static")
    clear()
    interpreter(input25, "dynamic")
    clear()

    '''
    expected output
    ========
    static
    =======
    5
    =======
    ==3===0==
    /x 5
    =2===0==
    /x  {/x 5 def x stack}
    ==1====0
    /x {/x  {/x 5 def x stack}}    
    ==0=====0===
    /x {/x {/x  {/x 5 def x stack}}}
    '''

def testInput26():
    input26="/x (cow) def /y (milk) def /z {/x (goat) def y x stack} def x z  "

    interpreter(input26, "static")
    clear()
    interpreter(input26, "dynamic")
    clear()

    '''
    expected output
    ========
    static
    =======
    goat
    milk
    cow
    =======

    ==1====0
    /x (goat)    
    ==0=====0===
    /x cow
    /y milk
    /z [..]
    '''

def testInput27():
    input27= "/dog {/fur (brown) def /age 12 def } def"

def testInput28():
    input28 = '''
            /class 5 def
            /yogurt { class } def 
            /fast { /class 7 def yogurt } def 
            fast
            /multiply { 
                /s {  6 mul} def
                s class mul
             } def
            /subtract { multiply class mul class sub } def
            multiply
            subtract
            fast
            stack
'''
    interpreter(input28, "static")
    clear()
    interpreter(input28, "dynamic")
    clear()

def testInput29():
    input29 = """
        /x 4 def 
        x 3 
        eq 
        {x 1 add /result exch def} 
        {x 4 eq 
            {x 2 add /result exch def} 
            {x 3 add /result exch def} 
        ifelse }
        ifelse
        result
        stack
"""
    interpreter(input29, "static")
    clear()
    interpreter(input29, "dynamic")
    clear()

def testInput210():
    input210='''
             /x 10 def
            /A { x } def
            /B { /x 30 def /A { x stack } def /C { /x 40 def A } def C } def
                B
    '''
    interpreter(input210, "static")
    clear()
    interpreter(input210, "dynamic")
    clear()


#testInput20() #T
#testInput21() #T
#testInput22() #T
#testInput23() #T
#testInput24() #T
#testInput25() #T
#testInput26() #T

#testInput28()
#testInput29()
testInput210()





input1 = "/square {dup mul } def  (square) 4 square dup 16 eq {(pass)} {(fail)} ifelse"
input42 ="/square {dup mul } def 5 square 25 eq  {(notWorked)} if stack"
#interpreter(input1)




#clear opstack and dictstackclear



#testing

'''

input2 ="""
(facto) dup length /n exch def
/fact {
 0 dict begin
 /n exch def
 n 2 lt
 { 1}
 {n 1 sub fact n mul }
 ifelse
 end
} def
n fact
"""
#interpreter(input2)  #stack =  facto 120

input3 = "/fact{0 dict begin /n exch def 1 n -1 1 {mul} for end} def 6 fact"
input31="0 dict begin /n exch def 1 n -1 1 {mul} for end"
#interpreter(input3) #720

input4 =  """
/lt6 { 6 lt } def
1 2 3 4 5 6 4 -3 roll
dup dup lt6 {mul mul mul} if
"""
#interpreter(input4)

input5 = " (CptS355_HW5) 4 3 getinterval (355) eq {(You_are_in_CptS355)} if "
#interpreter(input5)

input6 =  """
 /pow2 {/n exch def
 (pow2_of_n_is) dup 8 n 48 add put
 1 n -1 1 {pop 2 mul} for
 } def
 (Calculating_pow2_of_9) dup 20 get 48 sub pow2
 """
#interpreter(input6)


def testPut():
    opPush("(This is a test _)")
    dup()
    opPush("/s")
    exch()
    psDef()
    dup()
    opPush(15)
    opPush(48)
    put()
    if lookup("s") != "(This is a test 0)" or opPop()!= "(This is a test 0)":
        return False
    return True

#print(testPut())



def testInput1():
    interpreter(input1,"dynamic")

    if(opPop()=="(pass)"and opPop()==16 and opPop()=="(square)"):
        return True
    else:
        return False

#print(testInput1())
def testInput1():
    interpreter(input1)
    x=0
    if(opPop()=="(pass)"and opPop()==16 and opPop()=="(square)"):
        return True
    else:
        return False

def testInput2():
    interpreter(input2)
    if(opPop()==120and opPop()=="(facto)"):
        return True
    else:
        return False

def testInput3():
    interpreter(input3)
    if (opPop() ==  720 ):
        return True
    else:
        return False

def testInput4():

    interpreter(input4)
    if(opPop()==300and opPop()==6 and opPop()==2 and opPop()==1):
        return True
    else:
        return False

def testInput5():
    interpreter(input5)
    if(opPop()=="(You_are_in_CptS355)"):
        return True
    else:
        return False

def testInput6():
    interpreter(input6)
    if(opPop()==512 and opPop()=="(pow2_of_9_is)"and opPop()=="(Calculating_pow2_of_9)"):
        return True
    else:
        return False

def testInput7():
    input7="1 2 true {add} {mul} ifelse"
    interpreter(input7)
    if opPop()==3:
        return True
    return False

def testInput8():
    input8="1 2 lt {false} {true} ifelse {/n 5 def} {/n 6 def} ifelse n 5 mul"
    interpreter(input8)

    if opPop()==30:
        return True
    return False
def testInput9():
    input9="(abcdefghi) 2 3 getinterval dup 1 get"
    interpreter(input9)


    if opPop()==100 and opPop()=="(cde)":
        return True
    return False

def testInput10():
    input10="0 1 99 {1 add} for"
    interpreter(input10)

    y=True
    for x in range(1,100):
        if opPop()!=101-x:
            y=False
    return y

def testInput11():
    input11="99 -1 0 {1 add} for"
    interpreter(input11)

    y=True
    for x in range(1,100):
        if opPop()!=x:
            y=False
    return y

def testInput12():
    input12="99 -2 0 {1 add} for"
    interpreter(input12)
    i=2
    y=True
    while i <=100:
        if opPop()!=i:
            y=False
        i+=2
    return y




def testParse1():
   x= parse(['/pow2', '{', '/n', 'exch', 'def', '(Pow2_of_n_is)', 'dup', '8', 'n',
           '48', 'add', 'put', '1', 'n', '-1', '1', '{', 'pop', '2', 'mul', '}', 'for',
           '}', 'def', '(Calculating_pow2_of_9)', 'dup', '20', 'get', '48', 'sub',
           'pow2', 'stack'])
   if x==['/pow2', ['/n', 'exch', 'def', '(Pow2_of_n_is)', 'dup', 8, 'n', 48, 'add','put', 1, 'n', -1, 1, ['pop', 2, 'mul'], 'for'], 'def','(Calculating_pow2_of_9)', 'dup', 20, 'get', 48, 'sub', 'pow2', 'stack']:
       return True
   return False

def testPares2():
    x=parse(["(hello)","5","4","true","false","dup"])
    if x==["(hello)",5,4,True,False,"dup"]:
        return True
    return False

def main():

    testCases1=[('add',testAdd),("lookup",testLookup),("exch",testExch),("pop",testPop),('Begin-end',testBeginEnd),
               ("Roll",testRoll),("copy",testCopy),("clear",testClear),("Dict",testDict),("divide",testDivide),
               ("Mod",testMod),("gt",testGt),("eq",testEq),("Sub",testSub),("Mul",testMul),("dup",testDup),("Put",testPut),
               ("getInterval",testGetInterval),("pop",testPop),("get",testGet),("Length",testLength)]

    testCases2=[("testParse1",testParse1),("testParse2",testPares2),("input1",testInput1),("input2",testInput2),("input3",testInput3),("input4",testInput4),
                ("input5",testInput5),("input6",testInput6),("input7",testInput7),("input8",testInput8),("input9",testInput9),("input10",testInput10),
                ("input11",testInput11),("input12",testInput12)]


    print("part1")
    for x in testCases1:
        v=x[1]
        print(x[0]," success:",v())
        clear()

    print("part2")
    for y in testCases2:
        v=y[1]
        print(y[0]," success:",v())
        clear()

main()
'''
'''

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
    if opPop()=="(hel)":
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


'''