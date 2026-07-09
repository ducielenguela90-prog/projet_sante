# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 2 : Triage Patient Urgences CHU Brazzaville
# Notions S2 : variables, types, input(), f-strings, conversion
# Notions S3 : if/elif/else, conditions composees or/and/not
# Notions S4 : boucles for, while, break, continue
# ============================================================

total_suspects = 0
total_confirmes = 0
total_deces = 0
total_actifs = 0
zones_vertes = 0
zones_jaunes = 0
zones_oranges = 0
zones_rouges = 0
nb_districts = 9

# Enregistrement du tableau global des donnees par district
Tableau_donnees = []

for i in range (nb_districts) :
    print(f"--- District {i+1} ---")

    # Saisie des donnees pour chaque district
    district = input("Nom du district : ")
    departement = input("Departement : ")
    suspects = int(input("Cas suspects : "))
    confirmes = int(input("Cas confirmes : "))
    deces = int(input("Deces : "))

    # Remplissage de chaque colonne dU tableau de donnees
    colonne_donnees = {
        "district": district,
        "departement": departement,
        "suspects": suspects,
        "confirmes": confirmes,
        "deces": deces
    }
    # Ajout de chaque colonne de donnees dans le tableau global
    Tableau_donnees.append(colonne_donnees)

    # Calcul des cas actifs et de la letalite
    cas_actifs = confirmes - deces
    if confirmes > 0:
        letalite = (deces / confirmes) * 100
    else:
        letalite = 0
    
    # Calcul des totaux nationaux
    total_confirmes += confirmes
    total_suspects += suspects
    total_actifs += cas_actifs
    total_deces += deces

    # Calcul des taux d'alerte par district
    if confirmes >= 10:
        alerte = "ROUGE"
        print("URGENCE — intervention immédiate")
        zones_rouges += 1
    elif confirmes >= 5 and confirmes <= 9:
        alerte = "ORANGE"
        print("ALERT — Envoyer une équipe d'intervention")
        zones_oranges += 1
    elif confirmes >= 2 and confirmes <= 4:
        alerte = "JAUNE"
        print("ALERT — Renforcer la surveillance")
        zones_jaunes += 1
    else:
        alerte = "VERT"
        print("Surveillance standard")
        zones_vertes += 1
    
    print(' Alerte :', alerte)
    print(' Actifs :', cas_actifs)
    print(' Letalite :', round(letalite, 1), '%')
    print()
    
    # # Affichage des donnees saisies pour chaque district
    # print(f"--- Donnees du district {district} ---")
    # for j in range(len(Tableau_donnees)):
    #     print(f"District : {Tableau_donnees[j]['district']}")
    #     print(f"Departement : {Tableau_donnees[j]['departement']}")
    #     print(f"Cas suspects : {Tableau_donnees[j]['suspects']}")
    #     print(f"Cas confirmes : {Tableau_donnees[j]['confirmes']}")
    #     print(f"Deces : {Tableau_donnees[j]['deces']}")
 
# Impression du rapport national

print('=======================================')
print(' RAPPORT NATIONAL MPOX 2025 ')
print('=======================================')
print('Districts analyses :', nb_districts)
print('Total suspects :', total_suspects)
print('Total confirmes :', total_confirmes)
print('Total deces :', total_deces)
print('Total cas actifs :', total_actifs)
print('Zones VERTES :', zones_vertes)
print('Zones JAUNES :', zones_jaunes)
print('Zones ORANGES :', zones_oranges)
