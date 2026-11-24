# Audit éditorial du plan Dolin

Relecture : ton, longueur, titres, terminologie, vocabulaire, typographie, restes d'anciennes versions. Tous les textes « actuel » sont copiés de `dolin-body.html` : on peut les coller tels quels dans un chercher-remplacer. Sauf mention contraire, chaque texte n'apparaît qu'une fois dans le fichier.

## 1. Ce qui va

- La structure décidée se lit bien d'une vue à l'autre : vision en deux axes, objectif unique, deux chantiers, six jalons, trois moyens. Le fil « Vision 2030 · Chambéry, à nouveau ville du vermouth » ouvre (accueil) et ferme (décisions) le plan.
- Le vocabulaire imposé est respecté : « l'espace sabaudo », « les États de Savoie », « le savoyard ». On ne trouve ni « frontière », ni « transfrontalier », ni « ainsi », ni « prestations », ni « patois », ni « francoprovençal ».
- La typographie est saine : guillemets « » partout, espace devant chaque « : ; ? ! », aucun tiret cadratin dans les phrases (seulement dans les cellules vides des tableaux), aucune majuscule continue (le `text-transform:uppercase` de vil.css est neutralisé par dolin-extra.css).
- Les chiffres inconnus restent bien en [__], et les sources sont citées à côté de chaque chiffre.
- Le ton des vues tactiques (chantiers, décisions, calendrier) est le bon : des actions, un responsable, une date, sans avis.

## 2. Ce qui ne va pas : liste priorisée

### P1 : à corriger avant la relecture de demain

1. **questions** : une note interne est visible par le client : « 400 € proposés ; 450 à 500 € restent raisonnables ». De plus, le bouton « À confirmer » du tarif, dans la vue budget, renvoie précisément vers cette note. Correction : supprimer la ligne (texte exact en B, vue questions). Faire de même pour « L'émetteur du devis » : c'est à trancher avant l'envoi, pas une question pour Dolin.
2. **vision** : le lien vers la vue suivante reprend l'ancienne structure : « Chaque axe se traduit en objectifs mesurables d'ici mai 2027 ». Or l'objectif est unique, à l'horizon 2030. Correction en B (vision).
3. **tableau** : le titre « Des indicateurs par objectif », la colonne « Objectif » numérotée de 1 à 6 et la note « indicateurs principaux de chaque objectif » désignent en réalité les jalons. Correction : employer « jalon » (B, tableau).
4. **objectifs, accompagnement, lexique** : trois mots du client sont à remplacer. « Un levier » apparaît deux fois (« leviers » est banni). « Prestataire » a la même racine que « prestations ». « Les territoires alpins » est très proche d'« espace alpin ». Corrections en B.
5. **marque** : l'étiquette « Recommandée » sur « Vermouth sabaudo » est un avis de l'agence, juste sous la phrase « aucune n'est encore validée ». Les mentions « Moins personnel à Dolin » et « Plus long, plutôt pour… » sont aussi des jugements. Correction : des étiquettes descriptives et des faits (B, marque), et retirer la classe `rec` qui met la piste en avant.

### P2 : important

6. **Le mot « axe » est encore employé à la place de « chantier »** dans les vues stratégie, objectifs, projets et accompagnement. Par exemple : « Les publics des deux axes », « Il sert les deux axes », « une piste pour l'axe 2 ». Corrections en B.
7. **Le mot « objectifs » est encore au pluriel** alors que l'objectif est unique : « Vision et objectifs » (sur-titre de la vision), « Il sert tous les objectifs », « Chaque objectif est SMART », « Le socle des objectifs », « La vision et ses deux axes, les objectifs ». Corrections en B.
8. **Le rôle de l'Universitât Sabauda est décrit de quatre façons** (moyens, accompagnement, qui fait quoi, projets). Dans les moyens et l'accompagnement, elle porterait même « la route européenne ». Or la vue projets dit le contraire : la Route des vermouths est une action du chantier 1, portée par Dolin. Correction : une seule liste partout, « les bars à vermouth, les nouveaux vermouths savoyards, le vermouth à la table savoyarde, les rencontres du vermouth sabaudo », et une seule appellation : « l'Universitât Sabauda », le nom complet restant réservé au lexique et aux cartes de labels. Même chose pour « les rencontres Chambéry–Turin » : le nom est « les rencontres du vermouth sabaudo ».
9. **La Route des vermouths porte quatre noms** : « la Route des vermouths », « la route des vermouths », « la route du vermouth », « la route européenne » (une quinzaine de fois). Règle proposée : « la Route des vermouths » dans les titres, les listes, les tableaux et à la première mention dans chaque vue ; ensuite « la route ». Les remplacements sont donnés en B.
10. **Le place-based marketing a quatre définitions** (infobulle de la stratégie, outils, introduction de la vue marketing, lexique). Correction : une seule, « Faire de la culture d'un territoire (sa langue, son histoire, sa table) la matière première de la marque ». La version courte dans les outils devient « La culture du territoire, matière première de la marque ».
11. **Les sur-titres ne suivent pas la même logique.** On trouve « La tactique » (alors que les autres sections n'ont pas d'article : « Stratégie », « Budget »), « Les moyens · 1 · Marketing », « Les outils · Le socle » (la vue est rangée sous Stratégie dans le menu) et « Budget » tout seul. La vue stratégie globale n'a pas de sur-titre du tout. Règle proposée : « Section · Vue ». Corrections en B.
12. **Les titres principaux (h1) mélangent les registres.** Marketing a pour titre « Faire vivre ». Communication et projets, eux, ont des titres descriptifs, alors que les verbes « faire savoir » et « faire grandir » existent déjà. Autres problèmes : « Qui fait quoi, et quand » (vue suivi) reprend le nom d'une autre vue ; « Un accompagnement régulier » (budget) redit la vue précédente ; « Identité de marque » répète le nom de la vue. Corrections en B.
13. **Le partage des rôles est écrit cinq fois, avec cinq formulations** (moyens, qui fait quoi, accompagnement, suivi, tableau des rôles) : « propose, challenge, ouvre les portes », puis « prépare », puis « forme » ; « décide et exécute », puis « décide et vend », puis « décide, exécute et valide ». Correction : une formule unique, « Franck Monod propose, challenge et ouvre les portes ; Dolin décide et exécute ». Retirer la carte « Les rôles » de la vue suivi, qui fait doublon avec la vue qui fait quoi.
14. **Doublons dans les vues moyens et accompagnement.** La carte « Le cap » des moyens répète le « Aujourd'hui / Demain » de la vue marque. Elle se contredit aussi : le place-based marketing y est présenté comme un cap, alors que la même vue le range parmi les outils. Enfin, « Le cap » désigne autre chose dans l'accompagnement (le pilier Stratégie). « Le fil rouge » et le bloc « Deux labels » sont répétés à l'identique dans les moyens et dans l'accompagnement. Correction : supprimer « Le cap » dans les moyens ; garder le fil rouge et les labels dans les moyens seulement, et les remplacer dans l'accompagnement par un lien.
15. **Le Suédois est traité comme un projet dans les vues projets et qui fait quoi** (carte « Le Suédois · Piste », « Projets de Dolin : … le Suédois »), alors que l'objectif en fait un atout des deux chantiers et que le brief réserve les projets aux projets structurants. Autre souci : il est dit trois fois « peu mis en avant », ce qui se lit comme un reproche fait au client. Correction : retirer la carte du Suédois des projets et remplacer « Peu mis en avant » par « À mesurer », comme dans le tableau de bord.
16. **Les mêmes indicateurs portent des noms différents** d'une vue à l'autre : « Ventes de vermouth en Savoie » (objectif), « Chiffre d'affaires du vermouth en Savoie » (tableau), « +[__] % de chiffre d'affaires en Savoie » (titre de l'objectif). Le tableau de bord contient aussi des doublons : les ventes du Suédois sont comptées deux fois, et la ligne s'appelle « Bonus ». Corrections en B.
17. **Une même action est rangée sous deux moyens différents.** Les mots en savoyard sur le stand ou sur la carte sont classés « Communication » dans les chantiers 1 et 2, mais « Marketing » dans qui fait quoi et dans la vue marketing (où ils font partie des pistes du place-based marketing). Correction : « Marketing » partout.
18. **Les encadrés de conclusion portent des intitulés disparates** : « Ce qu'on en tire » et « Ce qu'il faut retenir » pour la même fonction ; « Ce que dit le marketing », qui sonne comme un cours ; « Méthode » et « Règle d'arbitrage » sans article. Dans la vue chantier 1, « Le point d'attention » et « Le point de vigilance » se suivent. Corrections en B.
19. **Paragraphes trop longs** : « Ce qu'on en tire » (diagnostic, 60 mots), « Ce que dit le marketing » (vision, 85 mots, qui redit en plus le bloc « La stratégie du leader » juste au-dessus), l'introduction de la vue marketing (une phrase de 50 mots), l'introduction des moyens, le calcul du marché savoyard (constat), l'Universitât dans les moyens, l'introduction de l'accompagnement. Versions courtes en B.
20. **turin** : « Le Consorzio boude aussi le Salone, qu'il juge trop ouvert » est un jugement familier, en contradiction avec la règle « Rester neutre » de la vue communication. Par ailleurs, le Consorzio est appelé tantôt « le Consorzio », tantôt « le consortium turinois ». Correction : un fait neutre (B), et « le Consorzio » pour l'institution, « consortium » ne servant que de nom commun.
21. **Faits incohérents entre les vues.** Le colloque Iter Vitis est daté du 3 juin dans le constat et les références, mais du 23 juin dans une autre ligne des références. Le salon de Turin s'appelle « Torino Cocktail Festival » dans le chantier 1 et « Torino Cocktail Week » dans les références. Le déjeuner SavoiaExperience a lieu « devant 150 acteurs » dans le chantier 2, mais réunit « environ 150 personnes » dans le calendrier ; il s'appelle « déjeuner SavoiaExperience » ou « déjeuner de clôture SavoiaExperience » selon les vues. Correction : vérifier les deux premiers points, et adopter « le déjeuner de clôture SavoiaExperience (environ 150 personnes) ».
22. **chambery** : « Choisir 20 à 30 établissements » est le seul chiffre de cible qui ne soit pas en [__], alors que le jalon 5 vise « [__] établissements ». S'il n'a pas été validé avec Pierre-Olivier Rousseaux, le remplacer par [__].

### P3 : finition

23. Les personnes ne sont pas nommées de façon uniforme : on trouve « Pierre-Olivier » (vues marketing et communication) et « Franck » (vue questions, quatre fois). Correction : le nom complet partout.
24. Notation : « [à fixer] » (dans les conventions de qui fait quoi) se confond avec la convention [__]. Correction : écrire « (à fixer) » ; les crochets restent réservés aux chiffres à fixer.
25. **Lexique et références.** Le lexique définit « Piola », qui n'est employé nulle part, mais pas « brindisi », qui est employé. Il manque les mots de la structure (axe, chantier, jalon, moyen), et « Savôya », imposé par le brief, n'apparaît nulle part dans le plan. Dans les références, il faut supprimer la ligne Spherical Insights, qui contient un commentaire « (non fiable…) », et la source Beer&Food Attraction : Rimini ne doit figurer qu'en question à Laura Carello. Ajouts et suppressions en B.

## B. Corrections de texte, vue par vue

### 00 · nav
- Actuel : `<p class="ngrp" title="Qui fait quoi, et quand ?">4 · La tactique</p>`
  Proposé : `<p class="ngrp" title="Qui fait quoi, et quand ?">4 · Tactique</p>`

### 02 · diagnostic
- Double espace avant les deux-points.
  Actuel : `quand Turin compte 41 à 45 maisons  : un petit marché`
  Proposé : `quand Turin compte 41 à 45 maisons : un petit marché`
- Comoz est cité deux fois dans les forces : supprimer la ligne suivante (la ligne « Comoz relancé » reste).
  Actuel : `<li>Un patrimoine qui raconte : le vermouth de Chambéry, la marque Comoz</li>`
  Proposé : (supprimer)
- Ce point des menaces était rédigé comme une action.
  Actuel : `<li>Les tensions entre le Salone et le Consorzio de Turin : rester neutre</li>`
  Proposé : `<li>Les tensions entre le Salone et le Consorzio</li>`
- Version plus courte de la conclusion (60 mots ramenés à 35).
  Actuel : `S'appuyer sur ce que personne d'autre n'a, l'histoire commune de Chambéry et Turin ; se servir du Salone et de la route européenne pour renouer avec l'espace sabaudo du vermouth ; et faire grandir le marché savoyard plutôt que d'y rester seul : être servi dans les bars et restaurants, et aider d'autres projets à naître.`
  Proposé : `L'histoire commune de Chambéry et Turin, que personne d'autre n'a. Le Salone et la Route des vermouths pour renouer avec l'espace sabaudo ; les bars, les restaurants et de nouveaux projets pour faire grandir le marché savoyard.`

### 03 · constat
- Actuel : `<h2>Ce qu'il faut mesurer d'abord</h2>`
  Proposé : `<h2>À mesurer d'abord</h2>`
- Version plus courte du calcul du marché savoyard (dans un accordéon, 75 mots ramenés à 50).
  Actuel : `Ce calcul a deux limites : la moyenne nationale efface les écarts entre régions, et la Savoie reçoit chaque année des millions de touristes que le nombre d'habitants ne compte pas. Il dit pourtant l'essentiel : environ 1,5 M€ par an, quand Dolin réalise 18,6 M€. Tel qu'il est, le marché savoyard ne peut pas porter la vision ; il faut le faire grandir. Le vrai chiffre se mesure avec les ventes de Dolin par département et un extrait des panels Circana ou NielsenIQ.`
  Proposé : `Deux limites : la moyenne nationale efface les écarts entre régions, et ne compte pas les touristes. L'ordre de grandeur suffit : environ 1,5 M€ par an, quand Dolin réalise 18,6 M€. Le marché savoyard est à faire grandir. Le vrai chiffre viendra des ventes de Dolin par département et des panels Circana ou NielsenIQ.`

### 04 · terrain
- Actuel : `<p class="lead">Ce qu'il faut savoir du Salone del Vermouth 2027 et des acteurs du vermouth à Turin.</p>`
  Proposé : `<p class="lead">Le Salone del Vermouth 2027 et les acteurs du vermouth à Turin.</p>`
- Actuel : `Associés au Fuorisalone et à la route du vermouth`
  Proposé : `Associés au Fuorisalone et à la Route des vermouths`
- Même intitulé de conclusion que dans le diagnostic.
  Actuel : `<b>Ce qu'il faut retenir</b>`
  Proposé : `<b>Ce qu'on en tire</b>`
- Actuel : `et ne pas s'arrêter au consortium turinois.`
  Proposé : `et ne pas s'arrêter au Consorzio.`

### 05 · vision
- Actuel : `<p class="ey">Vision et objectifs · La vision</p>`
  Proposé : `<p class="ey">Vision et objectif · La vision</p>`
- « Les outils » désigne ailleurs le place-based marketing, le marketing local et le cycle de vie client. Remplacement à faire sur les 2 occurrences.
  Actuel : `<dt>Les outils</dt>`
  Proposé : `<dt>Avec</dt>`
- Actuel : `Retrouver cette place : à Turin d'abord, puis sur la route européenne.`
  Proposé : `Retrouver cette place : à Turin d'abord, puis sur la Route des vermouths.`
- Actuel : `Le Salone et la route européenne servent aussi le marché savoyard.`
  Proposé : `Le Salone et la Route des vermouths servent aussi le marché savoyard.`
- Version plus courte de l'encadré théorique (85 mots ramenés à 45), sans redire le bloc « La stratégie du leader » placé juste au-dessus.
  Actuel : `<b>Ce que dit le marketing</b><span>C'est la stratégie classique du leader : développer la demande globale plutôt que se battre pour des parts de marché, parce que c'est le leader qui profite le plus d'un marché qui grandit (Philip Kotler, <i>Marketing Management</i>). En Savoie, le leader, c'est Dolin. On parle aussi de coopétition : coopérer avec ses concurrents pour agrandir le marché, puis s'y faire concurrence (Adam Brandenburger et Barry Nalebuff, 1996). À Turin, les maisons se font concurrence, mais défendent ensemble un nom et un récit.</span>`
  Proposé : `<b>Les références</b><span>La stratégie du leader (Philip Kotler, <i>Marketing Management</i>) et la coopétition : coopérer avec ses concurrents pour agrandir le marché, puis s'y faire concurrence (Adam Brandenburger et Barry Nalebuff, 1996). C'est ce que font les maisons de Turin autour d'un nom et d'un récit.</span>`
- Lien vers la vue suivante (P1).
  Actuel : `<b>De la vision aux objectifs</b><span>Chaque axe se traduit en objectifs mesurables d'ici mai 2027. <button type="button" class="link" data-view="objectifs">Les objectifs →</button></span>`
  Proposé : `<b>De la vision à l'objectif</b><span>Les deux axes deviennent un objectif, faire grandir les ventes de Dolin, et deux chantiers aux jalons datés. <button type="button" class="link" data-view="objectifs">L'objectif →</button></span>`

### 06 · objectifs
- Introduction : elle redisait celle de la vision.
  Actuel : `La vision donne la direction ; l'objectif, c'est le chiffre d'affaires. Trois étapes, et les jalons des deux chantiers.`
  Proposé : `Un objectif, trois étapes jusqu'en 2030, six jalons pour les deux chantiers.`
- Actuel : `<dt>Ventes de vermouth en Savoie</dt>`
  Proposé : `<dt>Chiffre d'affaires de Dolin en Savoie</dt>`
- Le Suédois, « peu mis en avant » : trois occurrences, à remplacer une par une.
  Actuel : `<dt>Le Suédois</dt><dd><span class="o0">Peu mis en avant</span>`
  Proposé : `<dt>Le Suédois</dt><dd><span class="o0">À mesurer</span>`
  Actuel : `<div class="obr"><span class="o0">Peu mis en avant</span>`
  Proposé : `<div class="obr"><span class="o0">À mesurer</span>`
  Actuel : `<dt>Départ</dt><dd>Peu mis en avant</dd>`
  Proposé : `<dt>Départ</dt><dd>À mesurer</dd>`
- Mot banni (P1).
  Actuel : `<p class="suk">Un levier sur les deux chantiers</p>`
  Proposé : `<p class="suk">Un atout sur les deux chantiers</p>`
  Actuel : `<h2>Un levier · Le Suédois</h2>`
  Proposé : `<h2>Un atout · Le Suédois</h2>`
- Actuel : `<p class="sul">Un amer de Chambéry, à 30 %, peu mis en avant. Or l'amaro est une habitude italienne, et le digestif une habitude savoyarde.</p>`
  Proposé : `<p class="sul">Un amer de Chambéry, à 30 % vol. L'amaro est une habitude italienne, le digestif une habitude savoyarde.</p>`
- Détail du Suédois : il redisait le bandeau du haut et parlait d'« axes ».
  Actuel : `Dolin fait un amer, le Suédois (30 % vol. ; gentiane, rhubarbe, myrrhe). Il sert les deux axes : l'amaro fait partie des habitudes italiennes, et il a sa place à la fin des repas en Savoie.`
  Proposé : `Gentiane, rhubarbe, myrrhe : le Suédois sert les deux chantiers, en amaro à Turin, en digestif en Savoie.`
- Actuel : `Il sert tous les objectifs :`
  Proposé : `Il sert les deux chantiers :`
- Actuel : `Chaque objectif est <abbr`
  Proposé : `Chaque jalon est <abbr`

### 07 · stratégie
- Il n'y a pas de sur-titre. À ajouter en tête de la maison, avant `<div class="hroof">` : `<p class="ey">Stratégie · La stratégie globale</p>`.
- Actuel : `l'Universitât Sabauda pour les projets collectifs.`
  Proposé : `l'Universitât Sabauda pour les projets qui dépassent Dolin.`
- Actuel : `<span class="meta">Les publics des deux axes</span>`
  Proposé : `<span class="meta">Les publics des deux chantiers</span>`
- Actuel : `1 : axe 1, l'espace sabaudo · 2 : axe 2, le marché savoyard`
  Proposé : `1 : chantier 1, Turin et l'Europe · 2 : chantier 2, Chambéry et la Savoie`
- Les trois moyens, alignés sur les mêmes formules que la vue moyens.
  Actuel : `<span>Concevoir les expériences : le stand, les bars, un lieu à Chambéry</span>`
  Proposé : `<span>Les expériences : le stand, les bars, un lieu à Chambéry</span>`
  Actuel : `<span>Faire connaître la maison, en français et en italien</span>`
  Proposé : `<span>Les messages, les publics, les canaux, en français et en italien</span>`
  Actuel : `<span>Faire grandir le marché, avec d'autres maisons et des bars</span>`
  Proposé : `<span>Développer le marché, avec d'autres maisons, des bars, des producteurs</span>`
- Définition unique du place-based marketing (même texte dans les vues stratégie et moyens, 2 occurrences).
  Actuel : `<span>Faire de la culture du territoire la matière des offres</span>`
  Proposé : `<span>La culture du territoire, matière première de la marque</span>`

### 08 · moyens
- Actuel : `Ils s'appuient sur trois outils (place-based marketing, marketing local, cycle de vie client), sur l'identité de marque et sur deux labels.`
  Proposé : `Avec trois outils, un socle et deux labels.`
- « Le cap » fait doublon avec la vue marque et contredit la liste des outils : supprimer l'encadré entier.
  Actuel : `<div class="thread"><span class="tl">Le cap</span><b>D'une identité de géographie à une identité de culture</b><span>Aujourd'hui, Dolin est « un vermouth français » ; demain, le vermouth sabaudo. Le place-based marketing n'est pas un moyen de plus : c'est ce cap, qui traverse les trois moyens.</span></div>`
  Proposé : (supprimer)
- Actuel : `Faire vivre, à travers Dolin, la culture de la Savoie : sa langue, son histoire, sa table. Elle passe par le marketing, par la communication, et par des projets culturels.`
  Proposé : `La langue, l'histoire et la table de la Savoie, portées par Dolin dans les trois moyens.`
- Ton : « et rien de plus » sonnait sec pour un label de Franck Monod.
  Actuel : `Il valide la graphie des mots en savoyard. C'est une partie du place-based marketing, et rien de plus.`
  Proposé : `Il valide la graphie des mots en savoyard, pour le place-based marketing. Son rôle s'arrête là.`
- Universitât : la liste unique, sans la route.
  Actuel : `Elle porte les projets qui dépassent Dolin : la renaissance des vermouths savoyards, les bars à vermouth, les nouveaux producteurs, le vermouth à la table savoyarde, les rencontres Chambéry–Turin, la route européenne. Une structure neutre peut réunir d'autres maisons ; un projet porté par Dolin seul aurait du mal à le faire.`
  Proposé : `Elle porte les projets qui dépassent Dolin : les bars à vermouth, les nouveaux vermouths savoyards, le vermouth à la table savoyarde, les rencontres du vermouth sabaudo. Structure neutre, elle réunit d'autres maisons, des bars, des chefs et des collectivités.`
- Formule de référence pour le partage des rôles.
  Actuel : `<span class="tl">Méthode</span><b>Tout se construit avec Dolin</b><span>Franck Monod propose, challenge et ouvre les portes ; Pierre-Olivier Rousseaux et ses équipes décident et exécutent.</span>`
  Proposé : `<span class="tl">Le partage des rôles</span><b>Tout se construit avec Dolin</b><span>Franck Monod propose, challenge et ouvre les portes ; Dolin décide et exécute.</span>`

### 09 · marketing
- Actuel : `<p class="ey">Les moyens · 1 · Marketing</p>`
  Proposé : `<p class="ey">Stratégie · Moyen 1 · Marketing</p>`
- Version plus courte de l'introduction, avec la définition unique.
  Actuel : `<p>Transformer l'identité en offres et en expériences, à Turin, sur la route européenne et en Savoie, avec la méthode du place-based marketing : faire de la langue, de l'histoire et des symboles du territoire la matière première de la marque, et véhiculer la culture des Savoyards.</p>`
  Proposé : `<p>Transformer l'identité en expériences, à Turin, sur la Route des vermouths et en Savoie, avec le place-based marketing : la culture du territoire, sa langue, son histoire, sa table, comme matière première de la marque.</p>`
- Actuel : `<li>Pierre-Olivier raconte la maison</li>`
  Proposé : `<li>Pierre-Olivier Rousseaux raconte la maison</li>`
- Actuel : `<b>La route des vermouths</b>`
  Proposé : `<b>La Route des vermouths</b>`
- Actuel : `<li>Dolin servi au déjeuner SavoiaExperience du 3 décembre</li>`
  Proposé : `<li>Dolin servi au déjeuner de clôture SavoiaExperience du 3 décembre</li>`
- Actuel : `<h2>La méthode a déjà marché</h2>`
  Proposé : `<h2>La méthode, déjà à l'œuvre</h2>`
- Actuel : `lié au vermouth ou au brindisi</span>`
  Proposé : `lié au vermouth ou au brindisi, le toast italien</span>`

### 10 · communication
- Sur-titre, titre et introduction : le verbe du moyen, comme pour le marketing.
  Actuel : `<p class="ey">Les moyens · 2 · Communication</p><h1>Trois messages, <em>deux langues</em></h1><p class="lead">Ce qu'on dit, à qui, par quels canaux, et les règles à tenir.</p>`
  Proposé : `<p class="ey">Stratégie · Moyen 2 · Communication</p><h1>Faire <em>savoir</em></h1><p class="lead">Trois messages, deux langues : ce qu'on dit, à qui, par quels canaux, et les règles à tenir.</p>`
- Actuel : `<td>Pierre-Olivier, Franck Monod</td>`
  Proposé : `<td>Pierre-Olivier Rousseaux, Franck Monod</td>`
- Toutes les règles commencent par un verbe à l'infinitif, sauf celle-ci.
  Actuel : `<b>Le récit avant le produit</b>`
  Proposé : `<b>Raconter avant de vendre</b>`
- Actuel : `les débats entre le Salone et le consortium turinois.`
  Proposé : `les débats entre le Salone et le Consorzio.`

### 11 · projets
- Actuel : `<p class="ey">Les moyens · 3 · Projets</p><h1>Des projets <em>structurants</em></h1><p class="lead">Des projets qui durent, qui réunissent d'autres acteurs et qui font grandir le marché. On en mène un ou deux à la fois ; chacun est chiffré à part.</p>`
  Proposé : `<p class="ey">Stratégie · Moyen 3 · Projets</p><h1>Faire <em>grandir</em></h1><p class="lead">Des projets structurants : ils durent, réunissent d'autres acteurs et font grandir le marché. Un ou deux à la fois, chacun chiffré à part.</p>`
- Ce texte redisait l'introduction (« chiffré à part ») et la vue moyens.
  Actuel : `Un projet au seul nom de Dolin tiendrait les autres à l'écart ; porté par une structure neutre, il les réunit, et le marché grandit pour tous. Les projets propres à Dolin restent chez Dolin ; chaque projet est chiffré à part.`
  Proposé : `Porté par une structure neutre, un projet réunit les autres maisons, et le marché grandit pour tous. Les projets propres à Dolin restent chez Dolin.`
- Actuel : `est une piste pour l'axe 2.`
  Proposé : `est une piste pour le chantier 2.`
- Le Suédois n'est pas un projet structurant : supprimer la carte entière.
  Actuel : `<div class="pj"><div class="pjh"><b>Le Suédois</b><span class="tag pis">Piste</span></div><p>Mettre en avant l'amer de Dolin : au digestif dans les restaurants de Savoie, dans les cocktails des bars à Turin, où l'amaro fait partie des habitudes.</p><small>Porté par Dolin · ventes et marchés à connaître</small></div>`
  Proposé : (supprimer)
- Actuel : `Porté par l'Universitât Sabauda des sciences gastronomiques, avec Dolin`
  Proposé : `Porté par l'Universitât Sabauda, avec Dolin`

### 12 · marque
- Actuel : `<p class="ey">Les outils · Le socle</p><h1>Identité <em>de marque</em></h1><p>Qui est Dolin, ce qu'il raconte, comment il parle, comment on le reconnaît. L'histoire en est un pilier, pas le tout.</p>`
  Proposé : `<p class="ey">Stratégie · Le socle</p><h1>Qui est Dolin, <em>et comment on le reconnaît</em></h1><p>Ce qu'il raconte, comment il parle. L'histoire en est un pilier, pas le tout.</p>`
- Actuel : `<b>Site, réseaux, presse, route européenne</b>`
  Proposé : `<b>Site, réseaux, presse, Route des vermouths</b>`
- Deux fois deux-points dans la même phrase.
  Actuel : `Les équipes de Dolin se l'approprient : c'est l'objet de l'acculturation : langue, culture, histoire, et le voyage à Turin.`
  Proposé : `Les équipes de Dolin se l'approprient par l'acculturation : langue, culture, histoire, et le voyage à Turin.`
- « La méthode » désigne déjà le place-based marketing dans la vue marketing.
  Actuel : `<h2>La méthode</h2><span class="meta">La même qu'au GFA`
  Proposé : `<h2>La démarche</h2><span class="meta">La même qu'au GFA`
- Avis de l'agence (P1) : étiquettes et remarques des pistes de signature.
  Actuel : `<div class="piste rec"><span class="role">Recommandée</span>`
  Proposé : `<div class="piste"><span class="role">Espace</span>`
  Actuel : `<p class="lim">Moins personnel à Dolin.</p>`
  Proposé : `<p class="lim">Ne nomme pas Dolin.</p>`
  Actuel : `<p class="lim">Plus long, plutôt pour un texte que pour une étiquette.</p>`
  Proposé : `<p class="lim">Six mots : pour un texte, plus que pour une étiquette.</p>`
- Cette ligne de la frise redit l'année 1856 et les vues projets et lexique.
  Actuel : `<div class="y5"><span>Aujourd'hui</span><div><b>Chambéry · Comoz</b><p>Dolin produit Comoz à Chambéry et le relance, pour l'instant aux États-Unis.</p></div></div>`
  Proposé : (supprimer)
- Actuel : `<span class="meta">Le socle des objectifs</span>`
  Proposé : `<span class="meta">Le socle des deux chantiers</span>`
- Actuel : `documents de la route du vermouth et des cafés historiques`
  Proposé : `documents de la Route des vermouths et des cafés historiques`

### 13 · turin
- Sur-titres : remplacement à faire sur les 5 occurrences (vues turin, chambery, roles, calendrier, decisions).
  Actuel : `<p class="ey">La tactique · `
  Proposé : `<p class="ey">Tactique · `
- Le moyen s'appelle « Projets » : remplacement à faire sur les 9 occurrences (légende et étiquettes des deux chantiers).
  Actuel : `<span class="mv p">Projet</span>`
  Proposé : `<span class="mv p">Projets</span>`
- Mots du stand : même moyen que dans la vue marketing et dans qui fait quoi.
  Actuel : `<span class="mv c">Communication</span><span class="atx">Un mot d'accueil en piémontais et en savoyard sur le stand</span>`
  Proposé : `<span class="mv m">Marketing</span><span class="atx">Un mot d'accueil en piémontais et en savoyard sur le stand</span>`
- Jugement familier, contraire à la règle « Rester neutre ».
  Actuel : `Le Consorzio boude aussi le Salone del Vermouth, qu'il juge trop ouvert : c'est justement ce qui laisse une place à Dolin.`
  Proposé : `Le Consorzio ne participe pas au Salone del Vermouth, ouvert aux vermouths d'ailleurs : c'est ce qui laisse une place à Dolin.`
- « Le point d'attention » suit de près « Le point de vigilance ».
  Actuel : `<b>Le point d'attention</b>`
  Proposé : `<b>À confirmer</b>`
- P3 : le bloc « La stratégie / La tactique · Ces pages », en tête de la vue, redit le tableau « De la stratégie à l'action » de la vue stratégie et n'existe pas dans le chantier 2. Il peut être supprimé.

### 14 · chambery
- Actuel : `Dolin et le Suédois au déjeuner SavoiaExperience, devant 150 acteurs`
  Proposé : `Dolin et le Suédois au déjeuner de clôture SavoiaExperience (environ 150 personnes)`
- Chiffre à confirmer avec Pierre-Olivier Rousseaux, sinon [__].
  Actuel : `Choisir 20 à 30 établissements : bars, restaurants, hôtels de station`
  Proposé : `Choisir [__] établissements : bars, restaurants, hôtels de station`
- Actuel : `<span class="mv c">Communication</span><span class="atx">Quelques mots de savoyard sur la carte, une fiche pour le personnel</span>`
  Proposé : `<span class="mv m">Marketing</span><span class="atx">Quelques mots de savoyard sur la carte, une fiche pour le personnel</span>`

### 15 · roles
- Ce texte contredisait le budget : l'acculturation est en option, et les projets sont chiffrés au projet.
  Actuel : `À chaque séance, deux demi-journées par mois : stratégie, marketing et place-based, communication, identité, charte, SEO, outils d'IA ; l'acculturation ; les projets propres à Dolin`
  Proposé : `Deux demi-journées par mois : stratégie, marketing et place-based marketing, et ce qui en découle (identité de marque, charte éditoriale, communication et SEO, outils d'IA) ; en option, l'acculturation ; au projet, les projets propres à Dolin`
- Actuel : `<td>Conçoit les offres et le place-based</td>`
  Proposé : `<td>Conçoit les offres, en place-based marketing</td>`
- Actuel : `<div class="note">Un lieu à Chambéry, Comoz, le Suédois, la cuvée sabauda</div>`
  Proposé : `<div class="note">Un lieu à Chambéry, Comoz, la cuvée sabauda</div>`
- Actuel : `Un an, renouvelable [à fixer]`
  Proposé : `Un an, renouvelable (à fixer)`
- Actuel : `Jusqu'en 2030 [à fixer]`
  Proposé : `Jusqu'en 2030 (à fixer)`

### 16 · calendrier
- Actuel : `fiche pour la route européenne`
  Proposé : `fiche pour la Route des vermouths`
- Actuel : `Fiche Dolin en ligne sur la route européenne`
  Proposé : `Fiche Dolin en ligne sur la Route des vermouths`

### 17 · decisions
- Actuel : `<b>Envoyer les contenus pour la route européenne</b>`
  Proposé : `<b>Envoyer les contenus pour la Route des vermouths</b>`
- Remplacement à faire sur les 2 occurrences (vues décisions et questions).
  Actuel : `pour le déjeuner SavoiaExperience.`
  Proposé : `pour le déjeuner de clôture SavoiaExperience.`

### 18 · accompagnement
- Mot proche du banni « prestations », définition par la négative et formule des rôles non unifiée.
  Actuel : `Un partenaire dans la durée, pas un prestataire qui exécute : il propose, challenge, ouvre les portes et forme ; Dolin décide. L'accompagnement tient sur trois piliers ; le reste en découle, ou sert d'outil.`
  Proposé : `Un partenaire dans la durée : Franck Monod propose, challenge, ouvre les portes et forme ; Dolin décide et exécute. Trois piliers, et ce qui en découle.`
- Le fil rouge fait doublon avec la vue moyens : supprimer l'encadré.
  Actuel : `<div class="thread"><span class="tl">Le fil rouge</span><b>Véhiculer la culture des Savoyards</b><span>Sa langue, son histoire, sa table : elle traverse les trois piliers, du marketing aux projets.</span></div>`
  Proposé : (supprimer)
- Les deux autres piliers commencent par un verbe (« Faire vivre », « Faire grandir »).
  Actuel : `<span class="st0"><i>1</i>Le cap</span>`
  Proposé : `<span class="st0"><i>1</i>Fixer le cap</span>`
- Actuel : `<li>La vision et ses deux axes, les objectifs</li>`
  Proposé : `<li>La vision et ses deux axes, l'objectif, les deux chantiers</li>`
- Si le bloc « Deux labels » est gardé ici malgré le doublon, il faut au moins aligner le texte de l'Universitât sur celui des moyens.
  Actuel : `Elle porte les projets qui dépassent Dolin : la renaissance des vermouths savoyards, le vermouth à la table savoyarde, les rencontres Chambéry–Turin, la route européenne. Une structure neutre, qui peut réunir d'autres maisons, des chefs, des bars et des collectivités.`
  Proposé : `Elle porte les projets qui dépassent Dolin : les bars à vermouth, les nouveaux vermouths savoyards, le vermouth à la table savoyarde, les rencontres du vermouth sabaudo. Structure neutre, elle réunit d'autres maisons, des bars, des chefs et des collectivités.`

### 19 · budget
- Actuel : `<p class="ey">Budget</p><h1>Un accompagnement <em>régulier</em></h1><p class="lead">Un partenariat dans la durée plutôt qu'une mission fermée : un rythme fixe de deux demi-journées par mois, une option, l'acculturation (sessions langue, culture, histoire et voyage à Turin), et des projets chiffrés à part.</p>`
  Proposé : `<p class="ey">Budget · Le devis</p><h1>Deux demi-journées <em>par mois</em></h1><p class="lead">Un rythme fixe, une option (l'acculturation) et des projets chiffrés à part.</p>`
- Le bouton renvoyait vers la note interne sur le tarif (P1).
  Actuel : `<button type="button" class="ck" data-view="questions">À confirmer</button>`
  Proposé : `<em class="tbd">à confirmer</em>`

### 20 · pilotage
- Actuel : `<h1>Qui fait quoi, <em>et quand</em></h1>`
  Proposé : `<h1>Les actions, <em>et où elles en sont</em></h1>`
- Formule unique. À défaut, supprimer la carte « Les rôles », qui fait doublon avec la vue qui fait quoi.
  Actuel : `<li><b>Franck Monod</b> propose, challenge, prépare et ouvre les portes</li>`
  Proposé : `<li><b>Franck Monod</b> propose, challenge et ouvre les portes</li>`
  Actuel : `<li><b>Dolin</b> décide, exécute et valide</li>`
  Proposé : `<li><b>Dolin</b> décide et exécute</li>`
- Actuel : `<b>Règle d'arbitrage</b>`
  Proposé : `<b>La règle d'arbitrage</b>`

### 21 · tableau
- Actuel : `<h1>Des indicateurs <em>par objectif</em></h1><p class="lead">Ce qu'on mesure, d'où on part, où on veut aller, et qui fournit le chiffre. Les outils (le Salone, la route européenne) ont leurs propres repères, mais ce sont les objectifs qui comptent.</p>`
  Proposé : `<h1>Des indicateurs, <em>de l'objectif aux jalons</em></h1><p class="lead">Ce qu'on mesure, d'où l'on part, où l'on va, et qui fournit le chiffre. Le Salone et la Route des vermouths sont des outils : on mesure ce qu'ils apportent à l'objectif.</p>`
- Remplacement à faire sur les 2 occurrences.
  Actuel : `<th>Objectif</th>`
  Proposé : `<th>Jalon</th>`
- Actuel : `<b>Chiffre d'affaires du vermouth en Savoie</b>`
  Proposé : `<b>Chiffre d'affaires de Dolin en Savoie</b>`
- Actuel : `<b>Ventes de Dolin en Savoie</b> (pour vérifier que la part de Dolin grandit aussi)`
  Proposé : `<b>Part de Dolin dans le marché savoyard</b>`
- Les ventes du Suédois figurent déjà dans le tableau de l'objectif : supprimer la ligne.
  Actuel : `<tr><td><b>Ventes du Suédois</b></td><td>Bonus</td><td>À mesurer</td><td>En hausse</td><td>Chaque trimestre</td><td>Dolin</td></tr>`
  Proposé : (supprimer)
- Actuel : `<td>Bonus</td>`
  Proposé : `<td>Atout</td>`
- Actuel : `indicateurs principaux de chaque objectif.`
  Proposé : `indicateurs principaux de chaque jalon.`

### 22 · questions
- Note interne visible par le client (P1) : supprimer les deux lignes.
  Actuel : `<li><b>Le tarif à la demi-journée</b><span class="who">Franck</span><span>400 € proposés ; 450 à 500 € restent raisonnables.</span></li>`
  Proposé : (supprimer)
  Actuel : `<li><b>L'émetteur du devis</b><span class="who">Franck</span><span>En son nom propre ou au nom de l'Universitât Sabauda.</span></li>`
  Proposé : (supprimer : à trancher avant l'envoi)
- Remplacement à faire sur toutes les occurrences restantes.
  Actuel : `<span class="who">Franck</span>`
  Proposé : `<span class="who">Franck Monod</span>`
- Actuel : `<span class="who">À vérifier</span><span>Annoncés pour 2027 par Laura Carello.</span>`
  Proposé : `<span class="who">Laura Carello</span><span>Annoncés pour 2027 : à vérifier.</span>`
- Actuel : `<b>Les contenus pour la route européenne</b>`
  Proposé : `<b>Les contenus pour la Route des vermouths</b>`

### 23 · lexique
- Définition unique du place-based marketing.
  Actuel : `<dd>Faire de l'identité culturelle d'un territoire (langue, histoire, symboles) la matière première d'une marque.</dd>`
  Proposé : `<dd>Faire de la culture d'un territoire (sa langue, son histoire, sa table) la matière première de la marque.</dd>`
- Mot absent du plan.
  Actuel : `<dt>Piola</dt><dd>Une taverne traditionnelle du Piémont.</dd>`
  Proposé : (supprimer)
- Formule trop proche du mot banni « espace alpin ».
  Actuel : `finance des projets communs entre les territoires alpins de France et d'Italie, dont la Savoie et le Piémont.`
  Proposé : `finance des projets communs à la France et à l'Italie, dont la Savoie et le Piémont.`
- À ajouter en tête de liste, pour fixer la terminologie :
  `<dt>Axe</dt><dd>L'une des deux directions de la vision : renouer avec l'espace sabaudo du vermouth ; travailler le marché savoyard.</dd>`
  `<dt>Chantier</dt><dd>Un axe mis en actions : chantier 1, Turin et l'Europe ; chantier 2, Chambéry et la Savoie.</dd>`
  `<dt>Jalon</dt><dd>Un résultat daté et mesuré d'un chantier ; six jalons en tout.</dd>`
  `<dt>Moyen</dt><dd>Ce qui fait avancer les chantiers : le marketing, la communication, les projets.</dd>`
  `<dt>Savôya</dt><dd>La Savoie, en savoyard.</dd>`

### 24 · references
- Date à vérifier : 3 juin dans le constat et dans la ligne suivante des références. Si c'est le 3 juin :
  Actuel : `le colloque Iter Vitis (23 juin 2026)`
  Proposé : `le colloque Iter Vitis (3 juin 2026)`
- Commentaire d'agence dans une source : supprimer la ligne entière (balise `<li>` comprise).
  Actuel : `Spherical Insights, estimation du marché français (non fiable, remplacée par l'IWSR)`
  Proposé : (supprimer)
- Rimini ne doit figurer qu'en question à Laura Carello : supprimer la ligne entière (balise `<li>` comprise).
  Actuel : `Beer&amp;Food Attraction 2027, chiffres et dates`
  Proposé : (supprimer)
- Nom à vérifier : la source dit « Torino Cocktail Week », la vue chantier 1 dit « Torino Cocktail Festival ». Garder un seul nom dans les deux vues.
