                                                # Syntax analyser project for compiler design fundamentals 
                                                #        MohammadMahdi Khani         40021973142
import os
def Base():
    global Error
    if (Lookahead=="<if>" or Lookahead=="<for>" or Lookahead=="<function>" or Lookahead=="<call>" or Lookahead=="<input>" or Lookahead=="<output>"):
        Syntax()
    elif ("<id" in Lookahead):
        Assignment()
    else:
        Error=1
        print("syntax error  "+Lookahead+" in "+str(Lookahead_pointer+1)+"th lexeme")
        exit()

def Syntax():
    global Error
    if (Lookahead=="<if>"):
        Match("<if>")
        Condition()
        Match("<{>")
        Base()
        Match("<}>")
        If_continue()

    elif (Lookahead=="<for>"):
        Match("<for>")
        Assignment()
        Match("<,>")
        Condition_for()
        Match("<,>")
        Match("<id")
        Operator_for()
        Match("<{>")
        Base()
        Match("<}>")

    elif (Lookahead=="<function>"):
        Match("<function>")
        Match("<id")
        Match("<(>")
        Match("</>")
        Function_call()
        Match("</>")
        Match("<)>")
        Match("<{>")
        Base()
        Match("<}>")

    elif (Lookahead=="<call>"):
        Match("<call>")
        Match("<id")
        Match("<(>")
        Match("</>")
        Function_call()
        Match("</>")
        Match("<)>")

    elif (Lookahead=="<input>"):
        Match("<input>")
        Match("<(>")
        Match("</>")
        Match("<id")
        Match("</>")
        Match("<)>")

    elif (Lookahead=="<output>"):
        Match("<output>")
        Match("<(>")
        Match("</>")
        Variable()
        Match("</>")
        Match("<)>")

    else:
        Error=1
        print("syntax error  "+Lookahead+" in "+str(Lookahead_pointer+1)+"th lexeme")
        exit()
    
def If_continue():
    if (Lookahead=="<else_if>"):
        Match("<else_if>")
        Condition()
        Match("<{>")
        Base()
        Match("<}>")
        Else_if_continue()
    elif (Lookahead=="<else>"):
        Match("<{>")
        Base()
        Match("<}>")
    else :
        return

def Else_if_continue():
    if (Lookahead=="<else>"):
        Match("<else>")
        Match("<{>")
        Base()
        Match("<}>")
    else :
        return

def Function_call():
    Variable()
    Call_continue()

def Call_continue():
    if (Lookahead=="<,>"):
        Match("<,>")
        Function_call()
    else :
        return
        
def Operator_for():
    global Error
    if (Lookahead=="<+>"):
        Match("<+>")
        Variable_for()
    elif (Lookahead=="<->"):
        Match("<->")
        Variable_for()
    elif (Lookahead=="<*>"):
        Match("<*>")
        Variable_for()
    elif (Lookahead=="<%>"):
        Match("<%>")
        Variable_for()
    elif (Lookahead=="<++>"):
        Match("<++>")
    elif (Lookahead=="<-->"):
        Match("<-->")
    else:
        Error=1
        print("syntax error  "+Lookahead+" in "+str(Lookahead_pointer+1)+"th lexeme")
        exit()

def Condition_for():
    Match("<id")
    Comparison()
    Variable_for()

def Variable_for():
    global Error
    if (Lookahead=="<id"):
        Match("<id")
    elif (Lookahead=="<int"):
        Match("<int")
    elif (Lookahead=="<float"):
        Match("<float")
    else:
        Error=1
        print("syntax error  "+Lookahead+" in "+str(Lookahead_pointer+1)+"th lexeme")
        exit()
    
def Assignment():
    Match("<id")
    Match("<=>")
    x()

def x():
    global Error
    if (Lookahead=="<number>" or Lookahead=="<string>"):
        Expr()
    elif (Lookahead=="<id" or Lookahead=="<int" or Lookahead=="<float" or Lookahead=='<"string>'):
        Operation()
    else :
        Error=1
        print("syntax error  "+Lookahead+" in "+str(Lookahead_pointer+1)+"th lexeme")
        exit()

def Expr():
    global Error
    if (Lookahead=="<number>"):
        Match("<number>")
        Match("<(>")
        y()
        Match("<)>")
    elif (Lookahead=="<string>"):
        Match("<string>")
        Match("<(>")
        Match('<"string">')
        Match("<)>")
    else :
        Error=1
        print("syntax error  "+Lookahead+" in "+str(Lookahead_pointer+1)+"th lexeme")
        exit()

def y():
    global Error
    if (Lookahead=="<int"):
        Match("<int")
    elif (Lookahead=="<float"):
        Match("<float")
    else :
        Error=1
        print("syntax error  "+Lookahead+" in "+str(Lookahead_pointer+1)+"th lexeme")
        exit()

def Operation():
    Variable()
    Operator()

def Operator():
    if (Lookahead=="<+>"):
        Match("<+>")
        Variable()
    elif (Lookahead=="<->"):
        Match("<->")
        Variable()
    elif (Lookahead=="<*>"):
        Match("<*>")
        Variable()
    elif (Lookahead=="<%>"):
        Match("<%>")
        Variable()
    elif (Lookahead=="<++>"):
        Match("<++>")
    elif (Lookahead=="<-->"):
        Match("<-->")
    else :
        return

def Condition():
    Variable()
    Comparison()
    Variable()

def Comparison():
    global Error
    if (Lookahead=="</=/>"):
        Match("</=/>")
    elif (Lookahead=="</!=/>"):
        Match("</!=/>")
    elif (Lookahead=="<<"):
        Match("<<")
    elif (Lookahead==">>"):
        Match(">>")
    elif (Lookahead=="<<="):
        Match("<<=")
    elif (Lookahead==">>="):
        Match(">>=")
    else :
        Error=1
        print("syntax error  "+Lookahead+" in "+str(Lookahead_pointer+1)+"th lexeme")
        exit()

def Variable():
    global Error
    if (Lookahead=="<id"):
        Match("<id")
    elif (Lookahead=="<int"):
        Match("<int")
    elif (Lookahead=="<float"):
        Match("<float")
    elif (Lookahead=='<"string">'):
        Match('<"string">')
    else :
        Error=1
        print("syntax error  "+Lookahead+" in "+str(Lookahead_pointer+1)+"th lexeme")
        exit()
    
def Match(symbol):
    global Error
    global Lookahead
    global Lookahead_pointer
    if ("<id" in Lookahead):
        Lookahead="<id"
    if (symbol==Lookahead):
        Lookahead_pointer+=1
        if (Lookahead_pointer<len(Tokens_list)):
            Lookahead=Tokens_list[Lookahead_pointer]
            if ("<float" in Lookahead):
                Lookahead="<float"
            elif ("<int" in Lookahead):
                Lookahead="<int"
            elif ("<id" in Lookahead):
                Lookahead="<id"
    else:
        Error=1
        print("syntax error  "+Lookahead+" in "+str(Lookahead_pointer+1)+"th lexeme")
        exit()
        return








os.system('cls')
Error=0
Lookahead_pointer=0
Tokens_file=open("token.txt")
Tokens_list=Tokens_file.read().split()
Lookahead=Tokens_list[0]
while Lookahead_pointer!=len(Tokens_list):
    Base()
if Error==0:
    print("Compiled successfuly (syntax without error)")