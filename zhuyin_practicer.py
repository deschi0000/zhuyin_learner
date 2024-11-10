import json
import os
from scorekeeper import ScoreKeeper


game_score = ScoreKeeper()

def get_number():
    while True:
        try: 
            number = int(input("Enter your choice [1-4]: "))
            if 1 <= number <= 4:
                return number
            else:
                print("Please enter a value of 1-4")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def run_questions(question_dict):

    
    
    # Extract the different parts
    question = question_dict["question"]
    # print(question_dict["question"])

    options = question_dict["options"]
    # print(question_dict["options"])


    # Ask the question
    print(f"Correct Zhuyin for: {question} ?")
    for i in range(0, len(options)):
        print(f"{i+1}: {options[i]}")
    chosen_number = get_number()


    # Get the answer
    answer = question_dict["answer"]
    # print(question_dict["answer"])

    if chosen_number == answer:
        print("Correct!\n")
        game_score.add_to_correct()
    else:
        print("Incorrect\n")

    print(game_score)

    # print(f"{question} ?")
    # print(f"{options} ?")
    



def main():

    consonant_list = []
    vowel_list = []
    
    file_path = os.path.join(os.getcwd(), 'zhuyin.json')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Get the consonants
            consonant_list = data["consonants"]
    
            # Get the vowels
            vowel_list = data["vowels"]

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Please check the JSON format.")

    # If doing the score here:
    # total_questions_amount = len(consonant_list) + len(vowel_list)
    # game_score = ScoreKeeper(total_questions_amount)
    
    # Add the list here, or abstract it away later
    game_score.add_to_total(len(consonant_list))

    for i in consonant_list:
        # print(i)
        run_questions(i)

    # Print the results:
    final_percentage = game_score.correct / game_score.total * 100
    print(f"\nFinal Outcome: {final_percentage:.1f}%")


    return

if __name__ == '__main__':
    main()
