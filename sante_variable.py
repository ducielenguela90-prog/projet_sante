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
m1_stock = int(input("Entrez le stock actuel d'Artemether-Lumefantrine : "))
m1_seuil_rupture = 2000
m1_cout_unitaire = 3500.0  # en FCFA

# Médicament 2 - Amoxicilline 500mg (antibiotique)
m2_nom = 'Amoxicilline 500mg'
m2_stock = int(input("Entrez le stock actuel d'Amoxicilline 500mg : "))
m2_seuil_rupture = 800
m2_cout_unitaire = 850.0  # en FCFA

# Médicament 3 - Paracétamol (antidouleur)
m3_nom = 'Paracétamol'
m3_stock = int(input("Entrez le stock actuel de Paracétamol : "))
m3_seuil_rupture = 5000
m3_cout_unitaire = 125.0  # en FCFA

# Médicament 4 - SRO
m4_nom = 'Sérum de Réhydratation Orale'
m4_stock = int(input("Entrez le stock actuel de Sérum de Réhydratation Orale : "))
m4_seuil_rupture = 5000
m4_cout_unitaire = 125.0  # en FCFA

# Médicament 5 - Vaccin Antipaludéen
m5_nom = 'Vaccin Antipaludéen'
m5_stock = int(input("Entrez le stock actuel de Vaccin Antipaludéen : "))
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

# === SECTION F : Classification automatique du statut des stocks (PNA) ===

# Médicament 1 - Artemether-Lumefantrine
if m1_stock <= m1_seuil_rupture:
    m1_statut = "RUPTURE CRITIQUE"
    m1_couleur = "[ROUGE]"
    m1_action = "Alerte immédiate PNA - commande express sous 24h"
elif m1_stock <= m1_seuil_rupture * 1.5:
    m1_statut = "ALERTE STOCK"
    m1_couleur = "[ORANGE]"
    m1_action = "Commande urgente à déclencher sous 72h"
elif m1_stock <= m1_seuil_rupture * 2.0:
    m1_statut = "STOCK LIMITE"
    m1_couleur = "[JAUNE]"
    m1_action = "Surveillance renforcée - planifier commande"
else:
    m1_statut = "STOCK NORMAL"
    m1_couleur = "[VERT]"
    m1_action = "Situation normale - suivi standard"

# Médicament 2 - Amoxicilline 500mg
if m2_stock <= m2_seuil_rupture:
    m2_statut = "RUPTURE CRITIQUE"
    m2_couleur = "[ROUGE]"
    m2_action = "Alerte immédiate PNA - commande express sous 24h"
elif m2_stock <= m2_seuil_rupture * 1.5:
    m2_statut = "ALERTE STOCK"
    m2_couleur = "[ORANGE]"
    m2_action = "Commande urgente à déclencher sous 72h"
elif m2_stock <= m2_seuil_rupture * 2.0:
    m2_statut = "STOCK LIMITE"
    m2_couleur = "[JAUNE]"
    m2_action = "Surveillance renforcée - planifier commande"
else:
    m2_statut = "STOCK NORMAL"
    m2_couleur = "[VERT]"
    m2_action = "Situation normale - suivi standard"

# Médicament 3 - Paracétamol
if m3_stock <= m3_seuil_rupture:
    m3_statut = "RUPTURE CRITIQUE"
    m3_couleur = "[ROUGE]"
    m3_action = "Alerte immédiate PNA - commande express sous 24h"
elif m3_stock <= m3_seuil_rupture * 1.5:
    m3_statut = "ALERTE STOCK"
    m3_couleur = "[ORANGE]"
    m3_action = "Commande urgente à déclencher sous 72h"
elif m3_stock <= m3_seuil_rupture * 2.0:
    m3_statut = "STOCK LIMITE"
    m3_couleur = "[JAUNE]"
    m3_action = "Surveillance renforcée - planifier commande"
else:
    m3_statut = "STOCK NORMAL"
    m3_couleur = "[VERT]"
    m3_action = "Situation normale - suivi standard"

# Médicament 4 - Ibuprofène
if m4_stock <= m4_seuil_rupture:
    m4_statut = "RUPTURE CRITIQUE"
    m4_couleur = "[ROUGE]"
    m4_action = "Alerte immédiate PNA - commande express sous 24h"
elif m4_stock <= m4_seuil_rupture * 1.5:
    m4_statut = "ALERTE STOCK"
    m4_couleur = "[ORANGE]"
    m4_action = "Commande urgente à déclencher sous 72h"
elif m4_stock <= m4_seuil_rupture * 2.0:
    m4_statut = "STOCK LIMITE"
    m4_couleur = "[JAUNE]"
    m4_action = "Surveillance renforcée - planifier commande"
else:
    m4_statut = "STOCK NORMAL"
    m4_couleur = "[VERT]"
    m4_action = "Situation normale - suivi standard"   

# Médicament 5 - Vaccin Antipaludéen
if m5_stock <= m5_seuil_rupture:
    m5_statut = "RUPTURE CRITIQUE"
    m5_couleur = "[ROUGE]"
    m5_action = "Alerte immédiate PNA - commande express sous 24h"
elif m5_stock <= m5_seuil_rupture * 1.5:
    m5_statut = "ALERTE STOCK"
    m5_couleur = "[ORANGE]"
    m5_action = "Commande urgente à déclencher sous 72h"
elif m5_stock <= m5_seuil_rupture * 2.0:
    m5_statut = "STOCK LIMITE"
    m5_couleur = "[JAUNE]"
    m5_action = "Surveillance renforcée - planifier commande"
else:
    m5_statut = "STOCK NORMAL"
    m5_couleur = "[VERT]"
    m5_action = "Situation normale - suivi standard"

# === SECTION G : Classification occupation hôpitaux ===

# Hôpital 1 - CHU Brazzaville
h1_taux_occupation = round((h1_nb_lits_occupes / h1_nb_lits) * 100, 2)
if h1_taux_occupation > 95:
    h1_niveau_occupation = "ALERTE CRITIQUE"
elif h1_taux_occupation > 85:
    h1_niveau_occupation = "ALERTE ÉLEVÉE"
elif h1_taux_occupation > 70:
    h1_niveau_occupation = "SITUATION OPTIMALE"
else:
    h1_niveau_occupation = "SOUS-UTILISATION"

# Hôpital 2 - Hôpital Général Pointe-Noire
h2_taux_occupation = round((h2_nb_lits_occupes / h2_nb_lits) * 100, 2)
if h2_taux_occupation > 95:
    h2_niveau_occupation = "ALERTE CRITIQUE"
elif h2_taux_occupation > 85:
    h2_niveau_occupation = "ALERTE ÉLEVÉE"
elif h2_taux_occupation > 70:
    h2_niveau_occupation = "SITUATION OPTIMALE"
else:
    h2_niveau_occupation = "SOUS-UTILISATION"

# Hôpital 3 - Hôpital de Dolisie
h3_taux_occupation = round((h3_nb_lits_occupes / h3_nb_lits) * 100, 2)
if h3_taux_occupation > 95:
    h3_niveau_occupation = "ALERTE CRITIQUE"
elif h3_taux_occupation > 85:
    h3_niveau_occupation = "ALERTE ÉLEVÉE"
elif h3_taux_occupation > 70:
    h3_niveau_occupation = "SITUATION OPTIMALE"
else:
    h3_niveau_occupation = "SOUS-UTILISATION"  

# Hôpital 4 - Hôpital de District Owando
h4_taux_occupation = round((h4_nb_lits_occupes / h4_nb_lits) * 100, 2)
if h4_taux_occupation > 95:
    h4_niveau_occupation = "ALERTE CRITIQUE"
elif h4_taux_occupation > 85:
    h4_niveau_occupation = "ALERTE ÉLEVÉE"
elif h4_taux_occupation > 70:
    h4_niveau_occupation = "SITUATION OPTIMALE"
else:
    h4_niveau_occupation = "SOUS-UTILISATION"

# Hôpital 5 - Centre de Santé de Impfondo
h5_taux_occupation = round((h5_nb_lits_occupes / h5_nb_lits) * 100, 2)
if h5_taux_occupation > 95: 
    h5_niveau_occupation = "ALERTE CRITIQUE"
elif h5_taux_occupation > 85:
    h5_niveau_occupation = "ALERTE ÉLEVÉE"
elif h5_taux_occupation > 70:
    h5_niveau_occupation = "SITUATION OPTIMALE"
else:
    h5_niveau_occupation = "SOUS-UTILISATION"


# === SECTION H : Classification couverture vaccinale ===

# Département 1 - Brazzaville
d1_nom = "Brazzaville"
d1_population = 450000
d1_vaccines = 418500
d1_taux_couverture = round((d1_vaccines / d1_population) * 100, 2)

if d1_taux_couverture < 50:
    d1_statut_vaccinal = "ZONE CRITIQUE"
elif d1_taux_couverture < 80:
    d1_statut_vaccinal = "ZONE À RISQUE"
elif d1_taux_couverture < 95:
    d1_statut_vaccinal = "ZONE INSUFFISANTE"
else:
    d1_statut_vaccinal = "ZONE CONFORME"

# Département 2 - Pointe-Noire
d2_nom = "Pointe-Noire"
d2_population = 280000
d2_vaccines = 229600
d2_taux_couverture = round((d2_vaccines / d2_population) * 100, 2)

if d2_taux_couverture < 50:
    d2_statut_vaccinal = "ZONE CRITIQUE"
elif d2_taux_couverture < 80:
    d2_statut_vaccinal = "ZONE À RISQUE"
elif d2_taux_couverture < 95:
    d2_statut_vaccinal = "ZONE INSUFFISANTE"
else:
    d2_statut_vaccinal = "ZONE CONFORME"

# Département 3 - Pool
d3_nom = "Pool"
d3_population = 120000
d3_vaccines = 54000
d3_taux_couverture = round((d3_vaccines / d3_population) * 100, 2)

if d3_taux_couverture < 50:
    d3_statut_vaccinal = "ZONE CRITIQUE"
elif d3_taux_couverture < 80:
    d3_statut_vaccinal = "ZONE À RISQUE"
elif d3_taux_couverture < 95:
    d3_statut_vaccinal = "ZONE INSUFFISANTE"
else:
    d3_statut_vaccinal = "ZONE CONFORME"

# Département 4 - Sangha
d4_nom = "Sangha"
d4_population = 85000
d4_vaccines = 35700
d4_taux_couverture = round((d4_vaccines / d4_population) * 100, 2)

if d4_taux_couverture < 50:
    d4_statut_vaccinal = "ZONE CRITIQUE"
elif d4_taux_couverture < 80:
    d4_statut_vaccinal = "ZONE À RISQUE"
elif d4_taux_couverture < 95:
    d4_statut_vaccinal = "ZONE INSUFFISANTE"
else:
    d4_statut_vaccinal = "ZONE CONFORME"
