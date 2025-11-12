#calculator
a=(int)(input("enter a number:"))
b=(int)(input("enter a number:"))
print("what operation do you wish to perform?")
print("1.addition\n2.subtraction\n3.multiplication\n4.division");
c=(int)(input("enter your choice:"))
res=0
match(c):
    case 1:
        res=a+b
        
    case 2:
        res=a-b
        
    case 3:
        res=a*b
        
    case 4:
        res=a/b
        

print(f"result={res}")