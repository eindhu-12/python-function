# -----------------------------fibonacci --------------------
print("fibonacci")
def fib(m):
    if( m==0 or m==1):
        return m
    return (fib(m-1)+fib(m-2))

print(fib(6))
print()


# -----------------------------factorial--------------------
print("factorial")
def fact(n):
    if(n==0 or n==1):
        return n
    return n*fact(n-1)
print(fact(5))

print()
# ------------------------------------------------------
num1=80
def fun():
    # global num1
    num1=90
    # global()=95
    print("Num is:-",num1)
fun()
print("output:-",num1)

print()

# ------orbitary arguments-------------
def sumOf(a,b,*args):
    res=0
    res=a+b
    for i in args:
        res+=i
    return res
print(sumOf(5,6,3,2))

# -------------keyword orbitary arguments-----------
#pass by value
#pass by reference


