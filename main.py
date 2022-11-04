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
    if first_loop == True:
        for i in range(2):
            x = random.choice(dictionaries)
            temp_dict.append(x)
            y = dictionaries.index(x)
            del dictionaries[y]
    elif first_loop == False:
        temp_dict.pop(0)
        x = random.choice(dictionaries)
        temp_dict.append(x)
        y = dictionaries.index(x)
        del dictionaries[y]
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {temp_dict[0]['name']}, {temp_dict[0]['description']}, from {temp_dict[0]['country']}.")
    print(vs)
    print(f"Against B: {temp_dict[1]['name']}, {temp_dict[1]['description']}, from {temp_dict[1]['country']}.")
    print("\n")
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
        
    