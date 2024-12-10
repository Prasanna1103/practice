def main():
    gorcery_item = {}
    while True:
        try:
            item = input("Item: ").strip().lower()
            if item in gorcery_item:
                gorcery_item[item] +=1
            else:
                gorcery_item[item] =1
        except EOFError:
            print()
            break
        
            
    for item in sorted(gorcery_item):
        print(f"{gorcery_item[item]} {item.upper()}")  
            
            
main()            
            
                  