
# -------------------------------- -------------------------------
mystr =  "taha khan"
print(mystr[::-1])
# --------------------------------------------------------------------------




# ------------------------------------------------------------------------------
mystr =  "abcdefghijklmnopqrstuvwxyz"
print(mystr[::2])
# ---------------------------------------------------------------------------




# count chr
# ---------------------------------------------------------
mystr =  "hello world of pakistan"

vl = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
for mystr in mystr:
    if mystr in vl:
        vl[mystr]+=1
        # print(mystr)

print(vl)
# ----------------------------------------------------------------



# --------------------------Functionn-----------------------
def greet_user(greet1, greet2, greet3):
    """Display a simple greeting"""
    print(greet1+greet2+greet3)
greet_user(int(input('Enter greet1:')), int(input('Enter greet2:')), int(input('Enter greet3:')))

# it will prrint of inputs sum
# chr will not be accepted

# -----------------------------------------------------------


# -----------------------------------function scoping----------------------------

def abc():
    x=90
    return x

x=30
print(x)
print(abc())

        # it will print
        # 30
        # 90
# ---------------------------------------------------------------



# -----------------------------------function scoping with list----------------------------

def abc2(x):
    x[0]=50


x=[10, 20, 30, 40]
abc2(x)
print(x)

        # it will print (because it is passing a referance)
        # [50, 20, 30, 40]

# ---------------------------------------------------------------




# -----------------------------------function scoping with list with slice----------------------------

def abc3(x):
    x[0]=50
    print(x)

x=[10, 20, 30, 40]
abc3(x[:])

print(x)

        # it will print(because slice make a copy)
        # [50, 20, 30, 40]
        # [10, 20, 30, 40]

# ---------------------------------------------------------------





