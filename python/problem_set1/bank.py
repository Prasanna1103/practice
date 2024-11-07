def banker(user):
    print(user)
    if user.startswith("hello"):
        print("$0")
    elif user.startswith("h"):
        print("$20")
    else :
        print("$100")        






user = input().lower()
banker(user)
