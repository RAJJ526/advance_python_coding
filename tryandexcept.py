try:
    x=10
    print(x)
except:
    print("an error is raised please check again")
else:
    print("everything is fine")
finally:
    print("end of except and try block")

#raise exception
x=-8
if x<0:
    raise Exception("sorry no numbers below zero")
else:
    print("no number is not less than 0")

#raise a type error if x is not an integer
# x="hello"
# if x is not int:
#     raise TypeError("only integers are allowed")

# y="hello"
# if y is not int:
#     raise SyntaxError("this is syntax error")

