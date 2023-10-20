from authen import *
def menu():
    while True :
        print("1- Taper 1 pour l enregistrement ")
        print("2- Taper 2 pour l authentification ")
        print("3- Taper 3 pour quiter ")
        choix= input("donner votre choix ")
        match choix :
            case "1":
                enregistrement()
                break
            case "2":
                authentification()

            case "3":
                quit(2)
            case _ :
                print ("merci de inser 1 , 2 ou 3 ")


menu()