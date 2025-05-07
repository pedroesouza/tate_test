import csv
import os
import time

def name():
        try:
            name = os.getlogin()
        except Exception:
            # fallback for environments where os.getlogin() might not work (e.g. some IDEs)
            import getpass
            name = getpass.getuser()

        formatted_name = name.replace('.', ' ').split()
        if formatted_name:
            formatted_name[0] = formatted_name[0].capitalize()
            formatted_name = ' '.join(formatted_name)


# gets your own location
# get_location("8.8.8.8")  # gets Google's public DNS location

# Get the current logged-in user
name = os.getlogin()

formatted_name = name.replace('.', ' ').split()
formatted_name[0] = formatted_name[0].capitalize()

# Join the parts back together
formatted_name = ' '.join(formatted_name)

def question_teller():
    with open('questions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            id = row[0]
            score = 0
            total_score = 0
            print('Welcome to the survey.')
            time.sleep(3)
            if id == '9':
                print("\nLet's play a little game, shall we?")
            while True:
                question = input(f'\nQuestion {id}: {row[1]}: ').lower().strip()
                if id == '1':
                    if question == 'yes': #Add this at the end for the for loop.
                        print("\nYou can't play this game then. Bye.")
                        break
                    elif question == 'no':
                        print('\nOk good.')
                        break
                    else:
                        print('\nIncorrect option, try again. (type yes or no).')
                elif id == '2':
                    print('\nOk.')
                    break
                elif id == '3':
                    print("\nThat's cool.")
                    break
                elif id == '4':
                    if question == 'yes':
                        print('\nOk, just double checking.')
                        break
                    elif question == 'no':
                        print('\nAre you sure?...')
                        break
                    else:
                        print('\nIncorrect option, try again. (type yes or no).')
                elif id == '5':
                    print('\nActually based off my IP grabber, you are at 31.255.56.229')
                    break
                elif id == '6':
                    if question == 'yes':
                        print('\nOk cool, our team is ready to move in...')
                        break
                    elif question == 'no':
                        print('\nNot anymore...')
                        break
                    else:
                        print('\nIncorrect option, try again. (type yes or no).')
                elif id == '7':
                    try:
                        int(question)
                        print('\nThanks.')
                        break
                    except ValueError:
                        print('\nIncorrect option, try again. (type a number).')
                elif id == '8':
                    if question == 'yes':
                        print('\nGood boy.')
                        break
                    elif question == 'no':
                        print('\nBad boy...')
                        #jumpscare
                        break
                elif id == '9a':
                    if question == '19':
                        print('\nCorrect!')
                        score += 1
                        total_score += 1
                        break
                    else:
                        print('\nIncorrect...')
                        total_score += 1
                        break
                elif id == '9b':
                    if question == '2':
                        print('\nCorrect!')
                        score += 1
                        total_score += 1
                        break
                    else:
                        print('\nIncorrect...')
                        total_score += 1
                        break
                elif id == '9c':
                    if question == '110':
                        print('\nCorrect!')
                        score += 1
                        total_score += 1
                        break
                    else:
                        print('\nIncorrect...')
                        total_score += 1
                        break
                elif id == '9d':
                    if question == '63':
                        print('\nCorrect!')
                        score += 1
                        total_score += 1
                        break
                    else:
                        print('\nIncorrect...')
                        total_score += 1
                        break
                elif id == '9e':
                    if question == '5':
                        print('\nCorrect!')
                        score += 1
                        total_score += 1
                        break
                    else:
                        print('\nIncorrect...')
                        total_score += 1
                        break
                elif total_score == 5:
                    if score >= 3:
                        print('\nYou failed...')
                        # jumpscare
                        break
                    else:
                        print('\nYou passed.')
                        break
                elif id == '10':
                    if question == 'yes':
                        print('\nNuh uh.')
                        break
                    elif question == 'no':
                        print('\nGood.')
                        break
                    else:
                        print('\nIncorrect option, try again. (type yes or no).')
                elif id == '11':
                    if question == 'yes' or question == 'no':
                        print('\nOk.')
                        break
                    else:
                        print('\nIncorrect option, try again. (type yes or no).')
                elif id == '12':
                    if question == 'yes':
                        print('\nHow did you know?')
                        time.sleep(2)
                        #jumpscare
                        break
                    elif question == 'no':
                        print('\nThink again...')
                        #wait for user to turn around
                        time.sleep(2)
                        #jumpscare
                        break
                elif id == '13':
                    if question in str(range(1, 10)):
                        print('\nGive me a ten.')
                        #jumpscare
                    elif question == '10':
                        print('\nGood boy.')
                        break
                    else:
                        print('\nIncorrect input, try again. (Type a number 1-10).')

question_teller()