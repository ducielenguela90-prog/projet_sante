# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 2 : Triage Patient Urgences CHU Brazzaville
# Notions S2 : variables, types, input(), f-strings, conversion
# Notions S3 : if/elif/else, conditions composees or/and/not
# ============================================================
print('=== SYSTEME DE TRIAGE — URGENCES CHU BRAZZAVILLE ===')
print('Protocole Manchester adapte — DSS Congo 2026')
print()

# --- SAISIE DES DONNEES PATIENT (S2 reutilise : input(), conversion) ---
nom_patient = input('Nom du patient : ')
age_patient = int(input('Age (annees) : '))
temperature = float(input('Temperature (degres C, ex: 38.4) : '))
spo2 = float(input('Saturation O2 en % (ex: 96.0) : '))
tension_syst = int(input('Tension systolique en mmHg (ex: 135) : '))
douleur = int(input('Douleur /10 (0=aucune, 10=insupportable) : '))

# --- VALIDATION DES PLAGES (S2 + S3 : conditions simples) ---
# Verifier que la temperature est dans une plage physiologiquement possible
if temperature < 35.0 or temperature > 43.0:
 print('ERREUR : Valeur de temperature impossible — verifier la saisie')
 # Dans une version avancee, on redemanderait la saisie ici
elif spo2 < 50.0 or spo2 > 100.0:
 print('ERREUR : SpO2 hors plage — verifier le capteur')
elif tension_syst < 50 or tension_syst > 250:
 print('ERREUR : Tension hors plage — verifier le brassard')
elif douleur < 0 or douleur > 10:
 print('ERREUR : Douleur doit être entre 0 et 10')
elif age_patient < 0 or age_patient > 120:
 print('ERREUR : Age invalide — verifier la saisie')
# TODO : Valider spo2, tension_syst, douleur, age de la meme facon
# --- TRIAGE (S3 nouveau : conditions composees avec or) ---
# Niveau 1 : IMMEDIAT — au moins UNE condition critique suffit (or)
   
if temperature > 39.5 or spo2 < 90 or tension_syst > 180:
    niveau_triage = '1 — IMMEDIAT'
    couleur_triage = '[ROUGE]'
    delai_pec = '0 minute'
    action_triage = 'Medecin present immediatement — code ROUGE active'
    
    # Motif principal
    if temperature > 39.5:
        motif_principal = f'Temperature critique {temperature}°C - seuil 39.5°C'
    elif spo2 < 90:
        motif_principal = f'Saturation O2 critique {spo2}% - seuil 90%'
    elif tension_syst > 180:
        motif_principal = f'Tension systolique critique {tension_syst} mmHg  - seuil 180 mmHg'
# Niveau 2 : URGENT — conditions moins critiques mais toujours urgentes
elif temperature > 38.5 or spo2 < 94 or tension_syst > 140 or douleur >= 7:
    niveau_triage = '2 — URGENT'
    couleur_triage = '[ORANGE]'
    delai_pec = '10 minutes'
    action_triage = 'Appel medecin senior'
    # Motif principal
    if temperature > 38.5:
        motif_principal = f'Temperature moins critique {temperature}°C - seuil 39.5°C'
    elif spo2 < 94:
        motif_principal = f'Saturation O2 {spo2}% - seuil 90%'
    elif tension_syst > 140:
        motif_principal = f'Tension systolique critique {tension_syst} mmHg  - seuil 180 mmHg'
    elif douleur >= 7:
        motif_principal = f'Douleur severe {douleur}/10 - seuil 7/10'
# Niveau 3 : URGENT DIFFERE
elif temperature > 37.5 or douleur > 6 :
    niveau_triage = '3 — URGENT DIFFERE'
    couleur_triage = '[JAUNE]'
    delai_pec = '30 minutes'
    action_triage = 'Infirmier - surveillance'
    # Motif principal
    if temperature > 37.5:
        motif_principal = f'Temperature anormale {temperature}°C - seuil 37.5°C'
    elif douleur > 6:
        motif_principal = f'Douleur moderee {douleur}/10 - seuil 7/10'

# Niveau 4 : MOINS URGENT (cas par defaut)
else:
    niveau_triage = '4 — MOINS URGENT'
    couleur_triage = '[VERT]'
    delai_pec = '120 minutes'
    action_triage = "File d'attende standard"
    # Motif principal
    if temperature <= 37.5 and douleur <= 6:
        motif_principal = f'Parametres vitaux normaux — Temperature {temperature}°C, Douleur {douleur}/10' 

# --- AFFICHAGE FICHE TRIAGE (S2 reutilise : f-strings) ---
print()
print('=' * 55)
print(f' RESULTAT TRIAGE — {nom_patient.upper()}')
print('=' * 55)

# TODO : Afficher tous les parametres vitaux et le resultat du triage
print("PARAMETRES VITAUX")
print('-'*55)

statut_temperature = "[ANORMAL > 39.5°C]" if temperature > 39.5 else "[NORMAL]"
statut_spo2 = "[NORMAL]" if spo2 >= 50 and spo2 < 100 else "[ANORMAL]"
statut_tension = "[NORMAL]" if tension_syst >= 50 and tension_syst <= 250 else "[ANORMAL]"
statut_douleur = "[NORMAL]" if douleur >=0 and douleur <= 10 else "[ANORMAL]"

print(f'Temperature : {temperature} °C {statut_temperature}')
print(f'Saturation O2 : {spo2} % {statut_spo2}')
print(f'Tension systolique : {tension_syst} mmHg {statut_tension}')
print(f'Douleur : {douleur} /10 {statut_douleur}') 
print('-'*55)
print(f'NIVEAU DE TRIAGE : {niveau_triage}')
print(f'COULEUR TRIAGE : {couleur_triage}')
print(f'PRISE EN CHARGE : {delai_pec}')
print(f'ACTION : {action_triage}')
print('-' * 55)
print(f'Motif principal : {motif_principal}')
print('=' * 55)
