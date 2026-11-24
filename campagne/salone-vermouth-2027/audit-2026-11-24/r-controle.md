# Contrôle qualité : la cohérence des faits d'une vue à l'autre

## 1. Ce qui va

- Les six échéances des jalons sont identiques dans L'objectif, Chantier 1, Chantier 2 et le Tableau de bord : J1 mai 2027, J2 fin 2027, J3 printemps 2027, J4 printemps 2027, J5 fin 2027, J6 mai 2027, le Suédois fin 2027.
- Le devis tombe juste partout : 12 demi-journées × 400 € = 4 800 €, 800 € par mois, de décembre à mai, dans Budget, Décisions, Qui fait quoi et Accompagnement. Le voyage à Turin (4 × 400 € = 1 600 €) est juste lui aussi.
- Les conventions ont les mêmes dates partout : Institut en décembre, avant le Salone ; Universitât rédigée en mars et signée en avril (Qui fait quoi, Calendrier, Décisions, Chantier 2).
- Les 70 attributs `data-view` (dont 46 dans le texte) pointent tous vers une vue qui existe. Les dates clés sont les mêmes d'une vue à l'autre : 3 décembre, 14 octobre, 22 janvier, du 29 janvier au 1er février 2027.
- Les calculs du Constat sont justes : 1,2 € et 0,8 € par habitant, ≈ 1,5 M€, 4,6 %, 36 M€, × 5 entre 2018 et 2024.

## 2. Ce qui ne va pas

### P1 · bloquant

1. **pilotage (base `tasks`, graines `db/tasks/t12.json`)** : la tâche « Décider de la participation au village du vermouth à Rimini » (Dolin, 15 janvier 2027) est encore dans le Suivi, alors que Rimini doit sortir du plan. Correction : supprimer `tasks/t12` de la base en ligne (ArtifactData, action delete) et le fichier de graine.

2. **pilotage (`t17`)** : « Choisir le projet de fond : Comoz, musée ou route européenne » reprend une ancienne liste. Le musée n'est plus un projet, et la route européenne est une action du chantier 1, pas un projet. Remplacer par : « Choisir le premier projet (jalon 6) : lieu à Chambéry, Comoz en Savoie, bars à vermouth, nouveaux vermouths ; s'il dépasse Dolin, le confier à l'Universitât », avec Dolin comme responsable et une échéance au 30 avril 2027.

3. **pilotage, comparé à turin, chambery et roles** : le Suivi compte 18 tâches pour environ 38 actions. Le chantier 2 en est presque absent : seules les bouteilles du 3 décembre y sont. Il manque aussi la décision 5 (les contenus pour la route européenne) et les deux conventions. Tâches à ajouter, avec les responsables et les mois des chantiers :
   - Décembre : la convention avec l'Institut ; la fiche Dolin pour la route européenne ; la liste des établissements de Savoie ; le point sur Comoz et le bar d'Annecy.
   - Janvier : faire valider les mots du stand par l'Institut ; l'offre aux bars et restaurants savoyards ; les mots de savoyard sur la carte ; le Suédois en digestif ; les expériences ouvertes au public ; Dolin sur les cartes du Fuorisalone.
   - Fin janvier : la rencontre avec Chazalettes.
   - Février : le questionnaire de notoriété ; le Salone raconté en Savoie ; le suivi des acheteurs (de février à mai).
   - Février à mars : les cafés historiques.
   - Mars : la comparaison des pistes ; la convention cadre rédigée.
   - Printemps : le récit pour la plateforme ; le document historique présenté aux élus ; la cuvée sabauda proposée ; les cavistes.
   - Avril : la convention cadre signée.
   - Mai : l'annonce du projet.

   Dans l'autre sens, trois tâches du Suivi n'existent dans aucun chantier : « Proposer à Laura Carello deux ou trois touches en piémontais » (t07), « Bilan du Salone » (t15) et « Séance de lancement » (t08). Il faut soit les rattacher à une action d'un chantier, soit les ajouter au Calendrier.

4. **tableau, comparé à objectifs** : l'indicateur principal ne mesure pas l'objectif. L'objectif porte sur le chiffre d'affaires de Dolin en Savoie. Or la ligne « Chiffre d'affaires du vermouth en Savoie » mesure le marché : la ligne « Ventes de Dolin en Savoie (pour vérifier que la part de Dolin grandit aussi) » le confirme. Remplacer « Chiffre d'affaires du vermouth en Savoie » par « Chiffre d'affaires de Dolin en Savoie (vermouth, Comoz, le Suédois) ». Remplacer ensuite « Ventes de Dolin en Savoie (pour vérifier que la part de Dolin grandit aussi) » par « Le marché du vermouth en Savoie (pour vérifier qu'il grandit) ».

5. **questions, comparé à budget** : le lien « À confirmer » du tarif mène à « Le tarif à la demi-journée · Franck · 400 € proposés ; 450 à 500 € restent raisonnables. ». C'est une note de négociation interne, visible par le client. La question « L'émetteur du devis : en son nom propre ou au nom de l'Universitât Sabauda » est interne elle aussi. Si l'Universitât émet le devis, la mention « TVA non applicable, article 293 B du CGI » et la règle « Une action, un seul cadre » ne tiennent plus. Correction : trancher l'émetteur avant la présentation et retirer ces deux lignes. Si la question du tarif doit rester, la remplacer par « Le tarif à la demi-journée · Franck · 400 €, à confirmer à la signature du devis. ».

6. **moyens et accompagnement, comparé à projets, roles et turin** : selon ces deux vues, l'Universitât porterait « la route européenne » et « la renaissance des vermouths savoyards ». Or la vue Projets dit que la route « n'[est] pas [un] projet, mais [une action] des chantiers ». Le lieu à Chambéry et Comoz, qui font cette renaissance, sont « Porté par Dolin ». Et les actions de la route vont à Dolin et à Franck Monod. Les rencontres portent aussi deux noms selon la vue.
   - Moyens : remplacer « Elle porte les projets qui dépassent Dolin : la renaissance des vermouths savoyards, les bars à vermouth, les nouveaux producteurs, le vermouth à la table savoyarde, les rencontres Chambéry–Turin, la route européenne. » par « Elle porte les projets qui dépassent Dolin : les bars à vermouth, les nouveaux vermouths savoyards, le vermouth à la table savoyarde, les rencontres du vermouth sabaudo. »
   - Accompagnement : remplacer « Elle porte les projets qui dépassent Dolin : la renaissance des vermouths savoyards, le vermouth à la table savoyarde, les rencontres Chambéry–Turin, la route européenne. » par la même phrase.

7. **vision** : la phrase « Chaque axe se traduit en objectifs mesurables d'ici mai 2027. » contredit L'objectif, qui fixe un seul objectif pour 2030 et des jalons qui vont jusqu'à fin 2027. Remplacer « De la vision aux objectifs » par « De la vision à l'objectif ». Remplacer la phrase par « Les deux axes se traduisent en un objectif, les ventes de Dolin d'ici 2030, et en six jalons, de mai à fin 2027. ». Remplacer le lien « Les objectifs → » par « L'objectif → ».

### P2 · important

8. **objectifs, comparé à turin** : le jalon 1 dit passer « Par » les cafés historiques et la cuvée, alors que ces deux actions sont rangées sous le jalon 2 dans le Chantier 1. Dans la carte et dans le détail du jalon 1, remplacer « le Salone : exposant et table ronde ; les cafés historiques de Turin ; une cuvée avec une maison turinoise » par « le Salone : exposant et table ronde ; les bars du Fuorisalone ; la presse italienne ». Dans le « Par » du jalon 2, ajouter « les cafés historiques de Turin ; une cuvée sabauda ».

9. **turin** : l'action « Le lieu du vermouth à Chambéry, étape ouverte au public » (Dolin, Franck Monod, 2028-29) se trouve sous le jalon 3, dont l'échéance est le printemps 2027. De plus, ce lieu est une piste du jalon 6, dans le chantier 2. Supprimer cette action du Chantier 1. Le lieu est déjà dans « Comparer les pistes » (Chantier 2) et dans l'étape 2028-29.

10. **objectifs (trois étapes), comparé aux jalons 5 et 6** : l'étape « 2028-29 Dolin servi en Savoie » reprend l'intitulé du jalon 5 « Être servi en Savoie », dont l'échéance est fin 2027. L'étape 2030 affiche « Bars à vermouth » et « Comoz en Savoie », deux pistes que le jalon 6 peut lancer dès mai 2027 ; en plus, Questions demande encore « faut-il le faire connaître en Savoie ? ».
    - Remplacer « 2028-29 Dolin servi en Savoie » par « 2028-29 Dolin installé en Savoie ».
    - Remplacer « Les bars, les restaurants, les cavistes ; un lieu à Chambéry ; les premières ventes en Italie. » par « Au-delà des premiers établissements : les bars, les restaurants, les cavistes de toute la Savoie ; un lieu à Chambéry ; les premières ventes en Italie. »
    - Remplacer les puces de 2030 par « D'autres bars à vermouth », « Nouveaux vermouths » et « Comoz en Savoie (à décider) ».

11. **vision (axe 1)** : la phrase « En 2030 · Dolin cité et servi à Turin ; Chambéry, étape de la route » reprend mot pour mot les cibles des jalons 1 (mai 2027) et 3 (printemps 2027). L'axe 1 serait donc atteint trois ans avant 2030. Remplacer par « Dolin vendu en Italie et reconnu à Turin comme une maison de la même histoire ; Chambéry, étape reconnue de la route européenne ».

12. **tableau** : quatre lignes se répètent ou se contredisent.
    - « Part des bars et restaurants dans les ventes » apparaît deux fois, avec une échéance en 2030 dans le bloc de l'objectif et fin 2027 sous le jalon 5. Indiquer « [__] % · fin 2027 » sous le jalon 5 et « [__] % · 2030 » dans le bloc de l'objectif, ou supprimer l'une des deux lignes.
    - « Ventes du Suédois » apparaît deux fois, dans le bloc de l'objectif et en « Bonus ». Supprimer la ligne « Bonus ».
    - Dans les deux tableaux de jalons, remplacer « Bonus » par « Le Suédois ». L'Objectif le présente comme un levier « sur les deux chantiers » ; il n'a donc pas sa place seulement dans le chantier 2.
    - « Ventes en Italie | Aucune connue | Premiers clients | 2028 » : remplacer « 2028 » par « 2028-29 », l'année de l'étape dans L'objectif.

13. **tableau, objectifs et marque** : les jalons sont appelés tantôt « jalons », tantôt « objectifs ».
    - Remplacer « Des indicateurs par objectif » par « Des indicateurs par jalon ».
    - Dans les deux tableaux des chantiers, remplacer l'en-tête de colonne « Objectif » par « Jalon ».
    - Remplacer « Les lignes en couleur sont les indicateurs principaux de chaque objectif. » par « Les lignes en couleur sont les indicateurs principaux de chaque jalon. ».
    - Remplacer « Chaque objectif est SMART » par « Chaque jalon est SMART ».
    - Remplacer « Il sert tous les objectifs » par « Il sert tous les jalons ».
    - Remplacer « Le socle des objectifs » (Marque) par « Le socle des jalons ».

14. **chambery** : l'action « Choisir 20 à 30 établissements : bars, restaurants, hôtels de station » avance un chiffre, alors que la cible du jalon 5 reste « [__] établissements ». Remplacer par « Choisir les premiers établissements ([__]) : bars, restaurants, hôtels de station ».

15. **chambery, comparé à calendrier** : la même assistance est écrite « devant 150 acteurs » d'un côté et « (environ 150 personnes) » de l'autre, sans source et sans entrée dans les chiffres non vérifiés. Remplacer « devant 150 acteurs » par « devant environ 150 acteurs du territoire ». Dans Questions, sous « Chiffres non vérifiés », ajouter « Environ 150 convives au déjeuner SavoiaExperience · Département de la Savoie · Chiffre annoncé par l'organisateur. ».

16. **references** : on y lit « le colloque Iter Vitis (23 juin 2026) », alors que le Constat, Questions et la ligne suivante de Références donnent le 3 juin 2026. Remplacer « (23 juin 2026) » par « (3 juin 2026) ».

17. **turin et references** : il reste des éléments obsolètes. Dans le Chantier 1, supprimer la ligne « Vinitaly, espace Xcellent Spirits | Vérone, 11-14 avril 2027 | … ». Dans Références, supprimer « Vinitaly, l'espace Xcellent Spirits », « Beverfood, Cocchi à Vinitaly 2025 » et « Beer&Food Attraction 2027, chiffres et dates ». Ce dernier est une source sur Rimini ; Rimini ne doit rester que dans la question posée à Laura Carello.

18. **terrain** : la phrase « Dolin part sur la première formule. Laura Carello propose de l'intégrer quand même au circuit du Fuorisalone, parce que c'est un producteur non italien (réunion du 13/11/2026). » contredit le tableau juste au-dessus : la formule Partner di prodotto comprend déjà « cartes du Fuorisalone ». Le Lexique dit la même chose (« une présence dans le circuit »). Remplacer par « Dolin part sur la première formule, qui comprend les cartes du Fuorisalone ; Laura Carello propose d'y ajouter [à préciser avec elle], parce que c'est un producteur non italien (réunion du 13/11/2026). ».

19. **projets et roles, comparé à objectifs, chambery et turin** : le Suédois est traité comme un « projet de Dolin », chiffré « au projet ». Mais toutes ses actions figurent déjà dans les chantiers, donc dans le devis : le poste au Salone, le digestif dès janvier, le 3 décembre. Il risque d'être payé deux fois, contre la règle « Rien n'est payé deux fois ». Supprimer la fiche « Le Suédois » de la vue Projets. Dans Qui fait quoi, remplacer « Un lieu à Chambéry, Comoz, le Suédois, la cuvée sabauda » par « Un lieu à Chambéry, Comoz, la cuvée sabauda ».

20. **calendrier et decisions** : le calendrier s'arrête en mai 2027, alors que les jalons 2 et 5 et le Suédois ont leur échéance fin 2027, et que « Prendre la parole aux rencontres d'Iter Vitis » est prévu en 2027.
    - Remplacer « De la fin novembre 2026 à mai 2027. Ensuite, les étapes 2028-29 et 2030. » par « De la fin novembre 2026 à fin 2027. Ensuite, les étapes 2028-29 et 2030. ».
    - Ajouter la ligne « Juin – décembre 2027 | Un partenariat signé avec une autre maison · [__] établissements qui servent Dolin et le Suédois · prise de parole aux rencontres d'Iter Vitis | 1 et 2 ».
    - Le voyage d'acculturation à Turin (option, « en 2027, pendant le Salone ») doit se décider en décembre, mais n'apparaît dans aucune décision ni ligne du calendrier. Dans Décisions, sous « Ensuite », ajouter « Choisir l'option du voyage à Turin pendant le Salone, avant fin décembre. ».

21. **pilotage (`dolin.js`)** : le Suivi repose encore sur l'ancienne structure.
    - Les responsables (`OWNERS=['Franck','Dolin','Laura','Les deux']`) ignorent l'Institut et l'Universitât, et « Les deux » est ambigu. Remplacer par `['Franck Monod','Dolin','Institut','Universitât','Laura Carello']` et migrer les tâches existantes : « Franck » → « Franck Monod », « Laura » → « Laura Carello ». Pour « Les deux », choisir un seul responsable par tâche.
    - Les étapes (`PHASES`) portent d'anciens noms : « Janvier · Turin », « Février – mars · Le bilan », « Avril – mai · Le fond ». Garder les clés et changer les libellés en « Décembre 2026 », « Janvier 2027 · le Salone », « Février – mars 2027 », « Avril – mai 2027 », puis ajouter `['suite','Juin – décembre 2027']`.
    - Le titre « Qui fait quoi, et quand » reprend le nom de la vue roles. Le remplacer par « Les actions, et où elles en sont ».

22. **strategie et moyens** : deux outils pointent vers des vues qui ne les expliquent pas. « Marketing local » mène au Chantier 2, alors que la notion est définie dans Marketing (« Marketing local · Adapter un message à une zone »). « Cycle de vie client » mène au Tableau de bord, où l'expression n'apparaît nulle part. Correction : faire pointer `data-view="chambery"` vers `marketing`, et `data-view="tableau"` vers `lexique`. Ajouter au Lexique deux entrées : « Marketing local · Adapter un message à une zone, avec les références de ceux qui y vivent. » et « Cycle de vie client · Les étapes d'un client : notoriété, intérêt, achat, fidélité, recommandation. ».

### P3 · finition

23. **Axes et chantiers mélangés, libellés inégaux** :
    - Projets : remplacer « est une piste pour l'axe 2 » par « est une piste pour le chantier 2 ».
    - Objectifs (le Suédois) : remplacer « Il sert les deux axes : » par « Il sert les deux chantiers : ».
    - Accompagnement : remplacer « La vision et ses deux axes, les objectifs » par « La vision, l'objectif et ses jalons ».
    - Vision : remplacer la surtitre « Vision et objectifs · La vision » par « Vision et objectif · La vision », comme dans le menu.
    - Stratégie : remplacer « l'Universitât Sabauda pour les projets collectifs » par « l'Universitât Sabauda pour les projets qui dépassent Dolin ».

24. **Questions à compléter** : ajouter dans « Pour Dolin » la ligne « L'espace d'exposition · Dolin · Annoncé pour 2022 : existe-t-il ? ». Il est cité « à vérifier » dans le Constat et dans Projets, mais absent de la liste. Ajouter dans « Pour Franck Monod » la ligne « Les panels · Franck · Un extrait Circana ou NielsenIQ et le détail IWSR pour la France. », demandés dans le Constat. Dans la question sur la date de la table ronde, remplacer « Évoquée pour un lundi en début de Fuorisalone, qui démarre le 22 janvier. » par « Évoquée pour le lundi 25 janvier 2027, en début de Fuorisalone. » : le 22 janvier 2027 tombe un vendredi. Harmoniser ensuite « Début du Fuorisalone » (Communication) et « Fin janvier » (Chantier 1, Calendrier) en « Le 25 janvier (à confirmer) ».

25. **Points isolés** :
    - Lexique : supprimer l'entrée « Piola », un mot qui n'apparaît nulle part dans le plan.
    - Chantier 1 : remplacer « Le Salone 2026, au Palazzo Carignano. » par « Le Salone 2026, au Museo Nazionale del Risorgimento (Palazzo Carignano). », comme dans le Terrain.
    - « Torino Cocktail Festival » (Chantier 1) contre « Torino Cocktail Week 2026 » (Références) : garder un seul nom.
    - Diagnostic : le lien « Le Salone, les acteurs, le calendrier » promet un calendrier que le Terrain n'a plus. Remplacer par « Le Salone, les formules, les acteurs ».
    - Diagnostic : « un petit marché, qui ne grandit pas » n'a pas de source. Remplacer par « un petit marché ».
    - Constat : le même « 56 % » désigne la grande distribution chez Dolin (Bref Eco) et le hors domicile en Italie (Circana). Vérifier le premier chiffre, qui ressemble à une erreur de copie.
    - Chantier 1 : l'action « Les 270 ans de Cinzano : raconter l'histoire commune » repose sur un chiffre « À vérifier » et met une autre marque en avant. La conditionner : « Si l'anniversaire est confirmé : … ».
    - Chantiers 1 et 2 : le texte « Les actions de chaque jalon, le calendrier, les décisions. Ces pages » n'a pas de liens. Ajouter des liens vers `calendrier`, `decisions` et `pilotage`, trois vues que seuls le menu et la pagination atteignent.
