import requests

# To get input
def get_user_input(prompt_message, valid_options):
    while True:
        user_input = input(prompt_message)
        if user_input.lower() in valid_options:
            return user_input.lower()
        else:
            print("Invalid input. Please try again.")

def prompt():
    preference = [] # Array to take inputs

    transaction = get_user_input('Are cryptocurrency transactions required? (y/n) \n', ['y', 'n'])
    preference.append(1 if transaction == 'y' else 2)

    if transaction == 'y':
        privacy = get_user_input('Is privacy needed? (y/n) \n', ['y', 'n'])
        preference.append(3 if privacy == 'y' else 4)

        if privacy == 'n':
            large = get_user_input('Are there large payments? (y/n) \n', ['y', 'n'])
            preference.append(5 if large == 'y' else 6)

            if large == 'n':
                evsm = get_user_input('Efficiency and low costs versus maturity? \nefficiency = 1 \nmaturity = 2 \n', ['1', '2'])
                preference.append(7 if evsm == '1' else 8)

    else:
        contract = get_user_input('Is guaranteed execution of contract conditions required? (y/n) \n', ['y', 'n'])
        preference.append(9 if contract == 'y' else 10)

        if contract == 'y':
            privacy = get_user_input('Is privacy needed? (y/n) \n', ['y', 'n'])
            preference.append(3 if privacy == 'y' else 4)

            if privacy == 'n':
                evsm = get_user_input('Efficiency and low costs versus maturity? \nefficiency = 1 \nmaturity = 2 \n', ['1', '2'])
                preference.append(7 if evsm == '1' else 8)

        else:
            governance = get_user_input('Governance type? \ndecentralized = 1 \nconsortium = 2 \ncenteralized = 3 \n', ['1', '2', '3'])

            if governance == '1':
                preference.append(11)

                privacy = get_user_input('Is privacy needed? (y/n) \n', ['y', 'n'])
                preference.append(3 if privacy == 'y' else 4)

                if privacy == 'n':
                    evsm = get_user_input('Efficiency and low costs versus maturity? \nefficiency = 1 \nmaturity = 2 \n', ['1', '2'])
                    preference.append(7 if evsm == '1' else 8)

            elif governance == '2':
                preference.append(12)

                evsm = get_user_input('Efficiency and low costs versus maturity? \nefficiency = 1 \nmaturity = 2 \n', ['1', '2'])
                preference.append(7 if evsm == '1' else 8)

            else:
                preference.append(13)

                evsm = get_user_input('Efficiency and low costs versus maturity? \nefficiency = 1 \nmaturity = 2 \n', ['1', '2'])
                preference.append(7 if evsm == '1' else 8)

    return preference

# Takes the preference array as input and converts it into a dictionary format
def create_preference_dict(preference):
    preference_dict = {}
    for i, value in enumerate(preference):
        preference_dict[f"p{i+1}"] = value
    return preference_dict

# Takes the dictionary as input, sends a GET request to the specified URL with the dictionary as parameters, and retrieves the response
def send_preference(preference_dict):
    response = requests.get("http://localhost:8080", params=preference_dict)
    print(response.json())

# Execution
preference = prompt()
preference_dict = create_preference_dict(preference)
print("User preference:", preference_dict)
send_preference(preference_dict)