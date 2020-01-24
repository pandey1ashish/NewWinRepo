from testclass import TestOne

print("Hello world")

def mathFun(a, b, str):
    if str == "add":
        return a+b
    elif str == "sub":
        return a-b
    elif str == "div":
        if b == 0:
            return "Devide by Zore"
        else:
            return a/b
    elif str == "multi":
        return a*b

#print("Addition: ", mathFun(2,4,"add"))
#print("Subtraction: ",mathFun(2,4,"sub"))
#print("Division: ",mathFun(2,0,"div"))
#print("Multiplication: ",mathFun(2,4,"multi"))

print('-------Import')
to = TestOne
print(to.__doc__)
print(to.name)
to.var_type(to, 10000, 55)