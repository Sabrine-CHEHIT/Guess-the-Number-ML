import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Bienvenue dans le jeu 'Devine le Nombre' !")
    print("L'ordinateur a choisi un nombre entre 1 et 100. Essayez de le deviner.")

    while True:
        try:
            user_guess = int(input("Votre proposition : "))
            attempts += 1

            if user_guess < secret_number:
                print("Trop bas ! Essayez encore.")
            elif user_guess > secret_number:
                print("Trop haut ! Essayez encore.")
            else:
                print(f"Bravo ! Vous avez trouvé le nombre en {attempts} essais.")
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    guess_the_number()
