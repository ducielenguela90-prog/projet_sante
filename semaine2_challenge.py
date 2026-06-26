# ===========================================================
# AKIENI ACADEMY — Projet Santé Publique
# Semaine 2 — Challenge Entreprise : Rapport Comparatif des 3 Hôpitaux du Pool
# ===========================================================

# DONNEES DES 3 HÔPITAUX ---
# Hôpital 1 : Hôpital District Kinkala
h1_nom = "Hopital District Kinkala"
h1_budget = 12_500_000
h1_consultations = 1847
h1_hospitalisations = 312
h1_deces = 8
h1_lits_totaux = 45
h1_lits_occupes = 41
h1_medecins = 3
h1_population = 85_000

# Hôpital 2 : CMS de Vindza
h2_nom = "CMS de Vindza"
h2_budget = 6_800_000
h2_consultations = 923
h2_hospitalisations = 87
h2_deces = 2
h2_lits_totaux = 20
h2_lits_occupes = 14
h2_medecins = 1
h2_population = 42_000

# Hôpital 3 : Hôpital de Kindamba
h3_nom = "Hopital de Kindamba"
h3_budget = 9_200_000
h3_consultations = 1234
h3_hospitalisations = 201
h3_deces = 11
h3_lits_totaux = 35
h3_lits_occupes = 33
h3_medecins = 2
h3_population = 67_000

# Coût d'un médecin (Bonus)
cout_medecin_trimestriel = 1_200_000  # FCFA

# CALCULS DES KPIs POUR CHAQUE HÔPITAL

# Hôpital 1 : Kinkala
h1_cout_moyen_par_patient = h1_budget / (h1_consultations + h1_hospitalisations)
h1_taux_occupation = round((h1_lits_occupes / h1_lits_totaux) * 100, 1)
h1_densite_medicale = round((h1_medecins / h1_population) * 1000, 2)
h1_taux_mortalite = round((h1_deces / h1_hospitalisations) * 100, 1) if h1_hospitalisations != 0 else 0
h1_est_critique = (h1_taux_mortalite > 2) or (h1_densite_medicale < 0.05)

# Hôpital 2 : Vindza
h2_cout_moyen_par_patient = h2_budget / (h2_consultations + h2_hospitalisations)
h2_taux_occupation = round((h2_lits_occupes / h2_lits_totaux) * 100, 1)
h2_densite_medicale = round((h2_medecins / h2_population) * 1000, 2)
h2_taux_mortalite = round((h2_deces / h2_hospitalisations) * 100, 1) if h2_hospitalisations != 0 else 0
h2_est_critique = (h2_taux_mortalite > 2) or (h2_densite_medicale < 0.05)

# Hôpital 3 : Kindamba
h3_cout_moyen_par_patient = h3_budget / (h3_consultations + h3_hospitalisations)
h3_taux_occupation = round((h3_lits_occupes / h3_lits_totaux) * 100, 1)
h3_densite_medicale = round((h3_medecins / h3_population) * 1000, 2)
h3_taux_mortalite = round((h3_deces / h3_hospitalisations) * 100, 1) if h3_hospitalisations != 0 else 0
h3_est_critique = (h3_taux_mortalite > 2) or (h3_densite_medicale < 0.05)

# --- BONUS : BUDGET POUR 5 MÉDECINS SUPPLÉMENTAIRES PAR HÔPITAL ---
budget_total = h1_budget + h2_budget + h3_budget
cout_5_medecins_par_hopital = 5 * cout_medecin_trimestriel
cout_total_5_medecins = 3 * cout_5_medecins_par_hopital  # 5 médecins pour chaque hôpital
budget_suffisant = budget_total >= cout_total_5_medecins

# --- AFFICHAGE DU RAPPORT ---
print("==========================================================")
print("RAPPORT COMPARATIF DES 3 HOPITAUX DU POOL - Q4 2025")
print("==========================================================")

# Hôpital 1 : Kinkala
print(f"\n--- {h1_nom} ---")
print(f"Budget trimestriel : {h1_budget:,} FCFA")
print(f"Cout moyen par patient : {h1_cout_moyen_par_patient:,.2f} FCFA")
print(f"Taux d'occupation des lits : {h1_taux_occupation}%")
print(f"Densite medicale : {h1_densite_medicale} médecins/1000 hab")
print(f"Taux de mortalite : {h1_taux_mortalite}%")
if h1_est_critique:
    print("STATUT : **CRITIQUE**")
else:
    print("STATUT : OK")

# Hôpital 2 : Vindza
print(f"\n--- {h2_nom} ---")
print(f"Budget trimestriel : {h2_budget:,} FCFA")
print(f"Cout moyen par patient : {h2_cout_moyen_par_patient:,.2f} FCFA")
print(f"Taux d'occupation des lits : {h2_taux_occupation}%")
print(f"Densite medicale : {h2_densite_medicale} médecins/1000 hab")
print(f"Taux de mortalite : {h2_taux_mortalite}%")
if h2_est_critique:
    print("STATUT : **CRITIQUE**")
else:
    print("STATUT : OK")

# Hôpital 3 : Kindamba
print(f"\n--- {h3_nom} ---")
print(f"Budget trimestriel : {h3_budget:,} FCFA")
print(f"Cout moyen par patient : {h3_cout_moyen_par_patient:,.2f} FCFA")
print(f"Taux d'occupation des lits : {h3_taux_occupation}%")
print(f"Densite medicale : {h3_densite_medicale} médecins/1000 hab")
print(f"Taux de mortalite : {h3_taux_mortalite}%")
if h3_est_critique:
    print("STATUT : **CRITIQUE**")
else:
    print("STATUT : OK")

# --- IDENTIFICATION DES HÔPITAUX CRITIQUES ---
print("============================")
print("ANALYSE CRITIQUE")
print("============================")
if h1_est_critique:
    print(f"{h1_nom} est en situation CRITIQUE !")
if h2_est_critique:
    print(f"{h2_nom} est en situation CRITIQUE !")
if h3_est_critique:
    print(f"{h3_nom} est en situation CRITIQUE !")

# --- BONUS : ANALYSE BUDGÉTAIRE POUR 5 MÉDECINS SUPPLÉMENTAIRES ---
print("=======================================================================")
print("BONUS : ANALYSE BUDGETAIRE POUR 5 MEDECINS SUPPLEMENTAIRES PAR HOPITAL")
print("=======================================================================")
print(f"Budget total des 3 hopitaux : {budget_total:,} FCFA")
print(f"Coût pour 5 medecins supplementaires par hopital : {cout_5_medecins_par_hopital:,} FCFA")
print(f"Coût total pour 15 medecins (5 par hopital) : {cout_total_5_medecins:,} FCFA")
if budget_suffisant :
    print("Budget SUFFISANT pour embaucher 5 medecins supplementaires dans chaque hopital.")
else:
    print("Budget INSUFFISANT pour embaucher 5 médecins supplementaires dans chaque hopital.")