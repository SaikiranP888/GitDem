def maximum(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
        

m1 = maximum(3, 5, 2)
print("The maximum number is " + str(m1))
print("You are doing well")
    
    