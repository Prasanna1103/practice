import random

def main():
    level1 = int(input("level1: "))
    
    num_to_guess = random.randint(1,level1)
    
    while True:
        
        guess = int(input("Guess: "))
        
    
        if guess < num_to_guess:
            print("Too small")
        elif guess > num_to_guess:
            print("Too large")
        else:        
            print("Just Right")
            break


if __name__ == "__main__":
    main()        
            