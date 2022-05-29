#import random

def scores_users():
    scores = 50
    return scores
    
def guessed_number():
    #random_num = random.randint(0,100)
    random_num = 10
    return random_num
    
def inputted_number(enter_num):
    sum_scores = scores_users()
    if enter_num != guessed_number():
        print("You are Guessing Wrong, input the number again: ")
        sum_scores -= 10
    else:
        sum_scores += 10
    return sum_scores

print("   ~~Number Guessing Program~~   ")
print("The clue -> 5 + 5")
enter_num = int(input("Enter number you are guess: "))
print(f"\nScores {inputted_number(enter_num)}")
