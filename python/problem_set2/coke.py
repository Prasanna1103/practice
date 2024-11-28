def main():
    change_owned = amount_due()
    print("Change owned: ", change_owned)


def amount_due():
    amount = 50
    accept_coin = [5, 10, 25]
    
    
    while amount > 0:
        print("Amount due: ", amount)
        insert_coin = int(input("Insert coin: "))
        if insert_coin in accept_coin:
            amount -= insert_coin

    return abs(amount)  

main()      

         
    