def vowel_remove():
    vowelletter = ['a', 'e', 'i', 'o', 'u']
    str = input("Name ")

    for s in str:
        if s.lower() in vowelletter:
            None
        else:
            print(s, end="")
    print()

vowel_remove()            
