def main():
    
    get_fraction()
    

def get_fraction():
    while True:
        try:
            fuel = input("Fraction(X/Y): ")
            x,y = fuel.split("/")    
            x = int(x)
            y = int(y)
            
            if y == 0:
                raise ZeroDivisionError 
            if x > y:
                raise ValueError

            fraction = round((x/y)*100)
            
            if fraction <=1:
                print("E")
            elif fraction >=99:
                print("F")
            else:
                print(f"fraction={fraction}")
                break
            
        except ValueError:
            print("invalid input: denominator is big")
        except ZeroDivisionError:
            print("invalid input: denominator is zero")
            
                        
main()            
            