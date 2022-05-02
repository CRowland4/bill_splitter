import random


def get_party_count():
    """Returns the number of people in the party, and validates the input"""
    party_count = int(input('Enter the number of friends joining (including you):\n'))
    
    if party_count <= 0:
        print("\nNo one is joining for the party")
        return False
    else:
        return party_count


def create_party_dict(party_count):
    """Creates a dictionary where the keys are the party members, and the values are '0'"""
    members = []
    print('\nEnter the name of every friend (including you), each on a new line:')

    for _ in range(party_count):
        members.append(input())

    return dict.fromkeys(members, 0)


def get_final_bill():
    """Returns the final bill amount"""
    return float(input("\nEnter the total bill value:\n"))


def ask_lucky_game():
    if input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n') == 'Yes':
        return True
    else:
        return False
        
        
def get_lucky_one(dictionary):
    """Picks the person that doesn't have to pay for their food"""
    return random.choice(list(dictionary.keys()))
    
    
def regular_split(bill, dictionary):
    """Splits the bill without a lucky person"""
    split = round(bill / len(dictionary), 2)
    
    for name in dictionary.keys():
        dictionary[name] = split
        
    return dictionary
    
    
def lucky_split(bill, dictionary, lucky_one):
    """Splits the bill, taking into account the lucky person"""
    split = round(bill / (len(dictionary) - 1), 2)
    
    for name in dictionary.keys():
        if name != lucky_one:
            dictionary[name] = split
        else:
            continue
            
    return dictionary
    

def stage_4():
"""Returns the final split among the party members"""
    party_count = get_party_count()
    
    if party_count == False:
        return ''
    else:
        party_dict = create_party_dict(party_count)
        
    bill = get_final_bill()
    
    if ask_lucky_game():
        lucky_one = get_lucky_one(party_dict)
        print(f'{lucky_one} is the lucky one!')
        return lucky_split(bill, party_dict, lucky_one)
    else:
        print("No one is going to be lucky")
        return regular_split(bill, party_dict)
        
        
print(stage_4())
