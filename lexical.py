                                           #قسمت اول پروژه اصول طراحی کامپایلر تحلیل گر لغوی 
                                                  #محمدمهدی خانی  ۴۰۰۲۱۹۷۳۱۴۲
import os
# تعریف توابع و سوئیچ کیس
def variable_checker(String):
    state=1
    while(1):
        for i in range(len(String)):
            match state:
                case 1:
                    if String[i]=="*":
                        i=i+1
                        state=2
                    else:
                        return False
                case 2:
                    if String[i]=="*":
                        i=i+1
                        if i==len(String):
                            return True
                        else:    
                            state=3
                    else:
                        return False
                case 3:
                    if (String[i]>='a' and String[i]<='z') or (String[i]>='A' and String[i]<='Z') or (String[i]=="_") or (String[i]>='0' and String[i]<='9'):
                        i=i+1
                        state=3
                        if i==len(String):
                            return True
                    else:
                        return False       

def condition1_checker(String):
    state=1
    while(1):
        for i in range(len(String)):
            match state:
                case 1:
                    if String[i]=="m":
                        i=i+1
                        state=2
                    else:
                        return False
                case 2:
                    if String[i]=="a":
                        i=i+1
                        state=3
                    else:
                        return False
                case 3:
                    if String[i]=="y":
                        i=i+1
                        if i==len(String):
                            return True
                        break
                    else:
                        return False

def condition2_checker(String):
    state=1
    while(1):
        for i in range(len(String)):
            match state:
                case 1:
                    if String[i]=="m":
                        i=i+1
                        state=2
                    else:
                        return False
                case 2:
                    if String[i]=="a":
                        i=i+1
                        state=3
                    else:
                        return False
                case 3:
                    if String[i]=="y":
                        i=i+1
                        state=4
                    else:
                        return False
                case 4:
                    if String[i]=="b":
                        i=i+1
                        state=5
                    else:
                        return False
                case 5:
                    if String[i]=="e":
                        i=i+1
                        if i==len(String):
                            return True
                        break
                    else:
                        return False                                                

def condition3_checker(String):
    state=1
    while(1):
        for i in range(len(String)):
            match state:
                case 1:
                    if String[i]=="o":
                        i=i+1
                        state=2
                    else:
                       return False
                case 2:
                    if String[i]=="t":
                        i=i+1
                        state=3
                    else:
                        return False
                case 3:
                    if String[i]=="h":
                        i=i+1
                        state=4
                    else:
                        return False
                case 4:
                    if String[i]=="e":
                        i=i+1
                        state=5
                    else:
                        return False
                case 5:
                    if String[i]=="r":
                        i=i+1
                        if i==len(String):
                            return True
                        break
                    else:
                        return False   

def loop_checker(String):
    state=1
    while(1):
        for i in range(len(String)):
            match state:
                case 1:
                    if String[i]=="r":
                        i=i+1
                        state=2
                    else:
                        return False
                case 2:
                    if String[i]=="e":
                        i=i+1
                        state=3
                    else:
                        return False
                case 3:
                    if String[i]=="p":
                        i=i+1
                        if i==len(String):
                            return True
                        break
                    else:
                        return False   

def number_checker(String):
    state=1
    while(1):
        for i in range(len(String)):
            match state:
                case 1:
                    if String[i]=="n":
                        i=i+1
                        state=2
                    else:
                        return False
                case 2:
                    if String[i]=="u":
                        i=i+1
                        state=3
                    else:
                        return False
                case 3:
                    if String[i]=="m":
                        i=i+1
                        if i==len(String):
                            return True
                        break
                    else:
                        return False   

def string_checker(String):
    state=1
    while(1):
        for i in range(len(String)):
            match state:
                case 1:
                    if String[i]=="a":
                        i=i+1
                        state=2
                    else:
                        return False
                case 2:
                    if String[i]=="l":
                        i=i+1
                        state=3
                    else:
                        return False
                case 3:
                    if String[i]=="p":
                        i=i+1
                        state=4
                    else:
                        return False                        
                case 4:
                    if String[i]=="h":
                        i=i+1
                        if i==len(String):
                            return True
                        break
                    else:
                        return False            

def function_checker(String):
    state=1
    while(1):
        for i in range(len(String)):
            match state:
                case 1:
                    if String[i]=="f":
                        i=i+1
                        state=2
                    else:
                        return False
                case 2:
                    if String[i]=="n":
                        i=i+1
                        if i==len(String):
                            return True
                        break
                    else:
                        return False           

def call_function_checker(String):
    state=1
    while(1):
        for i in range(len(String)):
            match state:
                case 1:
                    if String[i]=="c":
                        i=i+1
                        state=2
                    else:
                        return False
                case 2:
                    if String[i]=="a":
                        i=i+1
                        state=3
                    else:
                        return False
                case 3:
                    if String[i]=="l":
                        i=i+1
                        state=4
                    else:
                        return False                        
                case 4:
                    if String[i]=="l":
                        i=i+1
                        if i==len(String):
                            return True
                        break
                    else:
                        return False                               

def output_checker(String):
    state=1
    while(1):
        for i in range(len(String)):
            match state:
                case 1:
                    if String[i]=="s":
                        i=i+1
                        state=2
                    else:
                        return False
                case 2:
                    if String[i]=="h":
                        i=i+1
                        state=3
                    else:
                        return False
                case 3:
                    if String[i]=="o":
                        i=i+1
                        state=4
                    else:
                        return False                        
                case 4:
                    if String[i]=="w":
                        i=i+1
                        if i==len(String):
                            return True
                        break
                    else:
                        return False  

def input_checker(String):
    state=1
    while(1):
        for i in range(len(String)):
            match state:
                case 1:
                    if String[i]=="g":
                        i=i+1
                        state=2
                    else:
                        return False
                case 2:
                    if String[i]=="e":
                        i=i+1
                        state=3
                    else:
                        return False
                case 3:
                    if String[i]=="t":
                        i=i+1
                        if i==len(String):
                            return True
                        break
                    else:
                        return False   
def float_checker(String):
    state=1
    while(1):
        for i in range(len(String)):
            match state:
                case 1:
                    if String[i].isnumeric():
                        i=i+1
                        state=2
                    else :
                        return False
                case 2:
                    if String[i].isnumeric():
                        i=i+1
                        state=2
                    elif String[i]==".":
                        i=i+1
                        state=3
                    else:
                        return False 
                case 3:
                    if String[i].isnumeric():
                        i=i+1
                        state=3
                        if i==len(String):
                            return True
                    else:
                        return False 
def string_value_checker(String):
    if String[0]=='"' and String[-1]=='"':
        return True
    else:
        return False
#________________________________________________________________________________________________________________
# اضافه کردن فایل و خواندن از روی آن

os.system('cls')
File=open('program.txt')
token_file=open('token.txt' , '+w')
line=File.read().split("\n")
shenaseh = []
id_counter=1
for j in line:  
    String=j.split()
    # فرستادن کلمات به توابع برای چک کردن نوع آنها
    for i in String:
        if condition1_checker(i):
            token_file.write('<if>' + " ")

        elif condition2_checker(i):
            token_file.write('<else_if>' + " ")

        elif condition3_checker(i):
            token_file.write('<else>' + " ")

        elif loop_checker(i):
            token_file.write('<for>' + " ")  

        elif number_checker(i):
            token_file.write('<number>' + " ")  

        elif string_checker(i):
            token_file.write('<string>' + " ")

        elif function_checker(i):
            token_file.write('<function>' + " ")   

        elif call_function_checker(i):
            token_file.write('<call>' + " ")

        elif output_checker(i):
            token_file.write('<output>' + " ")   

        elif input_checker(i):
            token_file.write('<input>' + " ")

        elif string_value_checker(i):
            token_file.write('<"string">' + " ")

        elif i==',':
            token_file.write('<,>' + " ")

        elif i=='++':
            token_file.write('<++>' + " ")

        elif i=='--':
            token_file.write('<-->' + " ")

        elif i=='(':
            token_file.write('<(>' + " ")        

        elif i==')':
            token_file.write('<)>' + " ")

        elif i=='{':
            token_file.write('<{>' + " ")

        elif i=='}':
            token_file.write('<}>' + " ")

        elif i=='/':
            token_file.write('</>' + " ")

        elif i=='+':
            token_file.write('<+>' + " ")                                                                                         

        elif i=='-':
            token_file.write('<->' + " ")         

        elif i=='*':
            token_file.write('<*>' + " ")         

        elif i=='%':
            token_file.write('<%>' + " ")

        elif i=='=':
            token_file.write('<=>' + " ")

        elif i=='/=/':
            token_file.write('</=/>' + " ")

        elif i=='/!=/':
            token_file.write('</!=/>' + " ")    

        elif i=='<<':
            token_file.write('<<' + " ")

        elif i=='>>':
            token_file.write('>>' + " ")

        elif i=='<<=':
            token_file.write('<<=' + " ")

        elif i=='>>=':
            token_file.write('>>=' + " ")   

        elif i.isnumeric():
            token_file.write('<'+"int"+i+'>' + " ")

        elif variable_checker(i):
            inserted = False
            index = 0
            while(index < len(shenaseh)):
                if shenaseh[index]["name"] == i:
                    token_file.write(f"<id{shenaseh[index]["id"]}>" + " ")
                    inserted = True
                    break
                index += 1
            if not inserted:
                shenaseh.append({
                    "id": id_counter,
                    'name': i            
                })
                token_file.write('<id'+str(id_counter)+'>' + " ")    
                id_counter+=1  

        elif float_checker(i):
            token_file.write("<float"+i+">" + " ")        
        else:
            token_file.write('"'+i+'"'+' Is Not Defined!' + " ")
    token_file.write("\n")

token_file.close()
#________________________________________________________________________________________________________________
# نوشتن نتیجه در فایل پس از مشخص شدن توکن‌ها 

print("your program is compiled.")