def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible.")

    return a / b


def afficher_menu():
    print("\n=== CalculatedX ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")


def main():
    operations = {
        "1": addition,
        "2": soustraction,
        "3": multiplication,
        "4": division,
    }

    while True:
        afficher_menu()

        choix = input("Choisissez une opération : ")

        if choix == "5":
            print("À bientôt !")
            break

        if choix not in operations:
            print("Opération invalide.")
            continue

        try:
            a = float(input("Premier nombre : "))
            b = float(input("Deuxième nombre : "))

            resultat = operations[choix](a, b)

            print(f"Résultat : {resultat}")

        except ValueError as erreur:
            print(f"Erreur : {erreur}")


if __name__ == "__main__":
    main()