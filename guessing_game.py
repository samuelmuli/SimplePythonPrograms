import random
random_num = random.randint(1,10)
for i in range(random_num):
    try:
        user_guess = int(input("guess a number between 1 and 10:>>"))
        if user_guess == random_num:
            i += 1
            if i<2:
                print(f"You are a F*** Genius, you got my guess in only {i} attempt")
                break
            else:
                print(f"You Got it! However, after {i} attempts")
                break
        elif user_guess>random_num:
            print("High, Try Again")
        else:
            print("Low, Try Again")
    except:
        print("Unsupported user input formart")
