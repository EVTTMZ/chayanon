"""
#
#Part : Python Conditions
#
"""

a = 200
b = 50
if a > b :
    print("a > b is true.")
elif a < b:
    print("a < b is true.1")
elif a <= b:
    print("a <B is True.2")
elif a==b:
    print("a < b is True.3")
else:
    print("Nothing.")

if a < b: print("a < b is true.")

print("B") if a < b else print("A")

a = 200 
b = 30 
c = 500
if (a > b) and (c > a):
    print("both is True.")
if a > b or a > c: 
    print("some cond is True.")
if not a > b:
    print("Not")
if b > a:
    print("pass")
    pass

x = 50
if x > 10 :
    print("Let's go!")
    if x > 20:
        print("x > 20 is true1")
        if x > 20:
            print("x > 20 is true2")
            if x > 20:
                print("x > 20 is true3")
    else :
        print("x > 20 is True")
    

    