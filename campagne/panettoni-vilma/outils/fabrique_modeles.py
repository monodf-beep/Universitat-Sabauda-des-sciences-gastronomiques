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
# Images : hébergées dans la galerie Brevo (voir IMAGES.md) ; sinon, copie publique du dépôt GitHub.
IMG = {
    "bandeau": "https://raw.githubusercontent.com/monodf-beep/Universitat-Sabauda-des-sciences-gastronomiques/claude/jolly-dirac-zip2dz/campagne/panettoni-vilma/visuels/bandeau-mail.jpg",
    "cuboli": "https://raw.githubusercontent.com/monodf-beep/Universitat-Sabauda-des-sciences-gastronomiques/claude/jolly-dirac-zip2dz/campagne/panettoni-vilma/visuels/produits/cuboli.png",
    "persi-pien": "https://raw.githubusercontent.com/monodf-beep/Universitat-Sabauda-des-sciences-gastronomiques/claude/jolly-dirac-zip2dz/campagne/panettoni-vilma/visuels/produits/persi-pien.png",
    "pumate": "https://raw.githubusercontent.com/monodf-beep/Universitat-Sabauda-des-sciences-gastronomiques/claude/jolly-dirac-zip2dz/campagne/panettoni-vilma/visuels/produits/pumate.png",
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
A_COMPLETER = "background:#fff3a3;padding:0 3px;"

DATE_LIMITE = f'<span style="{A_COMPLETER}">[DATE LIMITE]</span>'
SIEGE = "Maison des associations, 67 rue Saint-François-de-Sales, 73000 Chambéry"
PHOTO = f'<span style="{A_COMPLETER}">[PHOTO DES PANETTONI]</span>'


def p(t):
    return f'<p style="{P}">{t}</p>'


def page(titre, corps, pre=""):
    return f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{titre}</title>
<style>@media only screen and (max-width:620px){{.pad{{padding:22px 18px 24px 18px!important}}}}</style>
</head><body style="margin:0;padding:0;background-color:{CREME};">
<div style="display:none;max-height:0;overflow:hidden;">{pre}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{CREME};"><tr><td align="center" style="padding:28px 12px 36px 12px;">
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
             f'Vilma &amp; Elio, Pinerolo" style="display:block;width:100%;max-width:600px;height:auto;border:0;">'
             f'</td></tr>')
    if not cases:
        return image
    return (image + f'<tr><td style="padding:6px 28px 4px 28px;"><table role="presentation" width="100%" '
            f'cellpadding="0" cellspacing="0" border="0"><tr>{cases}</tr></table></td></tr>')


def encadre():
    return (f'<tr><td style="padding:4px 36px 6px 36px;"><table role="presentation" width="100%" '
            f'cellpadding="0" cellspacing="0" border="0" style="border:1px solid {OR};"><tr>'
            f'<td style="padding:16px 20px;font-family:{S};font-size:15px;line-height:1.6;color:{TEXTE};">'
            f'<div style="font-family:{F};font-size:17px;color:{BORDEAUX};margin:0 0 8px 0;">Comment ça marche</div>'
            f"Si les panettoni vous intéressent, répondez simplement à ce mail : nous vous envoyons les tarifs "
            f"revendeurs et nous vous mettons en relation directe avec Vilma e Elio, qui prend la commande "
            f"et livre. Pour être livré avant les fêtes, mieux vaut nous écrire avant le {DATE_LIMITE}."
            f'<div style="margin:16px 0 2px 0;"><a href="{MAILTO}" style="display:inline-block;'
            f'background-color:{BORDEAUX};color:#ffffff;font-family:{S};font-size:15px;font-weight:bold;'
            f'text-decoration:none;padding:11px 20px;border-radius:3px;">Recevoir les tarifs revendeurs</a>'
            f'</div></td></tr></table></td></tr>')


def pied_formel():
    return (f'<tr><td style="padding:22px 36px 26px 36px;background-color:{CREME};font-family:{S};'
            f'font-size:12px;line-height:1.55;color:{GRIS};">'
            f'<strong style="color:{BORDEAUX};">Universitât Sabauda des sciences gastronomiques</strong> — '
            f"association qui fait connaître la gastronomie des deux versants des Alpes, entre Savoie et Piémont.<br>"
            f'<a href="mailto:franck.monod@culturasabauda.eu" style="color:{BORDEAUX};">franck.monod@culturasabauda.eu</a>'
            f" · Siège : {SIEGE}<br><br>"
            "Origine de votre adresse : {{ contact.ORIGINE_CONTACT }}. Si vous ne souhaitez plus recevoir nos "
            "messages, répondez simplement « non merci ».<br>"
            f'<a href="{{{{ unsubscribe }}}}" style="color:{BORDEAUX};">Se désinscrire</a></td></tr>')


def signature_et_pied_court():
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:6px 0 16px 0;"><tr>'
            f'<td style="padding:0 0 0 12px;border-left:3px solid {OR};font-family:{S};font-size:13px;'
            f'line-height:1.55;color:{TEXTE};"><strong style="color:{BORDEAUX};font-size:15px;">Franck Monod</strong><br>'
            f"Président — Universitât Sabauda des sciences gastronomiques<br>"
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
          + p("Franck Monod a fondé l'Universitât Sabauda des sciences gastronomiques, une association qui "
              "fait connaître la gastronomie des deux versants des Alpes, entre Savoie et Piémont.")
          + p(f"Nous participons au projet européen <strong>SavoiaExperience</strong> (Interreg "
              "ALCOTRA), consacré à la valorisation culturelle et touristique de l'espace sabaudo, entre Piémont "
              "et Savoie. Nous y sommes chargés de la recherche gastronomique et du repas de clôture du projet, "
              "préparé avec des traiteurs partenaires des deux côtés des Alpes, dont <strong>Vilma e Elio</strong>, "
              "maison artisanale de Pinerolo. C'est par eux que nous avons découvert leurs panettoni, et nous "
              "aimerions vous les faire connaître.")
          + p("Entre le panettone et la Savoie, il y a une vieille histoire. À Modane, on raconte que les ouvriers "
              "du tunnel du Fréjus, percé de 1857 à 1871, aimaient un pain sucré aux raisins, l'ancêtre du pain de "
              "Modane, cousin du panettone. Au début des travaux, la Savoie faisait encore partie du royaume de "
              "Piémont-Sardaigne.")
          + p(f'Leur catalogue est ici : <a href="{CATALOGUE}" style="color:{BORDEAUX};font-weight:bold;">'
              "voir le catalogue Panettoni d'autore (PDF, en italien)</a>. Deux mots seulement : "
              "leur panettone le plus aimé, le <strong>Cubolì</strong>, est à l'abricot, sans raisins secs ni "
              "fruits confits ; et, nouveauté 2026, ils en font une version <strong>sans lactose</strong>.")
          + p(rayon) + "</td></tr>" + encadre()
          + f'<tr><td class="pad" style="padding:20px 36px 24px 36px;">'
          + p("Nous vous prions d'agréer, Madame, Monsieur, nos salutations distinguées.")
          + f'<p style="margin:0;font-family:{F};font-size:16px;color:{BORDEAUX};">Universitât Sabauda des '
            f"sciences gastronomiques</p></td></tr>" + pied_formel(),
          pre="Une maison artisanale de Pinerolo, partenaire de notre projet entre Savoie et Piémont")

m2 = page("PANETTONI · 2 relance Franck",
          f'<tr><td class="pad" style="padding:28px 36px 30px 36px;">'
          + p("Bonjour,")
          + p("Je me permets de revenir vers vous au sujet des panettoni artisanaux de Vilma e Elio, à "
              "Pinerolo, que nous vous avons présentés le 10 novembre, avec leur catalogue.")
          + p("Je sais que le temps manque en cette saison, et qu'un e-mail se perd vite : d'où ce petit rappel.")
          + p("Si cela vous intéresse, <strong>un mot en réponse me suffit</strong> : je vous envoie les tarifs "
              "revendeurs, et je vous mets en relation avec Corinne, chez Vilma e Elio. Si ce n'est pas pour "
              "vous, dites-le-moi aussi : j'arrête les relances.")
          + p("Bonne journée,<br>Franck") + signature_et_pied_court() + "</td></tr>")

m3 = page("PANETTONI · 3 date limite", entete()
          + f'<tr><td class="pad" style="padding:26px 36px 24px 36px;">'
          + p("Madame, Monsieur,")
          + p(f"Pour avoir les panettoni de Vilma e Elio en boutique avant les fêtes, il faut nous écrire "
              f"<strong>au plus tard le {DATE_LIMITE}</strong> : passé cette date, la livraison avant Noël "
              "n'est plus garantie.")
          + p("Pour rappel : panettoni artisanaux de Vilma e Elio, à Pinerolo (Piémont), traiteur partenaire "
              "de notre travail sur la gastronomie sabaude : onze recettes, dont le Cubolì à l'abricot, sans raisins "
              "ni fruits confits, et une version sans lactose.")
          + p(f'Leur catalogue : <a href="{CATALOGUE}" style="color:{BORDEAUX};font-weight:bold;">Panettoni '
              "d'autore (PDF, en italien)</a>. Répondez simplement à ce mail : nous vous envoyons les tarifs "
              "revendeurs et nous vous mettons en relation avec Vilma e Elio.")
          + f'<p style="margin:22px 0 22px 0;"><a href="{MAILTO}" style="display:inline-block;'
            f'background-color:{BORDEAUX};color:#ffffff;font-family:{S};font-size:15px;font-weight:bold;'
            f'text-decoration:none;padding:11px 20px;border-radius:3px;">Recevoir les tarifs revendeurs</a></p>'
          + p("Nous vous prions d'agréer, Madame, Monsieur, nos salutations distinguées.")
          + f'<p style="margin:0;font-family:{F};font-size:16px;color:{BORDEAUX};">Universitât Sabauda des '
            f"sciences gastronomiques</p></td></tr>" + pied_formel(),
          pre="Pour une livraison avant Noël")

m4 = page("PANETTONI · 4 dernier mail Franck",
          f'<tr><td class="pad" style="padding:28px 36px 30px 36px;">'
          + p("Bonjour,")
          + p("C'est mon dernier mail au sujet des panettoni de Vilma e Elio : aujourd'hui est le dernier "
              "jour conseillé pour une livraison avant les fêtes.")
          + p("Si l'idée vous plaît pour plus tard, répondez-moi simplement « plus tard » et je reviendrai "
              "vers vous le moment venu. Faute de réponse, je vous appellerai peut-être une minute ; "
              "répondez « non merci » et je ne le ferai pas.")
          + p("Belle fin d'année,<br>Franck") + signature_et_pied_court() + "</td></tr>")

OUT.mkdir(exist_ok=True)
for nom, html in [("1-presentation.html", m1), ("2-relance-franck.html", m2),
                  ("3-date-limite.html", m3), ("4-dernier-franck.html", m4)]:
    (OUT / nom).write_text(html, encoding="utf-8")
    print(nom, len(html))
