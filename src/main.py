import random

def friends_dict():
    friends_list, friends_count = get_friends_list()
    if not friends_list:
        return
    amount_to_pay = get_bill_amount()
    per_person = split_bill(amount_to_pay, friends_count)

    lucky = lucky_friend(friends_list)
    per_person = split_bill(amount_to_pay, friends_count - 1)
    names_dict = create_friends_dict(friends_list, per_person)
    names_dict = lucky_bonus(names_dict, lucky)
    print(names_dict)

def lucky_friend(friends_list):
    choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:').lower()
    if choice == "yes":
        lucky = random.choice(friends_list)
        print(f"{lucky} is the lucky one!")
        return lucky
    else:
        print("No one is going to be lucky")
        return None

def get_friends_list():
    friends_numbers = int(input("Enter the number of friends joining (including you):"))
    if friends_numbers < 1:
        print("No one is joining for the party")
        return [],0
    else:
        friends_list = []
        print("Enter the name of every friend (including you), each on a new line:")

        for n in range(1,friends_numbers + 1):
            name = input()
            friends_list.append(name)

    return friends_list, friends_numbers

def get_bill_amount():
    return int(input("Enter the total bill value:"))

def split_bill(amount, friends_count):
    per_person = round(amount / friends_count, 2)
    return int(per_person) if per_person.is_integer() else per_person

def create_friends_dict(friends_list, per_person):
    return {name : per_person for name in friends_list}

def lucky_bonus(friends_list, lucky_person):
    if lucky_person:
        friends_list[lucky_person] = 0
    return friends_list

if __name__ == '__main__':
    friends_dict()