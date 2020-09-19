def square(number):
    return number*number


def times2(number):
    return number*2

def checking_letter():
    names = []
    for _ in range(5):
        name = input("Please enter the name of someone you know. ")
        names.append(name)

    lowercased = [name.lower() for name in names]

    titlecased = [name.title() for name in lowercased]

    invitations = [
        f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]

    for invitation in invitations:
        print(invitation)
