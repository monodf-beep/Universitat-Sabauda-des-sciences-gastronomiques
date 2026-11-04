# Campagne *Panettoni Vilma* — commerces de Savoie et de Haute-Savoie (novembre 2026)

L'Universitât Sabauda des sciences gastronomiques présente aux commerces de Savoie et de Haute-Savoie
les panettoni artisanaux de **Vilma & Elio** (Piémont), dans le cadre de son travail de
recherche gastronomique pour le projet SavoiaExperience. Les commerces intéressés répondent à Franck,
qui les **met en relation** avec Corinne : c'est Vilma & Elio qui vend et livre.

Méthode reprise de la campagne *Diccionèro de fata* de l'Institut de la Langue Savoyarde
(dépôt `Enstitut`, branche `claude/fervent-cannon-2uylbz`, `campagne/diccionero-de-fata/`).

## Les pièces

| Pièce | Fichier | État |
|---|---|---|
| Textes des 4 mails, pieds, réponse « mise en relation » | `mails.md` | rédigés ; cases à lever |
| Modèles HTML des mails (couleurs du catalogue Vilma) | `modeles/*.html`, fabriqués par `outils/fabrique_modeles.py` | dans Brevo #58 à #61, **inactifs** |
| Montage dans Brevo (compte Cultura Sabauda) | `sequence-brevo.md` | attributs, dossier #15, liste #16 et modèles créés ; scénario à monter à la main |
| Fiche revendeur, 1 page A4 | `fiche-revendeur/fiche-revendeur.pdf` (source : `fiche-revendeur/source/`) | gamme remplie d'après le catalogue 2025 ; prix et conditions à fournir par Corinne |
| Visuels | `visuels/bandeau-mail.jpg`, `visuels/produits/*.jpg` (11 recettes) | découpés dans le catalogue « Panettoni d'autore 2025 » ; droits à confirmer avec Corinne |
| Catalogue Vilma & Elio (lien dans les mails 1 et 3) | `catalogue/Vilma-Elio-Panettoni-d-autore.pdf` | version allégée (2,5 Mo) du PDF « Panettoni d'autore 2025 » |
| Listes (à importer, à vérifier, suivi) | `listes/` — **hors du dépôt** (`.gitignore`) | 95 adresses à importer, 14 à vérifier, 165 enseignes au suivi ; fabriquées par `outils/listes.py`. Le dépôt est public et ces fichiers contiennent des adresses nominatives : ils ne se publient pas. |

## Ce qui bloque l'envoi (cases jaunes)

1. `[DATE LIMITE]` de commande pour Noël, à fixer avec Corinne (proposé : jeudi 26 novembre).
2. Prix revendeur 2026, minimum, livraison, DLUO, allergènes : à demander à Corinne pour la fiche.
3. Domaine culturasabauda.eu à authentifier dans Brevo (DKIM, DMARC), sinon risque d'indésirables.

Siège de l'association (pied des mails et de la fiche) : Maison des associations, 67 rue Saint-François-de-Sales,
73000 Chambéry. La phrase d'« intérêt déclaré » et la case « à valider avec Chloé » ont été retirées (Franck, 04/11/2026).

## Pièce jointe ou lien ?

Le catalogue n'est **pas en pièce jointe** mais en **lien** dans les mails 1 et 3 : Brevo a refusé l'adresse du PDF
comme pièce jointe (04/11/2026), et un premier mail sans pièce jointe arrive plus souvent en boîte de réception.
Le lien pointe vers la copie du PDF sur cette branche GitHub (dépôt public) : ne pas supprimer la branche
pendant la campagne, ou déplacer le PDF (site de l'association, Drive partagé) et changer `CATALOGUE` dans
`outils/fabrique_modeles.py`.

## Refaire les fichiers

```
python3 outils/fabrique_modeles.py          # modèles HTML des mails
python3 outils/listes.py                    # listes (hors dépôt)
node <script pdf> fiche-revendeur/source/fiche-revendeur.html fiche-revendeur/fiche-revendeur.pdf
```
La fiche se refait avec Playwright (« imprimer en PDF », fonds compris) ; ses polices (Fraunces, Great Vibes,
Lato) viennent de Google Fonts : il faut le réseau. Vérifier ensuite avec `pdffonts` qu'elles sont embarquées.
