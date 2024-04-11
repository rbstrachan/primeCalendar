import datetime

annee_debut = 2020
annee_finale = 2029

def est_premier(n):
  """
  Fonction qui vérifie si un nombre est premier.

  Args:
    n: Le nombre à tester (entier).

  Returns:
    True si n est premier, False sinon.
  """
  if n <= 1:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

def generer_dates_primes(annee):
  """
  Fonction qui génère toutes les dates primes d'une année donnée au format YYYYMMDD.

  Args:
    annee: L'année à traiter (entier).

  Returns:
    Une liste de chaînes de caractères représentant les dates au format YYYYMMDD.
  """
  dates_primes = []
  for mois in range(1, 13):
    nb_jours = 31 if mois in (1, 3, 5, 7, 8, 10, 12) else 30
    if mois == 2:
      nb_jours = 28 if annee % 4 != 0 else 29
    for jour in range(1, nb_jours + 1):
      date = f"{annee:04d}{mois:02d}{jour:02d}"
      valeur_date = int(date)
      if est_premier(valeur_date):
        dates_primes.append(date)
  return dates_primes

# Accumulateur pour toutes les dates primes
all_dates_primes = []

# Boucle sur les années indiquées (inclusive)
for annee in range(annee_debut, annee_finale + 1):
  dates_primes = generer_dates_primes(annee)
  all_dates_primes.extend(dates_primes)  # Ajout des dates de l'année courante à l'accumulateur

def generer_fichier_ics(all_dates_primes):
  """
  Fonction qui génère un fichier .ics contenant toutes les dates primes entre 2020 et 2030 (inclus), en tant qu'événements "all-day".

  Args:
    all_dates_primes: Une liste contenant toutes les dates primes de toutes les années entre 2020 et 2030 (inclus) au format YYYYMMDD.

  Returns:
    Le contenu du fichier .ics en tant que chaîne de caractères.
  """

  contenu_ics = "BEGIN:VCALENDAR\n"
  contenu_ics += "VERSION:2.0\n"
  contenu_ics += "PRODID:-//reiwa//ICS Prime Dates Generator//EN\n"
  contenu_ics += "X-WR-CALNAME:Primes Days Calendar — 2020–2030\n"  # Combined calendar name

  for date_prime in all_dates_primes:
    date_objet = datetime.datetime.strptime(date_prime, "%Y%m%d")
    contenu_ics += "BEGIN:VEVENT\n"
    contenu_ics += "DTSTART;VALUE=DATE:" + date_prime + "\n"  # No time component for all-day events
    contenu_ics += "DTEND;VALUE=DATE:" + date_prime + "\n"  # No time component for all-day events
    contenu_ics += "SUMMARY:prime (" + date_prime + ")\n"
    contenu_ics += "UID:" + date_prime + "\n"
    contenu_ics += "END:VEVENT\n"

  contenu_ics += "END:VCALENDAR\n"

  return contenu_ics

# Génération du fichier .ics avec toutes les dates primes
fichier_ics = generer_fichier_ics(all_dates_primes)

# print le contenu de fichier_ics
print(fichier_ics)