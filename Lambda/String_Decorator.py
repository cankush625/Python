def decorfun(fun) :
    def inner(n) :
        result = fun(n)
        result = result + " how are you ?"
        return result
    return inner

@decorfun
def hello(name) :
    return "Hello "+name

print(hello("Ankush"))

'''By Ankush Chavan'''