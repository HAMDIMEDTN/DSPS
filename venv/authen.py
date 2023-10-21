import re
#from getpass import getpass
#getpass ne fonctionne pas sur pycharm pour utlise un mot de pass chifree
def check(email):
    regex = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

def check_password(password):
    # Use a regular expression to validate the password
    return bool(re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password))

def enregistrement():
    while True:
        email = input("Inserer votre email: ")
        if check(email):
            print("Email Valid ")
            break
        else:
            print("Introduire un email valide")

    while True:
        password = input("Donner votre password: ")
        if check_password(password):
            print("Password valid")
            break
        else:
            print("Le password doit contenir 1 lettre majuscule, 1 lettre minuscule, 1 chiffre, 1 caractère spécial et être de longueur 8.")

    with open('users.txt', 'a') as file:
        file.write(f"Email: {email}, Password: {password}\n")


def authentification():
    while True:
        email = input("Entrez votre email : ")
        password = input("Entrez votre mot de passe : ")

        with open('users.txt', 'r') as file:
            for line in file:
                if f"Email: {email}, Password: {password}" in line:
                    print("Authentification réussie!")
                    menu()



        print("Email ou mot de passe incorrect. Réessayez.")


def menu():
    while True :
        print("1- Taper 1 pour Hachez le mot par sha256")
        print("2- Taper 2 pour Hachez le mot en génerant unsalt (bcrypt) ")
        print("3- Taper 3 pour Attaquer par Dictionnaire le Mot inséré ")
        mot= input("donner un mot a hache ")
        match mot :
            case "1":
                print("Hachez le mot par sha256")
                quit()
            case "2":
                print("Hachez le mot en génerant unsalt (bcrypt)")
                quit()
            case "3":
                print("Attaquer par Dictionnaire le Mot inséré ")
                quit()
            case _ :
                print ("merci de inser 1 , 2 ou 3 ")


