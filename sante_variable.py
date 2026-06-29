# ===========================================================
# MODULE FONDATEUR - Projet Santé Publique / Akieni Academy
# Ce fichier centralise toutes les constantes et variables métier.
# Il sera enrichi chaque semaine jusqu'à la S24.
# ===========================================================

# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ===
# Taux de change (FCFA vers EUR et USD)
TAUX_EUR_FCFA = 655.957
TAUX_USD_FCFA = 600.0

# Seuils OMS pour les indicateurs de santé
SEUIL_OMS_DENSITE_MEDICALE = 2.3  # médecins pour 1000 habitants
SEUIL_OMS_COUVERTURE_VACCIN = 95.0  # pourcentage minimum OMS
SEUIL_MORTALITE_ALERTE = 2.0  # % décès / hospitalisations
SEUIL_RUPTURE_STOCK_JOURS = 30  # jours minimum de stock

# Liste des 12 départements du Congo
DEPARTEMENTS_CONGO = ['Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette',
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala',
    'Niari', 'Plateaux', 'Pool', 'Sangha'
]

# === SECTION B : VARIABLES DES 5 HÔPITAUX ===
# Hôpital 1 - CHU de Brazzaville
h1_nom = 'CHU de Brazzaville'
h1_ville = 'Brazzaville'
h1_departement = 'Brazzaville'
h1_type = 'CHU'
h1_nb_lits = 320
h1_nb_lits_occupes = 284
h1_nb_medecins = 47
h1_nb_infirmiers = 123
h1_population_zone = 1_800_000  # Population desservie

# Hôpital 2 - Hôpital Général de Pointe-Noire
h2_nom = 'Hôpital Général de Pointe-Noire'
h2_ville = 'Pointe-Noire'
h2_departement = 'Pointe-Noire'
h2_type = 'Hôpital Général'
h2_nb_lits = 180
h2_nb_lits_occupes = 143
h2_nb_medecins = 22
h2_nb_infirmiers = 58
h2_population_zone = 1_200_000

# Hôpital 3 - Hôpital de Dolisie
h3_nom = 'Hôpital de Dolisie'
h3_ville = 'Dolisie'
h3_departement = 'Niari'
h3_type = 'Hôpital de District'
h3_nb_lits = 120
h3_nb_lits_occupes = 95
h3_nb_medecins = 15
h3_nb_infirmiers = 40
h3_population_zone = 800_000

# Hôpital 4 - Hôpital de District Owando
h4_nom = 'Hôpital de District Owando'
h4_ville = 'Owando'
h4_departement = 'Cuvette'
h4_type = 'Hôpital de District'
h4_nb_lits = 80
h4_nb_lits_occupes = 60
h4_nb_medecins = 8
h4_nb_infirmiers = 25
h4_population_zone = 500_000

# Hôpital 5 - Centre de Santé de Impfondo
h5_nom = 'Centre de Santé de Impfondo'
h5_ville = 'Impfondo'
h5_departement = 'Likouala'
h5_type = 'Centre de Santé'
h5_nb_lits = 30
h5_nb_lits_occupes = 20
h5_nb_medecins = 3
h5_nb_infirmiers = 10
h5_population_zone = 200_000

# === SECTION C : VARIABLES DES 5 MÉDICAMENTS ===
# Médicament 1 - Artemether-Lumefantrine (antipaludéen)
m1_nom = 'Artemether-Lumefantrine'
m1_stock = 8450
m1_seuil_rupture = 2000
m1_cout_unitaire = 3500.0  # en FCFA

# Médicament 2 - Amoxicilline 500mg (antibiotique)
m2_nom = 'Amoxicilline 500mg'
m2_stock = 3200
m2_seuil_rupture = 800
m2_cout_unitaire = 850.0  # en FCFA

# Médicament 3 - Paracétamol (antidouleur)
m3_nom = 'Paracétamol'
m3_stock = 15000
m3_seuil_rupture = 5000
m3_cout_unitaire = 125.0  # en FCFA

# Médicament 4 - SRO
m4_nom = 'Sérum de Réhydratation Orale'
m4_stock = 15600
m4_seuil_rupture = 5000
m4_cout_unitaire = 125.0  # en FCFA

# Médicament 5 - Vaccin Antipaludéen
m5_nom = 'Vaccin Antipaludéen'
m5_stock = 5000
m5_seuil_rupture = 1000
m5_cout_unitaire = 2000.0  # en FCFA

# === SECTION D : CALCULS D'INITIALISATION ===
# 1. Densité médicale nationale
total_medecins = h1_nb_medecins + h2_nb_medecins + h3_nb_medecins + h4_nb_medecins + h5_nb_medecins #Le total des médécins
total_population = h1_population_zone + h2_population_zone + h3_population_zone + h4_population_zone + h5_population_zone #Le total de la population des cinq villes 
densite_medicale_nationale = round((total_medecins / total_population) * 1000, 2)

# 2. Taux d'occupation moyen
total_lits = h1_nb_lits + h2_nb_lits + h3_nb_lits + h4_nb_lits + h5_nb_lits
total_lits_occupes = h1_nb_lits_occupes + h2_nb_lits_occupes + h3_nb_lits_occupes + h4_nb_lits_occupes + h5_nb_lits_occupes
taux_occupation_moyen = round((total_lits_occupes / total_lits) * 100, 2)

# 3. Valeur totale du stock de médicaments
valeur_totale_stock = m1_stock * m1_cout_unitaire + m2_stock * m2_cout_unitaire + m3_stock * m3_cout_unitaire + m4_stock * m4_cout_unitaire + m5_stock * m5_cout_unitaire

# === SECTION E : RAPPORT D'INVENTAIRE ===
print("==================================================================================")
print("RAPPORT D'INVENTAIRE INITIAL - SYSTEME DE SANTE CONGOLAIS")
print("==================================================================================")

print("\n--- CONSTANTES NATIONALES ---")
print(f"Taux EUR/FCFA : {TAUX_EUR_FCFA}")
print(f"Taux USD/FCFA : {TAUX_USD_FCFA}")
print(f"Seuil OMS densité médicale : {SEUIL_OMS_DENSITE_MEDICALE} medecins/1000 hab")
print(f"Seuil OMS couverture vaccin : {SEUIL_OMS_COUVERTURE_VACCIN}%")
print(f"Seuil alerte mortalite : {SEUIL_MORTALITE_ALERTE}%")
print(f"Seuil rupture stock : {SEUIL_RUPTURE_STOCK_JOURS} jours")

print("\n--- KPIs GLOBAUX ---")
print(f"Densite medicale nationale : {densite_medicale_nationale} medecins/1000 hab")
print(f"Taux d'occupation moyen : {taux_occupation_moyen}%")
print(f"Valeur totale du stock : {valeur_totale_stock:,} FCFA")

'''
print("\n--- ALERTES ---")
if densite_medicale_nationale < SEUIL_OMS_DENSITE_MEDICALE:
    print(f"! ALERTE : Densite medicale nationale critique ({densite_medicale_nationale} < {SEUIL_OMS_DENSITE_MEDICALE})")
if taux_occupation_moyen > 85:
    print(f"ALERTE : Taux d'occupation moyen eleve ({taux_occupation_moyen}% > 85%)")
if taux_occupation_moyen < 70:
    print(f"ALERTE : Taux d'occupation moyen faible ({taux_occupation_moyen}% < 70%)")
    
'''
