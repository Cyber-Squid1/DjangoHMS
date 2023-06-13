from datetime import datetime

x="10:00:00"
z=datetime.time(x,"%H:%M:%S")
print("x:",type(x))
print("z:",type(z))


# # y="10:00:00"
# # if x==y:
# #     print("Hi")


# a=datetime.now()
# b=datetime.strftime(a,"%H:%M:%S")
# print(type(b))

# import datetime

# x=datetime.time(10,00,00)
# print(x)
# print(type(x))