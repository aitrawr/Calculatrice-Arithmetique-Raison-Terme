from colorama import Fore, Style

def terme_suite_arithmetique(Ux, y, r, n):
    """
    calcule le terme Un de la suite arithmétique reçu par Un = U0 + r*(n-1)
    :param Ux: valeur du terme donné
    :param y: valeur du terme donné
    :param r: raison de la suite
    :param n: terme de la suite à calculer
    :return: valeur du terme Un
    """
    U0 = y - r * (Ux - 1) 
    Un = U0 + r * (n - 1)
    return Un

def main():
    exit_command = 'exit'
    while True:
        try:
            print()
            user_input = input("exit pour exit : ")
            if user_input.lower() == exit_command:
                print("Fin du programme.")
                break

            Ux = int(input("c'est quoi le terme? : "))
            y = int(input("ok cool est il est égal à cmb? : "))
            r = int(input("la raison stp : "))
            n = int(input("numéro du terme à calculer : "))

            Un = terme_suite_arithmetique(Ux, y, r, n)
            print("\nRésultat du calcul :")
            print(f"la valeur du terme donné est : {Fore.BLUE}{Ux}{Style.RESET_ALL}")
            print(f"le terme est egale à : {Fore.BLUE}{y}{Style.RESET_ALL}")
            print(f"la raison  : {Fore.GREEN}{r}{Style.RESET_ALL}")
            print(f"le numéro du terme à calculer : {Fore.YELLOW}{n}{Style.RESET_ALL}")
            print(f"le resultat est : {Fore.RED}{Un}{Style.RESET_ALL}")
            
        except ValueError:
            print("bah mdr.")

if __name__ == "__main__":
    main()
