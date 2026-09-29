from engine.basic_calc import BasicCalculator


def afficher_menu():
    print("\n=== CalculatedX ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Historique")
    print("0. Quitter")


def main():
    calculatrice = BasicCalculator()

    choix_operations = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
    }

    while True:
        afficher_menu()

        choix = input("\nChoisissez une option : ")

        if choix == "0":
            print("Au revoir !")
            break

        if choix == "5":
            print("\n=== Historique ===")

            calculs = calculatrice.historique.calculs

            if not calculs:
                print("Aucun calcul enregistré.")
            else:
                for calcul in calculs:
                    print(
                        calcul["operandes"][0],
                        calcul["operation"],
                        calcul["operandes"][1],
                        "=",
                        calcul["resultat"],
                    )

            continue

        if choix not in choix_operations:
            print("Choix invalide.")
            continue

        try:
            a = float(input("Premier nombre : "))
            b = float(input("Deuxième nombre : "))

            symbole = choix_operations[choix]

            resultat = calculatrice.calculer(
                symbole,
                a,
                b,
            )

            print(f"Résultat : {resultat}")

        except ValueError as erreur:
            print(f"Erreur : {erreur}")


if __name__ == "__main__":
    main()