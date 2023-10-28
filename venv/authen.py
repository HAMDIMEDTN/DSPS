import re
import hashlib
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

        sha256 = hashlib.sha256()
        sha256.update(password.encode())
        hash_result = sha256.hexdigest()

        file.write(f"Email: {email}, Password: {hash_result}\n")


def authentification():
    while True:
        email = input("Entrez votre email : ")
        password = input("Entrez votre mot de passe : ")
        sha256 = hashlib.sha256()
        sha256.update(password.encode())
        hash_result = sha256.hexdigest()
        with open('users.txt', 'r') as file:
            for line in file:
                if f"Email: {email}, Password: {hash_result}" in line:
                    print("Authentification réussie!")
                    menu()



        print("Email ou mot de passe incorrect. Réessayez.")


def menu():
    while True :
        mot = input("donner un mot a hache ")
        print("1- Taper 1 pour Hachez le mot par sha256")
        print("2- Taper 2 pour Hachez le mot en génerant unsalt (bcrypt) ")
        print("3- Taper 3 pour Attaquer par Dictionnaire le Mot inséré ")
        choix = input("donner votre choix ")
        match choix :
            case "1":

                sha256 = hashlib.sha256()
                sha256.update(mot.encode())
                hash_result = sha256.hexdigest()
                print(f"Le hachage SHA-256 du mot '{mot}' est : {hash_result}")
                quit()


            case "2":
                import bcrypt

                salt = bcrypt.gensalt()

                mot_de_passe_hache = bcrypt.hashpw(mot.encode(), salt)

                print(f"Le mot de passe haché avec le salt est : {mot_de_passe_hache.decode()}")

                quit()
            case "3":
                from datetime import datetime
                dic = open('dic.txt', mode='r')

                F = False
                n = 0
                t = datetime.now()
                for pwd in dic:
                    pwd = pwd.strip()
                    n += 1
                    if mot == pwd:
                        print("mot de passe trouver :  ", pwd, "pensez a le changer ")
                        print(n, "mots testes en ", (datetime.now() - t).total_seconds(), "secondes")
                        dic.close()
                        F = True
                        break
                print()
                if not F:
                    print("mot de passe non trouve , aucun hache ne correspond a votre hache ", mot)
                    dic.close()



                quit()
            case _ :
                print ("merci de inser 1 , 2 ou 3 ")

