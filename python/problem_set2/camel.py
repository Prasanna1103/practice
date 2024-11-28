def main():
    snake_case = get_sta()
    print("snake_case: ",snake_case)
    
    
    
def get_sta():
    camel_case = input("camelCase: ")
    snake_case = []
    for s in camel_case:
        if s.isupper():
            snake_case.append("_")
            snake_case.append(s.lower())
        else:
            snake_case.append(s)    
            
    return ''.join(snake_case) 
    
            
        
    
main()   
 