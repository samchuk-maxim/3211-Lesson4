# def black(*args):
#     print("Show params")
#     for argument in args:
#         print("\t", argument)
#
# black("QWErtyu",12342,"ipuerjhgj",True,False)


# def sum(*args):
#     sum=0
#     for argument in args:
#         sum+=argument
#     return sum
#
# print("Result",sum(4,2,5,1,3,5,6,7,2))

# def printHuman(**kwargs):
#     print("Print human",kwargs)
#
# printHuman(name="sads",surname="Kek")


# def superPrint(*args,**kwargs):
#     for arguments in args:
#         print("\t",arguments)
#
#     for argumentsWithName in kwargs:
#         print("\t\t",argumentsWithName)
#
# superPrint(2,"32",12,"123",True,Name="Maxim",Surname="Sumchuk")

currents={
    "USD":41,
    "EUR":47
}

def convert(**kwargs):
    current=currents.get(kwargs.get("current"))
    return kwargs.get("amount")/current

print(convert(current="USD",amount=90))