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
            if id == '9':
                print("Let's play a little game, shall we?")
            while True:
                question = input(f'Question {id}: {row[1]}: ').lower().strip()
                if id == '1':
                    if question == 'yes': #Add this at the end for the for loop.
                        print("You can't play this game then. Bye.")
                        break
                    elif question == 'no':
                        print('Ok good.')
                        break
                    else:
                        print('Incorrect option, try again. (type yes or no).')
                elif id == '2':
                    print('Ok.')
                    break
                elif id == '3':
                    print("That's cool.")
                    break
                elif id == '4':
                    if question == 'yes':
                        print('Ok, just double checking.')
                        break
                    elif question == 'no':
                        print('Are you sure?...')
                        break
                    else:
                        print('Incorrect option, try again. (type yes or no).')
                elif id == '5':
                    print('Actually based off my IP grabber, you are at 31.255.56.229')
                    break
                elif id == '6':
                    if question == 'yes':
                        print('Ok cool, our team is ready to move in...')
                        break
                    elif question == 'no':
                        print('Not anymore...')
                        break
                    else:
                        print('Incorrect option, try again. (type yes or no).')
                elif id == '7':
                    try:
                        int(question)
                        print('Thanks.')
                        break
                    except ValueError:
                        print('Incorrect option, try again. (type a number).')
                elif id == '8':
                    if question == 'yes':
                        print('Good boy.')
                        break
                    elif question == 'no':
                        print('Bad boy...')
                        #jumpscare
                        break
                elif id == '9a':
                    if question == '19':
                        print('Correct!')
                        score += 1
                        total_score += 1
                        break
                    else:
                        print('Incorrect...')
                        total_score += 1
                        break
                elif id == '9b':
                    if question == '2':
                        print('Correct!')
                        score += 1
                        total_score += 1
                        break
                    else:
                        print('Incorrect...')
                        total_score += 1
                        break
                elif id == '9c':
                    if question == '110':
                        print('Correct!')
                        score += 1
                        total_score += 1
                        break
                    else:
                        print('Incorrect...')
                        total_score += 1
                        break
                elif id == '9d':
                    if question == '63':
                        print('Correct!')
                        score += 1
                        total_score += 1
                        break
                    else:
                        print('Incorrect...')
                        total_score += 1
                        break
                elif id == '9e':
                    if question == '5':
                        print('Correct!')
                        score += 1
                        total_score += 1
                        break
                    else:
                        print('Incorrect...')
                        total_score += 1
                        break
                elif total_score == 5:
                    if score >= 3:
                        # jumpscare
                        pass
                        break
                    else:
                        print('You passed.')
                        break
                elif id == '10':
                    if question == 'yes':
                        print('Nuh uh.')
                        break
                    elif question == 'no':
                        print('Good.')
                        break
                    else:
                        print('Incorrect option, try again. (type yes or no).')
                elif id == '11':
                    if question == 'yes' or question == 'no':
                        print('Ok.')
                        break
                    else:
                        print('Incorrect option, try again. (type yes or no).')
                elif id == '12':
                    if question == 'yes':
                        print('How did you know?')
                        time.sleep(2)
                        #jumpscare
                        break
                    elif question == 'no':
                        print('Think again...')
                        #wait for user to turn around
                        time.sleep(2)
                        #jumpscare
                        break
                elif id == '13':
                    if question in str(range(1, 10)):
                        print('Give me a ten.')
                        #jumpscare
                    elif question == '10':
                        print('Good boy.')
                        break
                    else:
                        print('Incorrect input, try again. (Type a number 1-10).')

question_teller()