def calulator(x,y,z):
    x,z = float(x),float(z)
    if y == '+':
        result  =(x)+(z)
    elif y == '-':
        result = (x)-(z)
    elif y =='/':
        result = (x)/(z)
    elif y== "*":
        result = (x)*(z)
    else:
        print()
        return
    print(f"{result:.2f}")    

x,y,z = input().split()
calulator(x,y,z)
