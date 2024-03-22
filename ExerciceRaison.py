import random
from colorama import Fore, Style

def generate_exercise():
    Ux = random.randint(1, 10)  # numéro du terme connu
    y = random.randint(1, 999)  # valeur du terme connu
    n = random.randint(Ux + 1, Ux + 10)  # numéro du terme correspondant à Un
    Un = y + (n - Ux) * random.randint(1, 20)  # valeur du terme correspondant à n
    r = (Un - y) / (n - Ux)  # formule de calcul

    #
    exercise = f"U{Fore.BLUE}{Ux}{Style.RESET_ALL} = {Fore.RED}{y}{Style.RESET_ALL}  U{Fore.BLUE}{n}{Style.RESET_ALL} = {Fore.RED}{Un}{Style.RESET_ALL}\n trouve r mdr"

    return exercise, r

def main():
    exit_command = "exit"
    while True:
        try:
            exercise, correct_answer = generate_exercise()
            print("\n" + exercise)
            user_input = input("\nsalut appuyer sur enter pour continuer et exit pour partir")
            if user_input.lower() == exit_command:
                print("byebye.")
                break

            user_answer = input("input : ")
            if user_answer.lower() == exit_command:
                print("byebye.")
                return

            try:
                user_answer = float(user_answer)
                if abs(user_answer - correct_answer) < 0.01:  # utilise une tolerancee pour la comparsison
                    print(Fore.GREEN + "oui c'est sa" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"non, c'est {correct_answer}." + Style.RESET_ALL)
            except ValueError:
                print(Fore.YELLOW + "tfk mdr" + Style.RESET_ALL)
        except ValueError:
            print(Fore.YELLOW + "erreur réessayer." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
