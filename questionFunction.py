import requests
import csv
import os

def address():
    # Use your own IP by leaving out the IP part of the URL
    response = requests.get('https://ipinfo.io/json')
    
    if response.status_code == 200:
        data = response.json()
        IP = data.get('ip')
        City = data.get('city')
        Region = data.get('region')
        Country = data.get('country')
        LatLong = data.get('loc')
        WiFi = data.get('org')
        area_code = data.get('postal')
        time_zone = data.get('timezone')

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

        print(f'Well {formatted_name}, it says here that you are in {City}, {Region}, {Country}. Your current IP address is {IP} and your latitude and longitude is {LatLong}. Your WiFi network is {WiFi} and your postal/area code is {area_code}. You are also in the {time_zone} time zone.')
    else:
        print("Failed to retrieve location")

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
                address()
                continue
            if row[4] == 'text entry':
                print(row[5])
            else:
                if question == row[4]:
                    print(row[5])
                else:
                    print('Incorrect.')

question_teller()