a=10

def fun():
    global a
    a=20
    print("inside fun",a)

fun()
print("outside fun",a)