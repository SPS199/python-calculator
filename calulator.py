print("1 ADD")
print("2 subract")
print("3 multiply")
print("4 divison")
print("5 percentage")
option = int(input("choose the sum:"))
result=0
if (option in [1,2,3,4,5]):
    num1=int (input("enter your  First number:"))
    num2=int (input("enter your  Second number:"))
    
if (option  == 1 ):
    result = num1 + num2
elif (option == 2):
    result = num1 - num2
elif(option == 3):
    result = num1 * num2
elif (option == 4):
    result = num1 / num2
elif(option == 5):
    result =  num1 * num2/100
else:
    print(" invalid number")

print(" the answer {}".format (result))



