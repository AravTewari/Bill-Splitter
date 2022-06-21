import random


def add_friends():
    print("Enter the number of friends joining (including you):")
    num_friends = int(input())

    if num_friends <= 0:
        print("No one is joining for the party")
    else:
        print("Enter the name of every friend (including you), each on a new line")

        friends_dict = {}
        for i in range(num_friends):
            friend_name = input()
            friends_dict[friend_name] = 0

        print("Enter the total bill value:")
        total_bill = int(input())
        split_bill_dict = split_bill(friends_dict, total_bill)

        lucky_person = make_lucky(split_bill_dict)

        if lucky_person is not None:
            split_bill_dict.pop(lucky_person)
            split_bill_dict = split_bill(split_bill_dict, total_bill)
            split_bill_dict[lucky_person] = 0

        print(split_bill_dict)


def split_bill(friends_dict, total_bill):
    bill_per_person = round(total_bill / len(friends_dict), 2)
    return friends_dict.fromkeys(friends_dict, bill_per_person)


def make_lucky(split_bill_dict):
    print('Do you want to use the "Who is lucky?" feature?')
    answer = input()
    if answer == "Yes":
        lucky_person = random.choice(list(split_bill_dict.keys()))
        print(f"{lucky_person} is the lucky one!")
        return lucky_person
    else:
        print("No one is going to be lucky")
        return None


add_friends()
