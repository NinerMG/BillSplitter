def friends_dict():
    friends_numbers = int(input("Enter the number of friends joining (including you):"))
    if friends_numbers < 1:
        print("No one is joining for the party")
    else:
        friends_list = []
        print("Enter the name of every friend (including you), each on a new line:")

        for n in range(1,friends_numbers + 1):
            name = input()
            friends_list.append(name)

        names_dict = {n : 0 for n in friends_list}
        print(names_dict)

if __name__ == '__main__':
    friends_dict()