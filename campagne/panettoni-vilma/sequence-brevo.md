# Séquence de mails dans Brevo (compte Cultura Sabauda)

> Même méthode que la campagne *Diccionèro de fata* (dépôt `Enstitut`) : **rien ne s'active seul**.
> Les modèles sont créés **inactifs**, Franck envoie les tests, relit, puis active lui-même.
> Compte : Cultura Sabauda (franck.monod@culturasabauda.eu), offre gratuite : **300 envois par jour**.

## 1. Ce qui est déjà en place dans Brevo (créé le 04/11/2026 par le connecteur)

| Élément | Identifiant | État |
|---|---|---|
| Attributs de contact | `ORGANISME`, `COMMUNE`, `TYPE_COMMERCE`, `ORIGINE_CONTACT`, `PANETTONE_EN_RAYON`, `STATUT_CAMPAGNE` (texte) | créés |
| Dossier | #15 « Panettoni Vilma 2026 » | créé |
| Liste | #16 « Panettoni 2026 · Commerces Savoie et Haute-Savoie » | vide |
| Modèle mail 1 (formel) | #58 « PANETTONI · 1 présentation (formel) » | inactif, cases jaunes à lever |
| Modèle mail 2 (Franck) | #59 « PANETTONI · 2 relance Franck » | inactif |
| Modèle mail 3 (formel) | #60 « PANETTONI · 3 date limite (formel) » | inactif |
| Modèle mail 4 (Franck) | #61 « PANETTONI · 4 dernier mail Franck » | inactif |

Expéditeur de tous les modèles : franck.monod@culturasabauda.eu (déjà validé dans Brevo). Nom affiché :
« Universitât Sabauda » pour les mails 1 et 3, « Franck Monod » pour les mails 2 et 4. Réponse à :
franck.monod@culturasabauda.eu. Le HTML exact est dans `modeles/` (régénéré par `outils/fabrique_modeles.py`).

## 2. Avant d'activer (Franck)

1. **Lever les cases jaunes** dans `outils/fabrique_modeles.py`, régénérer, puis recopier le HTML dans
   les modèles #58 à #61 (ou demander au connecteur de le faire) :
   `[ADRESSE DU SIÈGE]`, `[INTÉRÊT DÉCLARÉ]`, `[DATE LIMITE]`, `[À VALIDER avec Chloé]`.
2. **Authentifier le domaine culturasabauda.eu** dans Brevo (Paramètres > Expéditeurs, domaines et IP
   dédiées > Domaines) : DKIM et DMARC à ajouter chez l'hébergeur du domaine. Aujourd'hui seul
   `franckmonod.eu` est déclaré, et pas authentifié. Sans cela, une partie des mails ira en indésirables.
3. **Envoyer un test** de chaque modèle vers une boîte **externe** (Gmail perso, pas culturasabauda.eu) :
   relire objet, nom d'expéditeur, liens, pied ; vérifier qu'il arrive en boîte de réception.
4. **Importer les contacts** dans la liste #16 depuis `listes/a-importer-brevo.csv` (séparateur `;`),
   **après l'activation du scénario** (voir 3), sans cocher « mettre à jour les contacts désinscrits ».

## 3. Le scénario (Automatisations > Créer un scénario > personnalisé), à construire à la main

L'API de Brevo ne permet pas de créer un scénario : il se monte dans l'interface (≈ 10 minutes).

- **Déclencheur** : « Contact ajouté à une liste » → liste #16.
- Étape 1 : Envoyer un e-mail → modèle **#58**.
- Attendre **6 jours**. Condition : si `STATUT_CAMPAGNE` est `repondu`, `interesse`, `plus_tard` ou `exclu` →
  **sortie du scénario**.
- Étape 2 : Envoyer → modèle **#59**. Attendre **4 jours**, même condition de sortie.
- Étape 3 : Envoyer → modèle **#60**. Attendre **6 jours**, même condition de sortie.
- Étape 4 : Envoyer → modèle **#61**. Attendre 3 jours, puis `STATUT_CAMPAGNE` = `a_appeler`.

**Ordre obligatoire** : Brevo ne fait entrer dans un scénario que les contacts ajoutés à la liste *après*
son activation. Donc : activer le scénario, **puis** importer la liste, le mardi 10 novembre au matin.
Les dates écrites dans les mails (10 novembre, [DATE LIMITE]) supposent ce lancement ; s'il glisse,
les corriger avant.

**Après une modification d'un modèle**, le scénario garde sa copie : dans l'étape, supprimer le message
puis « Ajouter un message » > à partir d'un modèle > rechoisir le modèle (relevé dans la campagne du
dictionnaire, 03/11/2026).

## 4. Pendant la campagne : les réponses arrivent dans Gmail, pas dans Brevo

Chaque réponse se reporte **le jour même** sur le contact dans Brevo, sinon la relance part quand même :

| Réponse du commerce | `STATUT_CAMPAGNE` | Ce que fait Franck |
|---|---|---|
| Intéressé | `interesse` | réponse type « mise en relation » (`mails.md`), Corinne en copie, fiche PDF jointe |
| « Plus tard » | `plus_tard` | noter la période dans `listes/suivi.csv` |
| « Non merci » | `exclu` + liste de blocage Brevo | ne plus jamais écrire ni appeler ; ne pas supprimer la ligne |
| Autre réponse | `repondu` | répondre à la main |

Le suivi complet (mails, appels, mise en relation, commande) se tient dans `listes/suivi.csv`.

## 5. Volume

300 envois par jour en offre gratuite : la liste tient en une journée. Si elle dépasse 300 contacts, l'importer
en deux fois, à un jour d'écart.
