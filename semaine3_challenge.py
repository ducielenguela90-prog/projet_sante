from sante_variable import *

print("="*60)
print("TABLEAU DE BORD SANITAIRE - MINISTERE DE LA SANTE")
print("Date : 16 janvier 2026 | Pour le Conseil des Ministres")
print("="*60)

# Calcul des taux d'occupation pour chaque hôpital
h1_taux_occupation = round(h1_nb_lits_occupes / h1_nb_lits * 100, 2)
h2_taux_occupation = round(h2_nb_lits_occupes / h2_nb_lits * 100, 2)
h3_taux_occupation = round(h3_nb_lits_occupes / h3_nb_lits * 100, 2)
h4_taux_occupation = round(h4_nb_lits_occupes / h4_nb_lits * 100, 2)
h5_taux_occupation = round(h5_nb_lits_occupes / h5_nb_lits * 100, 2)


# Calcul du nombre d'hôpitaux en situation critique
hopital_critique = 0

# Médicament en rupture de stock
h1_nb_ruptures = 2
h2_nb_ruptures = 0
h3_nb_ruptures = 1
h4_nb_ruptures = 3
h5_nb_ruptures = 2

# Nombre de médicaments en alerte
h1_nb_alerte = 2
h2_nb_alerte = 1
h3_nb_alerte = 2
h4_nb_alerte = 0
h5_nb_alerte = 1

# Calcul du niveau de triage des occupations
# Pour h1
if h1_taux_occupation > 95:
    h1_niveau_occupation = "[CRI]"
elif h1_taux_occupation > 85:
    h1_niveau_occupation = "[ALT]"
else :
    h1_niveau_occupation = "[OK]"

# Pour h2
if h2_taux_occupation > 95:
    h2_niveau_occupation = "[CRI]"
elif h2_taux_occupation > 85:
    h2_niveau_occupation = "[ALT]"
else :
    h2_niveau_occupation = "[OK]"

# Pour h3
if h3_taux_occupation > 95:
    h3_niveau_occupation = "[CRI]"
elif h3_taux_occupation > 85:
    h3_niveau_occupation = "[ALT]"
else :
    h3_niveau_occupation = "[OK]"

# Pour h4
if h4_taux_occupation > 95:
    h4_niveau_occupation = "[CRI]"
elif h4_taux_occupation > 85:
    h4_niveau_occupation = "[ALT]"
else :
    h4_niveau_occupation = "[OK]"

# Pour h5
if h5_taux_occupation > 95:
    h5_niveau_occupation = "[CRI]"
elif h5_taux_occupation > 85:
    h5_niveau_occupation = "[ALT]"
else :
    h5_niveau_occupation = "[OK]"

# Calcul du niveau d'alerte global pour chaque hôpital
# Pour h1
if (h1_nb_ruptures >= 2 or h1_taux_occupation > 95) :
    h1_niveau_alerte = "[CRITIQUE]"
    hopital_critique = hopital_critique + 1
elif (h1_nb_ruptures >= 1 or h1_taux_occupation > 85) or (h1_nb_alerte >= 2 and h1_nb_medecins <5) :
    h1_niveau_alerte = "[PREOCCUPANT]"
else :
    h1_niveau_alerte = "[SATISFAISANT]"

# Pour h2
if (h2_nb_ruptures >= 2 or h2_taux_occupation > 95) :
    h2_niveau_alerte = "[CRITIQUE]"
    hopital_critique = hopital_critique + 1
elif (h2_nb_ruptures >= 1 or h2_taux_occupation > 85) or (h2_nb_alerte >= 2 and h2_nb_medecins <5) :
    h2_niveau_alerte = "[PREOCCUPANT]"
else :
    h2_niveau_alerte = "[SATISFAISANT]"

# Pour h3
if (h3_nb_ruptures >= 2 or h3_taux_occupation > 95) :
    h3_niveau_alerte = "[CRITIQUE]"
    hopital_critique = hopital_critique + 1
elif (h3_nb_ruptures >= 1 or h3_taux_occupation > 85) or (h3_nb_alerte >= 2 and h3_nb_medecins <5) :
    h3_niveau_alerte = "[PREOCCUPANT]"
else :
    h3_niveau_alerte = "[SATISFAISANT]" 

# Pour h4
if (h4_nb_ruptures >= 2 or h4_taux_occupation > 95) :
    h4_niveau_alerte = "[CRITIQUE]"
    hopital_critique = hopital_critique + 1
elif (h4_nb_ruptures >= 1 or h4_taux_occupation > 85) or (h4_nb_alerte >= 2 and h4_nb_medecins <5) :
    h4_niveau_alerte = "[PREOCCUPANT]"
else :
    h4_niveau_alerte = "[SATISFAISANT]"

# Pour h5
if (h5_nb_ruptures >= 2 or h5_taux_occupation > 95) :
    h5_niveau_alerte = "[CRITIQUE]"
    hopital_critique = hopital_critique + 1
elif (h5_nb_ruptures >= 1 or h5_taux_occupation > 85) or (h5_nb_alerte >= 2 and h5_nb_medecins <5) :
    h5_niveau_alerte = "[PREOCCUPANT]"
else :
    h5_niveau_alerte = "[SATISFAISANT]" 

# Affichage du tableau de bord sanitaire
print("\nTABLEAU DE BORD SANITAIRE") 
print("-"*100)
print(f"{'HOPITAL':<40} | {'OCCUPATION':<20} | {'ALERTES':<15} | {'NIVEAU GLOBAL':<15} ")
print('-'*100)
print(f"{h1_nom:<40} | {h1_taux_occupation} % {h1_niveau_occupation}      | {h1_nb_ruptures}R + {h1_nb_alerte}{'A':<10.2s} | {h1_niveau_alerte:<15}   ")
print(f"{h2_nom:<40} | {h2_taux_occupation} % {h2_niveau_occupation}      | {h2_nb_ruptures}R + {h2_nb_alerte}{'A':<10.2s} | {h2_niveau_alerte:<15}   ")
print(f"{h3_nom:<40} | {h3_taux_occupation} % {h3_niveau_occupation}      | {h3_nb_ruptures}R + {h3_nb_alerte}{'A':<10.2s} | {h3_niveau_alerte:<15}   ")
print(f"{h4_nom:<40} | {h4_taux_occupation} % {h4_niveau_occupation}      | {h4_nb_ruptures}R + {h4_nb_alerte}{'A':<10.2s} | {h4_niveau_alerte:<15}   ")
print(f"{h5_nom:<40} | {h5_taux_occupation} % {h5_niveau_occupation}      | {h5_nb_ruptures}R + {h5_nb_alerte}{'A':<10.2s} | {h5_niveau_alerte:<15}   ")

# Calcul du compteur du bilan national
# Hopitaux en situation critique
print("\nBILAN NATIONAL")
print("-"*100)
print(f"{hopital_critique} sont en situation critique sur 5 hopitaux")
print(f"{h1_nb_ruptures + h2_nb_ruptures + h3_nb_ruptures + h4_nb_ruptures + h5_nb_ruptures} medicaments en rupture de stock à l'echelle nationale")
