num1= int(input("Input num 1:"))
num2= int(input("Input num 2:"))
opp= input ("Input operation:")
if opp=="+":
    print(num1+num2)
if opp=="-":
    print(num1-num2)
if opp=="/":
    if num2==0:
        print("Not defined")
    else:
        print("num1/num2")
if opp=="*":
    print(num1*num2)