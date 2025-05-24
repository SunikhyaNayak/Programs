def fun1():
    x=10
    y=20
    print(f"x is {x} and y is {y}")
    z=x
    x=y
    y=z
    print(f"x is {x} and y is {y}")
fun1()