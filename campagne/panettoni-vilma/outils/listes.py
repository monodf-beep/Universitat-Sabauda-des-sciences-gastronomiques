"""Fusionne les adresses e-mail relevées avec le tableau des commerces et écrit les listes.

Entrées : `listes/source/cibles-*.csv` (tableau de prospection, priorités A, B, ?) et
`listes/source/emails-*.csv` (adresses relevées le 04/11/2026, une ligne par enseigne).
Sorties :
- `listes/a-importer-brevo.csv` : adresses publiées, avec leur source, prêtes pour la liste Brevo #16 ;
- `listes/a-verifier.csv` : adresses vues mais douteuses (nominatives, source faible) : à la main ;
- `listes/suivi.csv` : une ligne par enseigne, pour suivre mails, appels et mise en relation.
"""
import csv
import re
import unicodedata
from pathlib import Path

ICI = Path(__file__).resolve().parent.parent / "listes"
SRC = ICI / "source"


def norme(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    return set(w for w in re.findall(r"[a-z0-9]+", t) if len(w) > 2 and w not in {
        "les", "des", "aux", "the", "siege", "reseau", "boutique", "magasin", "fromagerie", "cave",
        "epicerie", "biocoop", "coop", "cooperative", "laitiere"})


def type_commerce(t):
    t = (t or "").lower()
    if "fromag" in t or "crèm" in t or "crem" in t or "laiti" in t or "coopérative" in t or "affineur" in t:
        return "fromagerie"
    if "bio" in t or "diét" in t:
        return "bio"
    if t.startswith("épicerie") or t.startswith("epicerie"):
        return "epicerie"
    if "cavist" in t or "cave" in t or "vin" in t:
        return "caviste"
    return "epicerie"


# Adresses relevées mais à ne pas importer (décidé le 04/11/2026), avec la raison, reportée dans le suivi.
ECARTES = {
    "Tendance Nature": "devenue une boutique CBD",
    "Les Halles des Haras": "adresse du service communication de l'exploitant (Biltoki) : démarcher stand par stand",
    "Le Garde-Manger (Emmanuel Renaut)": "boutique fermée pour la saison depuis le 1er novembre",
    "Aux Produits Savoyards (Coop des Arves)": "même décideur que Coop des Arves – siège (une adresse par réseau)",
    "Fromagerie-Coopérative Vallée des Arves (Valloire)": "même décideur que Coop des Arves – siège",
}


cibles = []
for f in sorted(SRC.glob("cibles-*.csv")):
    cibles += list(csv.DictReader(open(f, encoding="utf-8"), delimiter=";"))
emails = []
for f in sorted(SRC.glob("emails-*.csv")):
    emails += list(csv.DictReader(open(f, encoding="utf-8"), delimiter=";"))


def cible_de(e):
    mots = norme(e["nom"]) or norme(e["nom"] + " x")
    best, score = None, 0
    for c in cibles:
        s = len(mots & norme(c["Nom"])) * 2 + len(norme(e["commune"]) & norme(c["Commune"]))
        if s > score:
            best, score = c, s
    return best if score >= 2 else None


importer, verifier, suivi, vus = [], [], [], set()
for e in emails:
    c = cible_de(e) or {}
    typ = type_commerce(c.get("Type", "") + " " + e["nom"])
    pan = "oui" if str(c.get("Panettone déjà en vente ?", "")).lower().startswith(("oui", "probable")) else "non"
    dept = c.get("Dépt", "")
    mail = (e["email"] or "").strip().lower()
    origine = ("Adresse publiée par votre établissement ou par un annuaire professionnel public "
               f"(source consultée : {e['source_url']})")
    suivi.append({"priorite": c.get("Priorité", ""), "dept": dept, "zone": c.get("Zone", ""),
                  "nom": e["nom"], "commune": e["commune"], "type": typ, "panettone_en_rayon": pan,
                  "email": mail, "statut_email": e["statut"], "telephone": c.get("Téléphone", ""),
                  "source_url": e["source_url"], "note": e["note"],
                  "mail1": "", "mail2": "", "mail3": "", "mail4": "", "appel": "", "reponse": "",
                  "mise_en_relation": "", "commande": "", "refus": "", "notes_suivi": ""})
    if e["nom"] in ECARTES:
        suivi[-1]["notes_suivi"] = "écarté de l'import : " + ECARTES[e["nom"]]
        continue
    if not mail:
        continue
    ligne = {"EMAIL": mail, "ORGANISME": e["nom"], "TYPE_COMMERCE": typ, "COMMUNE": e["commune"],
             "PANETTONE_EN_RAYON": pan, "ORIGINE_CONTACT": origine, "STATUT_CAMPAGNE": "a_contacter"}
    if e["statut"] == "trouve" and mail not in vus:
        vus.add(mail)
        importer.append(ligne)
    elif e["statut"] == "a_verifier":
        verifier.append({**ligne, "motif": e["note"]})

for nom, lignes in [("a-importer-brevo.csv", importer), ("a-verifier.csv", verifier), ("suivi.csv", suivi)]:
    with open(ICI / nom, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(lignes[0].keys()), delimiter=";")
        w.writeheader()
        w.writerows(lignes)
    print(nom, len(lignes))
