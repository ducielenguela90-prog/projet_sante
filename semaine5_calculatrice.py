# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 2 : Triage Patient Urgences CHU Brazzaville
# Notions S2 : variables, types, input(), f-strings, conversion
# Notions S3 : if/elif/else, conditions composees or/and/not
# Notions S4 : boucles for, while, break, continue
# Notions S5 : Exercice d'application Calculatrice
# ============================================================

def calculatrice():
    print("Bienvenue dans la calculatrice !")
    print("Choisissez une opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    choix = input("Entrez le numéro de l'opération (1/2/3/4) : ")

    if choix in ['1', '2', '3', '4']:
        num1 = float(input("Entrez le premier nombre : "))
        num2 = float(input("Entrez le deuxième nombre : "))

        if choix == '1':
            resultat = num1 + num2
            operation = "addition"
        elif choix == '2':
            resultat = num1 - num2
            operation = "soustraction"
        elif choix == '3':
            resultat = num1 * num2
            operation = "multiplication"
        elif choix == '4':
            if num2 != 0:
                resultat = num1 / num2
                operation = "division"
            else:
                print("Erreur : Division par zéro.")
                return
        print(f"Le résultat de l'{operation} de {num1} et {num2} est : {resultat}")
    else:
        print("Choix invalide. Veuillez réessayer.")

calculatrice()
