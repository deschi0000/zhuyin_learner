import json
import os, sys
from scorekeeper import ScoreKeeper
from zhuyin_type import ZhuyinType
import random


game_score = ScoreKeeper()

# Load to keep the cmd line nice and neat
clear = lambda: os.system('cls')


def get_number():
    '''Makes sure that a valid number between 1-4 is inputted'''
    
    while True:
        try: 
            answer = input("Enter your choice [1-4]: ")

            # Give option to quit
            if answer == "q":
                print("Quitting")
                sys.exit()
           

            number = int(answer)

            if 1 <= number <= 4:
                return number
            else:
                print("Please enter a value of 1-4")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def run_questions(question_dict):

    ''' Runs the questions in the command 
    line loaded from the json file'''

    # Extract the different parts
    question = question_dict["question"]
    # print(question_dict["question"])

    options = question_dict["options"]
    # print(question_dict["options"])

    clear()

    # Keep updating the score for each question   
    print(game_score)

    # Ask the question
    print(f"Correct Zhuyin for: {question} ?")
    for i in range(0, len(options)):
        print(f"{i+1}: {options[i]}")
    chosen_number = get_number()


    # Get the answer
    answer = question_dict["answer"]
    # print(question_dict["answer"])

    if chosen_number is answer:
        print("Correct!\n")
        game_score.add_to_correct()
    else:
        print("Incorrect\n")

    # print(game_score)
    clear()

    # print(f"{question} ?")
    # print(f"{options} ?")
    

def load_zhuyin_json_list(zhuyin_type):

    '''Returns a list of the argument type (from enum)'''

    consonant_list = []
    vowel_list = []
    all_list = []
    file_path = os.path.join(os.getcwd(), 'zhuyin.json')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Get the consonants
            consonant_list = data["consonants"]
    
            # Get the vowels
            vowel_list = data["vowels"]

            #Get everything
            all_list = consonant_list + vowel_list

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Please check the JSON format.")

    if zhuyin_type is ZhuyinType.CONSONANT:
        return consonant_list
    elif zhuyin_type is ZhuyinType.VOWEL:
        return vowel_list
    elif zhuyin_type :
        return all_list
    else:
        return all_list


def load_intro():
    print("Welcome to Zhuyin Practicer ㄓˋ ㄧㄣ ㄌㄧㄢˋ ㄒㄧˊ")
    print("What would you like to Practice?")
    
    while True:
        try:
            choice = input("[v]owels, [c]onsonants, [a]ll or [q]uit: ")
            if choice not in ("v","c","e","q"):
                print("Please choose one of the options")
            else:
                choice.lower()
                if choice is "v":
                    return ZhuyinType.VOWEL
                elif choice is "c":
                    return ZhuyinType.CONSONANT
                elif choice is "a":
                    return ZhuyinType.ALL
                elif choice is "q":
                    print("Quitting")
                    sys.exit()

        except ValueError:
            print("Invalid input. Please enter a valid choice.")

def main():

    # Clear the screen for tidiness
    clear()

    practice_choice = load_intro()

    # Load the json list that you want with the type
    list_to_practice = load_zhuyin_json_list(practice_choice)
    
    # Add the list here, or abstract it away later
    game_score.add_to_total(len(list_to_practice))

    # Lets shuffle the list to keep it fun
    random.shuffle(list_to_practice)

    for i in list_to_practice:
        # print(i)
        run_questions(i)

    # Print the results:
    final_percentage = game_score.correct / game_score.total * 100
    print(f"\nFinal Outcome: {final_percentage:.1f}%")


if __name__ == '__main__':
    main()
