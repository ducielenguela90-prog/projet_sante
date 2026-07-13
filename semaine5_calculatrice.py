# ============================================================
# AKIENI ACADEMY —
# Semaine 5 — Exercice d'application Calculatrice
# ============================================================


def addition(a, b):
    """
    Fonction permettant d'effectuer l'addition de deux nombres.
    Elle retourne la somme des deux valeurs.
    """
    return a + b


def soustraction(a, b):
    """
    Fonction permettant d'effectuer la soustraction de deux nombres.
    Elle retourne la différence entre les deux valeurs.
    """
    return a - b


def multiplication(a, b):
    """
    Fonction permettant d'effectuer la multiplication de deux nombres.
    Elle retourne le produit des deux valeurs.
    """
    return a * b


def division(a, b):
    """
    Fonction permettant d'effectuer la division de deux nombres.
    Elle vérifie que le deuxième nombre n'est pas égal à zéro.
    """
    if b == 0:
        return "Erreur : Division par zéro impossible."
    return a / b


def calculatrice():
    """
    Fonction principale de la calculatrice.
    Elle affiche le menu, récupère les choix de l'utilisateur
    et effectue les opérations demandées.
    """

    # Boucle permettant de refaire plusieurs calculs
    while True:

        print("\n===== CALCULATRICE =====")
        print("Addition (1)")
        print("Soustraction (2)")
        print("Multiplication (3)")
        print("Division (4)")
        print("Quitte (5)")

        operation = input("Choisissez une opération (1/2/3/4/5) : ")


        # Permettre à l'utilisateur de quitter
        if operation == "5":
            print("Merci d'avoir utilisé la calculatrice.")
            break


        # Vérification du choix de l'utilisateur
        if operation not in ["1", "2", "3", "4"]:
            print("Choix invalide. Veuillez réessayer.")
            continue


        try:
            # Conversion des valeurs saisies en nombres
            nombre1 = float(input("Entrez le premier nombre : "))
            nombre2 = float(input("Entrez le deuxième nombre : "))


            # Exécution de l'opération choisie
            if operation == "1":
                resultat = addition(nombre1, nombre2)
                type_operation = "addition"

            elif operation == "2":
                resultat = soustraction(nombre1, nombre2)
                type_operation = "soustraction"

            elif operation == "3":
                resultat = multiplication(nombre1, nombre2)
                type_operation = "multiplication"

            elif operation == "4":
                resultat = division(nombre1, nombre2)
                type_operation = "division"


            # Affichage du résultat
            print(f"Résultat de l'{type_operation} de {nombre1} et {nombre2} : {resultat}")


        # Gestion des erreurs de saisie
        except ValueError:
            print("Erreur : veuillez entrer uniquement des nombres.")


# Appel de la fonction calculatrice pour lancer le programme
calculatrice()

