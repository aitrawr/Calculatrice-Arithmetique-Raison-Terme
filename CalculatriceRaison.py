from colorama import Fore, Style

def raison_suite_arithmetique(Ux, y, Un, n):
    """
    Calcule la raison de la suite arithmétique à partir des valeurs données.
    :param Ux: Valeur du terme connu.
    :param y: Valeur du terme correspondant à Ux.
    :param Un: Valeur du terme Un correspondant à n.
    :param n: Numéro du terme correspondant à Un.
    :return: Raison de la suite arithmétique.
    """
    r = (Un - y) / (n - Ux)
    return r

def main():
    exit_command = 'exit'
    while True:
        try:
            print()
            user_input = input("enter pour continuer et exit pour partir. ")
            if user_input.lower() == exit_command:
                print("Fin du programme.")
                break

            Ux = int(input("rentre le numéro du terme  : "))
            y = int(input("ok la valeur de ce terme stp : "))
            Un = int(input("mtn la VALEUR du terme qui correspond à n : "))
            n = int(input(" numéro du terme qui correspond à Un : "))

            r = raison_suite_arithmetique(Ux, y, Un, n)
            print("\nvoilà le resultat")
            print(f"numero du terme connu : {Fore.BLUE}{Ux}{Style.RESET_ALL}")
            print(f"valeur du terme connu : {Fore.BLUE}{y}{Style.RESET_ALL}")
            print(f"valeur  n : {Fore.GREEN}{Un}{Style.RESET_ALL}")
            print(f"numero Un : {Fore.YELLOW}{n}{Style.RESET_ALL}")
            print(f"La raison est : {Fore.RED}{r}{Style.RESET_ALL}")
            
        except ValueError:
            print("Veuillez entrer des valeurs valides.")

if __name__ == "__main__":
    main()
