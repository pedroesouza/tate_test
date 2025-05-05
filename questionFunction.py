import requests
import csv
import os

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
            question = input(f'{row[3]}: ')
            if row[0] == '5':
                name()
                continue
            if row[4] == 'text entry':
                print(row[5])
            else:
                if question == row[4]:
                    print(row[5])
                else:
                    print('Incorrect.')

question_teller()