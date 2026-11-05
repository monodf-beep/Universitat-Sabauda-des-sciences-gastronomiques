"""Écrit les quatre modèles HTML de la séquence Brevo (textes : ../mails.md).

Usage : python3 outils/fabrique_modeles.py   (depuis campagne/panettoni-vilma/)
Les cases [ENTRE CROCHETS] restent visibles en jaune : un modèle qui en garde une ne s'active pas.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "modeles"

# Couleurs reprises du catalogue « Panettoni d'autore 2025 » de Vilma & Elio : rouge corail des titres,
# rouge profond, vert sapin, sur fond blanc. (Les noms des variables datent de la première charte.)
CREME, BORDEAUX, OR, TEXTE, GRIS = "#f7f4f1", "#b3140f", "#127a3a", "#1f1b18", "#5f5a55"
CORAIL = "#d94448"
SAPIN, DORE = "#2f4a2c", "#e0b85a"  # vert des pages de fond du catalogue, or des rubans
# Images : hébergées dans la galerie Brevo (voir IMAGES.md) ; sinon, copie publique du dépôt GitHub.
IMG = {
    "bandeau": "https://raw.githubusercontent.com/monodf-beep/Universitat-Sabauda-des-sciences-gastronomiques/claude/jolly-dirac-zip2dz/campagne/panettoni-vilma/visuels/bandeau-mail.jpg",
    "cuboli": "https://raw.githubusercontent.com/monodf-beep/Universitat-Sabauda-des-sciences-gastronomiques/claude/jolly-dirac-zip2dz/campagne/panettoni-vilma/visuels/produits/cuboli.png",
    "persi-pien": "https://raw.githubusercontent.com/monodf-beep/Universitat-Sabauda-des-sciences-gastronomiques/claude/jolly-dirac-zip2dz/campagne/panettoni-vilma/visuels/produits/persi-pien.png",
    "pumate": "https://raw.githubusercontent.com/monodf-beep/Universitat-Sabauda-des-sciences-gastronomiques/claude/jolly-dirac-zip2dz/campagne/panettoni-vilma/visuels/produits/pumate.png",
    "lien": "https://raw.githubusercontent.com/monodf-beep/Universitat-Sabauda-des-sciences-gastronomiques/claude/jolly-dirac-zip2dz/campagne/panettoni-vilma/visuels/lien-savoie-piemont.jpg",
    "monte-granero": "https://raw.githubusercontent.com/monodf-beep/Universitat-Sabauda-des-sciences-gastronomiques/claude/jolly-dirac-zip2dz/campagne/panettoni-vilma/visuels/produits/monte-granero.png",
}
import json, os
CATALOGUE = ("https://raw.githubusercontent.com/monodf-beep/Universitat-Sabauda-des-sciences-gastronomiques/"
             "claude/jolly-dirac-zip2dz/campagne/panettoni-vilma/catalogue/Vilma-Elio-Panettoni-d-autore.pdf")
_galerie = os.path.join(os.path.dirname(__file__), "images-brevo.json")
if os.path.exists(_galerie):
    IMG.update(json.load(open(_galerie, encoding="utf-8")))
F = "Georgia,'Times New Roman',serif"
S = "Arial,Helvetica,sans-serif"
P = f"margin:0 0 18px 0;font-family:{S};font-size:16px;line-height:1.65;color:{TEXTE};"
MAILTO = ("mailto:franck.monod@culturasabauda.eu"
          "?subject=Panettoni%20Vilma%20-%20tarifs%20revendeurs")
A_COMPLETER = "background:#fff3a3;color:#1f1b18;padding:0 3px;"

DATE_LIMITE = "mercredi 25 novembre"  # validée par Corinne le 05/11/2026 (« intorno al 25 novembre »)
SIEGE = "Maison des associations, 67 rue Saint-François-de-Sales, 73000 Chambéry"
PHOTO = f'<span style="{A_COMPLETER}">[PHOTO DES PANETTONI]</span>'


def p(t):
    return f'<p style="{P}">{t}</p>'


def page(titre, corps, pre="", fond=CREME):
    return f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{titre}</title>
<style>@media only screen and (max-width:620px){{.pad{{padding:22px 18px 24px 18px!important}}}}</style>
</head><body style="margin:0;padding:0;background-color:{fond};">
<div style="display:none;max-height:0;overflow:hidden;">{pre}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{fond};"><tr><td align="center" style="padding:28px 12px 36px 12px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;background-color:#ffffff;border:1px solid #e8e2da;">
{corps}
</table></td></tr></table></body></html>
"""


def entete():
    return (f'<tr><td style="padding:26px 36px 0 36px;font-family:{F};font-size:13px;letter-spacing:2px;'
            f'text-transform:uppercase;color:{CORAIL};">Universitât Sabauda'
            f'<span style="color:{GRIS};letter-spacing:1px;"> · des sciences gastronomiques</span></td></tr>'
            f'<tr><td style="padding:12px 36px 0 36px;"><div style="border-top:2px solid {OR};height:0;'
            f'line-height:0;font-size:0;">&nbsp;</div></td></tr>')


VIGNETTES = False  # le catalogue part en pièce jointe : pas de vignettes dans le mail (Franck, 04/11)


def bandeau():
    vignettes = [("cuboli", "Cubolì", "abricot"), ("persi-pien", "Persi Pien", "cacao, pêche, amaretti"),
                 ("pumate", "Pumaté", "pomme, cannelle"), ("monte-granero", "Monte Granero", "pandoro")]
    cases = "".join(
        f'<td width="25%" align="center" valign="top" style="padding:0 4px;font-family:{S};font-size:12px;'
        f'line-height:1.35;color:{GRIS};"><img src="{IMG[k]}" width="120" alt="{nom}" style="display:block;'
        f'width:100%;max-width:120px;height:auto;border:0;margin:0 auto 6px auto;">'
        f'<strong style="color:{CORAIL};font-family:{F};font-size:14px;">{nom}</strong><br>{sous}</td>'
        for k, nom, sous in vignettes)
    if not VIGNETTES:
        cases = ""
    image = (f'<tr><td style="padding:0;"><img src="{IMG["bandeau"]}" width="600" alt="Panettoni d\'autore, '
             f'Vilma &amp; Elio, Grand-Villars (Villar-Perosa, Piémont)" style="display:block;width:100%;max-width:600px;height:auto;border:0;">'
             f'</td></tr>')
    if not cases:
        return image
    return (image + f'<tr><td style="padding:6px 28px 4px 28px;"><table role="presentation" width="100%" '
            f'cellpadding="0" cellspacing="0" border="0"><tr>{cases}</tr></table></td></tr>')


def fleche(texte, lien, couleur=BORDEAUX):
    return (f'<div style="margin:6px 0 0 0;"><a href="{lien}" style="font-family:{S};font-size:15px;'
            f'font-weight:bold;color:{couleur};text-decoration:none;">&rarr;&nbsp;{texte}</a></div>')


def atouts():
    cases = [("Le Cubolì", "à l'abricot, sans fruits confits"), ("Sans lactose", "la nouveauté 2026"),
             ("Échantillons", "pour goûter avant de commander")]
    td = "".join(
        f'<td width="33%" valign="top" style="padding:12px 10px;border-top:3px solid {CORAIL};'
        f'font-family:{S};font-size:14px;line-height:1.4;color:{GRIS};">'
        f'<strong style="display:block;font-family:{F};font-size:17px;color:{BORDEAUX};margin-bottom:3px;">'
        f'{t}</strong>{d}</td>' for t, d in cases)
    return (f'<tr><td style="padding:4px 26px 8px 26px;"><table role="presentation" width="100%" '
            f'cellpadding="0" cellspacing="0" border="0"><tr>{td}</tr></table></td></tr>')


FREJUS = ("Le chantier du Fréjus a été dirigé par un ingénieur savoyard, Germain Sommeiller, né à Saint-Jeoire. La nuit de Noël 1870, après treize ans de travaux, les mineurs partis de Modane et de Bardonecchia se sont rejoints sous la montagne, à quelques centimètres près. Le tunnel a ouvert le 17 septembre 1871. On raconte que les Piémontais ont fêté la percée avec des panettoni : depuis, le panettone a aussi une histoire savoyarde.")


def lien_savoie_piemont():
    return (f'<tr><td style="padding:6px 0 0 0;"><img src="{IMG["lien"]}" width="600" alt="Savoie et '
            f'Piémont, reliés par le tunnel du Fréjus à Noël 1870 : une même histoire" '
            f'style="display:block;width:100%;max-width:600px;height:auto;border:0;"></td></tr>'
            f'<tr><td style="padding:10px 36px 6px 36px;font-family:{S};font-size:15px;line-height:1.6;'
            f'color:{GRIS};">'
            + FREJUS + "</td></tr>")


def encadre():
    return (f'<tr><td style="padding:10px 36px 6px 36px;"><table role="presentation" width="100%" '
            f'cellpadding="0" cellspacing="0" border="0" style="background-color:{SAPIN};border-radius:4px;"><tr>'
            f'<td style="padding:18px 22px;font-family:{S};font-size:15px;line-height:1.6;color:#ffffff;">'
            f"<strong>Intéressé ?</strong> Répondez à ce mail : nous vous envoyons les tarifs revendeurs et des "
            f"échantillons, et nous vous mettons en relation avec Vilma e Elio, qui prend la commande et livre. "
            f"Pour Noël, écrivez-nous avant le {DATE_LIMITE}."
            f'<div style="margin:10px 0 0 0;">{fleche("Demander les tarifs", MAILTO, DORE)}'
            f'{fleche("Voir le catalogue (PDF)", CATALOGUE, DORE)}</div></td></tr></table></td></tr>')


def pied_formel():
    return (f'<tr><td style="padding:22px 36px 26px 36px;background-color:{CREME};font-family:{S};'
            f'font-size:12px;line-height:1.55;color:{GRIS};">'
            f'<strong style="color:{BORDEAUX};">Universitât Sabauda des sciences gastronomiques</strong>, '
            f"association qui fait connaître la gastronomie sabaude, de la Savoie au Piémont.<br>"
            f'<a href="mailto:franck.monod@culturasabauda.eu" style="color:{BORDEAUX};">franck.monod@culturasabauda.eu</a>'
            f" · Siège : {SIEGE}<br><br>"
            "Origine de votre adresse : {{ contact.ORIGINE_CONTACT }}. Si vous ne souhaitez plus recevoir nos "
            "messages, répondez simplement « non merci ».<br>"
            f'<a href="{{{{ unsubscribe }}}}" style="color:{BORDEAUX};">Se désinscrire</a></td></tr>')


def signature_et_pied_court():
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:6px 0 16px 0;"><tr>'
            f'<td style="padding:0 0 0 12px;border-left:3px solid {OR};font-family:{S};font-size:13px;'
            f'line-height:1.55;color:{TEXTE};"><strong style="color:{BORDEAUX};font-size:15px;">Franck Monod</strong><br>'
            f"Président, Universitât Sabauda des sciences gastronomiques<br>"
            f'Tél. : 00 33 (0)6 31 19 42 49 · <a href="mailto:franck.monod@culturasabauda.eu" '
            f'style="color:{BORDEAUX};">franck.monod@culturasabauda.eu</a></td></tr></table>'
            f'<div style="border-top:1px solid #e8e2da;margin:24px 0 12px 0;height:0;line-height:0;font-size:0;">&nbsp;</div>'
            f'<p style="margin:0 0 8px 0;font-family:{S};font-size:12px;line-height:1.5;color:{GRIS};">'
            f"Universitât Sabauda des sciences gastronomiques · Siège : {SIEGE}.</p>"
            f'<p style="margin:0;font-family:{S};font-size:12px;line-height:1.5;color:{GRIS};">'
            "Origine de votre adresse : {{ contact.ORIGINE_CONTACT }}. Répondez « non merci » et je ne vous "
            f'écrirai plus.<br><a href="{{{{ unsubscribe }}}}" style="color:{BORDEAUX};">Se désinscrire</a></p>')


T = "contact.TYPE_COMMERCE"
a_cote = ('{% if ' + T + ' == "caviste" %}de vos vins'
          '{% elif ' + T + ' == "fromagerie" %}de vos fromages'
          '{% elif ' + T + ' == "bio" %}de vos produits bio'
          '{% else %}de votre épicerie{% endif %}')
rayon = ('{% if contact.PANETTONE_EN_RAYON == "oui" %}'
         "Vous proposez déjà des panettoni : ceux-ci peuvent compléter votre rayon avec des parfums que "
         "l'on trouve peu, artisanaux et piémontais."
         "{% else %}Pour les fêtes, c'est un cadeau gourmand qui change, à côté " + a_cote + ".{% endif %}")

m1 = page("PANETTONI · 1 présentation", entete() + bandeau()
          + f'<tr><td class="pad" style="padding:26px 36px 4px 36px;">'
          + p("Madame, Monsieur,")
          + p("L'<strong>Universitât Sabauda des sciences gastronomiques</strong> fait connaître la gastronomie "
              "sabaude, de la Savoie au Piémont. Pour le projet européen <strong>SavoiaExperience</strong> "
              "(Interreg ALCOTRA), nous menons la recherche gastronomique et préparons le repas de clôture avec "
              "des traiteurs partenaires de Savoie et du Piémont. Parmi eux, <strong>Vilma e Elio</strong>, "
              "maison artisanale de Grand-Villars (Villar-Perosa, Piémont), dont nous aimerions vous faire goûter les panettoni.")
          + "</td></tr>" + lien_savoie_piemont() + atouts()
          + f'<tr><td class="pad" style="padding:8px 36px 4px 36px;">' + p(rayon) + "</td></tr>" + encadre()
          + f'<tr><td class="pad" style="padding:20px 36px 24px 36px;">'
          + p("Nous vous prions d'agréer, Madame, Monsieur, nos salutations distinguées.")
          + f'<p style="margin:0;font-family:{F};font-size:16px;color:{BORDEAUX};">Universitât Sabauda des '
            f"sciences gastronomiques</p></td></tr>" + pied_formel(),
          pre="Les panettoni de Vilma e Elio : de la Savoie au Piémont, une même histoire", fond=SAPIN)

m2 = page("PANETTONI · 2 relance Franck",
          f'<tr><td class="pad" style="padding:28px 36px 30px 36px;">'
          + p("Bonjour,")
          + p("Je me permets de revenir vers vous au sujet des panettoni artisanaux de Vilma e Elio, "
              "à Grand-Villars (Villar-Perosa, Piémont), que nous vous avons présentés le 6 novembre, avec leur catalogue.")
          + p("Je sais que le temps manque en cette saison, et qu'un e-mail se perd vite : d'où ce petit rappel.")
          + p("Si cela vous intéresse, <strong>un mot en réponse me suffit</strong> : je vous envoie les tarifs "
              "revendeurs, Corinne, chez Vilma e Elio, peut vous faire goûter quelques échantillons, et je vous "
              "mets en relation avec elle. Si ce n'est pas pour "
              "vous, dites-le-moi aussi : j'arrête les relances.")
          + p("Bonne journée,<br>Franck") + signature_et_pied_court() + "</td></tr>")

m3 = page("PANETTONI · 3 date limite", bandeau()
          + f'<tr><td class="pad" style="padding:26px 36px 24px 36px;">'
          + p("Madame, Monsieur,")
          + p(f"Pour avoir les panettoni de Vilma e Elio en boutique avant les fêtes, il faut nous écrire "
              f"<strong>au plus tard le {DATE_LIMITE}</strong> : passé cette date, la livraison avant Noël "
              "n'est plus garantie.")
          + p("Pour rappel : panettoni artisanaux de Vilma e Elio, à Grand-Villars (Villar-Perosa, Piémont), traiteur partenaire "
              "de notre travail sur la gastronomie sabaude : onze recettes, dont le Cubolì à l'abricot, sans raisins "
              "ni fruits confits, et une version sans lactose.")
          + p(f'Leur catalogue : <a href="{CATALOGUE}" style="color:{BORDEAUX};font-weight:bold;">Panettoni '
              "d'autore (PDF, en italien)</a>. Répondez simplement à ce mail : nous vous envoyons les tarifs "
              "revendeurs, Vilma e Elio peut vous faire goûter quelques échantillons, et nous vous mettons en "
              "relation avec eux.")
          + f'<div style="margin:4px 0 22px 0;">{fleche("Demander les tarifs revendeurs", MAILTO)}</div>'
          + p("Nous vous prions d'agréer, Madame, Monsieur, nos salutations distinguées.")
          + f'<p style="margin:0;font-family:{F};font-size:16px;color:{BORDEAUX};">Universitât Sabauda des '
            f"sciences gastronomiques</p></td></tr>" + pied_formel(),
          pre="Pour une livraison avant Noël", fond=SAPIN)

m4 = page("PANETTONI · 4 dernier mail Franck",
          f'<tr><td class="pad" style="padding:28px 36px 30px 36px;">'
          + p("Bonjour,")
          + p("C'est mon dernier mail au sujet des panettoni de Vilma e Elio : aujourd'hui est le dernier "
              "jour conseillé pour une livraison avant les fêtes.")
          + p("Si l'idée vous plaît pour plus tard, répondez-moi simplement « plus tard » et je reviendrai "
              "vers vous le moment venu. Si ce n'est pas pour vous, répondez « non merci » : je ne vous "
              "écrirai plus.")
          + p("Belle fin d'année,<br>Franck") + signature_et_pied_court() + "</td></tr>")

OUT.mkdir(exist_ok=True)
for nom, html in [("1-presentation.html", m1), ("2-relance-franck.html", m2),
                  ("3-date-limite.html", m3), ("4-dernier-franck.html", m4)]:
    (OUT / nom).write_text(html, encoding="utf-8")
    print(nom, len(html))
