# Import files.
from dictionaryfile import dictionaries 
from art import logo 
from art import vs 
import random
# CLS commands do not work with IDE used to write this program. Clear function used as substitute.
def clear():
    print(100 * "\n")
# Define temporary dictionary to compare instagram follower counts.
temp_dict = []
# Define other variables.
score = 0
game_continue = True
first_loop = True
# Define lose game function for when player chooses lower option.
def lose_game():
    global game_continue
    global score
    clear()
    print(logo)
    print("Instagram Followers Edition")
    print("\n")
    print(f"Sorry, that's wrong! Final score: {score}.")
    game_continue = False



while game_continue == True:
#     Dictionaries index spans a total of 50 famous instagram accounts. Game is won when all accounts have been used.
    if score == 49:
        clear()
        print(logo)
        print("Instagram Followers Edition")
        print("\n")
        print(f"You won the game! Your winning score is {score}.")
        exit()
    clear()
    print(logo)
    print("Instagram Followers Edition")
    print("\n")
# First loop condition used to pick two random accounts when starting the game.
    if first_loop == True:
        for i in range(2):
            x = random.choice(dictionaries)
            temp_dict.append(x)
            y = dictionaries.index(x)
            del dictionaries[y]
# Option A from previous round is removed. Option B becomes new option A and random account is picked to become new Option B.
    elif first_loop == False:
        temp_dict.pop(0)
        x = random.choice(dictionaries)
        temp_dict.append(x)
        y = dictionaries.index(x)
        del dictionaries[y]
#         Confirmation of correct answer from previous round and score display.
        print(f"You're right! Current score: {score}.")
#         Display information of two Instagram account holders.
    print(f"Compare A: {temp_dict[0]['name']}, {temp_dict[0]['description']}, from {temp_dict[0]['country']}.")
    print(vs)
    print(f"Against B: {temp_dict[1]['name']}, {temp_dict[1]['description']}, from {temp_dict[1]['country']}.")
    print("\n")
#     Nested while loop to grab correct input and check if guess is correct or incorrect.
    while True:
        try:
            guess = str(input("Who has more followers? Type 'a' or 'b': ")).lower()
        except:
            print("Invalid input. Give me your guess by typing 'a' or 'b'.")
            continue
        if guess == 'a':
            if (temp_dict[0]['follower_count']) > (temp_dict[1]['follower_count']):
                score += 1
                first_loop = False
                break
            elif (temp_dict[0]['follower_count']) < (temp_dict[1]['follower_count']):
                lose_game()
                break
        elif guess == 'b':
            if (temp_dict[0]['follower_count']) > (temp_dict[1]['follower_count']):
                lose_game()
                break
            elif (temp_dict[0]['follower_count']) < (temp_dict[1]['follower_count']):
                score += 1
                first_loop = False
                break
        else:
            print("Invalid input. Give me your guess by typing 'a' or 'b'.")
            continue
