import random
from colorama import Fore, Style

def generate_exercise():
    a0 = random.randint(1, 999)
    r = random.randint(1, 20)
    n_values = random.sample(range(1, 20), random.randint(1, 5))
    n_values.sort()

    terms = {}
    for n in n_values:
        terms[n] = a0 + (n - 1) * r

    exercise = f"r = {Fore.RED}{r}{Style.RESET_ALL}  U{Fore.BLUE}0{Style.RESET_ALL} = {Fore.RED}{a0}{Style.RESET_ALL}"
    exercise += "\ncalcule tout sa stp  :"
    for n, term in terms.items():
        exercise += f"\nU{Fore.BLUE}{n}{Style.RESET_ALL}."

    return exercise, terms

def is_close(value, target, tolerance=1):
    """
    vérifie si une valeur est proche d'une cible dans une certaine tolérance
    """
    return abs(value - target) <= tolerance

def main():
    exit_command = "exit"
    while True:
        try:
            exercise, terms = generate_exercise()
            print("\n" + exercise)
            user_input = input("\nexit pour exit:")
            if user_input.lower() == exit_command:
                print("byebye.")
                break

            for n, term in terms.items():
                user_input = input(f"submit stp {Fore.BLUE}{n}{Style.RESET_ALL} : ")
                if user_input.lower() == exit_command:
                    print("byebye.")
                    return

                try:
                    user_answer = int(user_input)
                    if is_close(user_answer, term):
                        print(Fore.GREEN + "lol ok cheater gg" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + f" TA EU FAUX CETAIT {term}" + Style.RESET_ALL)
                except ValueError:
                    print(Fore.YELLOW + "tu fait quoi ptdr" + Style.RESET_ALL)
        except ValueError:
            print(Fore.YELLOW + "bug retry stp" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
