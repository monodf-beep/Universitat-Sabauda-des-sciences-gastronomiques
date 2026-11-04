# Campagne *Panettoni Vilma* — commerces de Savoie et de Haute-Savoie (novembre 2026)

L'Universitât Sabauda des sciences gastronomiques présente aux commerces de Savoie et de Haute-Savoie
les panettoni artisanaux de **Vilma & Elio** (Pinerolo, Piémont), dans le cadre de son travail de
recherche gastronomique pour le projet SavoiaExperience. Les commerces intéressés répondent à Franck,
qui les **met en relation** avec Corinne : c'est Vilma & Elio qui vend et livre.

Méthode reprise de la campagne *Diccionèro de fata* de l'Institut de la Langue Savoyarde
(dépôt `Enstitut`, branche `claude/fervent-cannon-2uylbz`, `campagne/diccionero-de-fata/`).

## Les pièces

| Pièce | Fichier | État |
|---|---|---|
| Textes des 4 mails, pieds, script d'appel, réponse « mise en relation » | `mails.md` | rédigés ; cases à lever |
| Modèles HTML des mails (couleurs du catalogue Vilma) | `modeles/*.html`, fabriqués par `outils/fabrique_modeles.py` | dans Brevo #58 à #61, **inactifs** |
| Montage dans Brevo (compte Cultura Sabauda) | `sequence-brevo.md` | attributs, dossier #15, liste #16 et modèles créés ; scénario à monter à la main |
| Fiche revendeur, 1 page A4 | `fiche-revendeur/fiche-revendeur.pdf` (source : `fiche-revendeur/source/`) | gamme remplie d'après le catalogue 2025 ; prix et conditions à fournir par Corinne |
| Visuels | `visuels/bandeau-mail.jpg`, `visuels/produits/*.jpg` (11 recettes) | découpés dans le catalogue « Panettoni d'autore 2025 » ; droits à confirmer avec Corinne |
| Liste des commerces | `listes/` | adresses e-mail en cours de recherche |

## Ce qui bloque l'envoi (cases jaunes)

1. `[ADRESSE DU SIÈGE]` de l'association (obligatoire dans un mail de prospection).
2. `[À VALIDER avec Chloé]` : citer SavoiaExperience / Interreg ALCOTRA dans une prospection pour une entreprise
   privée, et confirmer que Vilma & Elio est bien retenu pour le repas du 3 décembre.
3. `[DATE LIMITE]` de commande pour Noël, à fixer avec Corinne (proposé : jeudi 26 novembre).
4. `[INTÉRÊT DÉCLARÉ]` : garder la phrase si l'association est rémunérée sur les ventes, sinon la retirer.
5. Prix revendeur 2026, minimum, livraison, DLUO, allergènes : à demander à Corinne pour la fiche.
6. Domaine culturasabauda.eu à authentifier dans Brevo (DKIM, DMARC), sinon risque d'indésirables.

## Refaire les fichiers

```
python3 outils/fabrique_modeles.py          # modèles HTML des mails
node <script pdf> fiche-revendeur/source/fiche-revendeur.html fiche-revendeur/fiche-revendeur.pdf
```
La fiche se refait avec Playwright (« imprimer en PDF », fonds compris) ; ses polices (Fraunces, Great Vibes,
Lato) viennent de Google Fonts : il faut le réseau. Vérifier ensuite avec `pdffonts` qu'elles sont embarquées.
