# Audit direction artistique : homogénéité graphique dans la charte Dolin

Base : les 72 captures (bureau, mobile, sombre), dolin-extra.css, vil.css, dolin-tokens.css, dolin-body.html.

## 1. Ce qui va

- La charte tient dans l'ensemble : Playfair Display pour les titres, Raleway pour le texte, rouge et or de l'emblème, fond ivoire, losanges sur les boutons, menu latéral sobre.
- Trois vrais visuels portent le message : l'accueil (`.hero`), la carte des deux axes (vision, `.mapband`), la maison de la stratégie (`.house`).
- Les deux chantiers (turin, chambery) partagent le même gabarit de jalon (numéro, cible, actions, moyen, qui, quand), et il se replie bien en fiches sur mobile.
- Objectifs : la frise des trois étapes (`.tl3`) et le bloc Suédois (`.sued`) donnent une hiérarchie nette.
- Le mode sombre a ses propres tokens. Les photos et la plupart des cartes y restent lisibles.

## 2. Ce qui ne va pas

### P1 : bloquant

1. **diagnostic (bureau et mobile) : le bloc « Deux analyses nourrissent ce diagnostic » est cassé.** On voit deux colonnes de 156 px sur fond rouge, et leur texte déborde sur « Ce qu'on en tire ». La cause est une collision de classes : `.d2` de vil.css (l. 318, `.d2{width:156px;height:156px;background:var(--hi)}`, prévue pour les disques `.tdisc`) s'applique aussi à `<div class="det4 d2">`. **Correction :** dans le HTML, `class="det4 d2"` devient `class="det4 dk2"`, et dans dolin-extra.css l. 313, `.det4.d2` devient `.det4.dk2` (dans la règle et dans sa media query).

2. **strategie (mobile) : la rangée « L'objectif » de la maison est écrasée en trois colonnes.** On lit un mot par ligne, et « +[__] % » est coupé. La cause : `.hobj{grid-template-columns:120px minmax(0,1.4fr) minmax(0,1fr)}` (dolin-extra.css l. 532) est déclaré après la media query de la l. 462 et l'écrase. **Correction :** ajouter après la l. 538 :
   `@media (max-width:900px){.hobj{grid-template-columns:minmax(0,1fr)}.hobj .hnum{border-left:0;border-top:1px solid var(--line)}}`

3. **marque (mobile) : « La méthode » reste sur quatre colonnes de 80 px.** Les titres se chevauchent (« plateforme » passe sur « pas tout casser »). La cause : `.card ol.steps4` (l. 228) a une spécificité plus forte que la media query `.steps4` (l. 233). **Correction :**
   `@media (max-width:900px){.card ol.steps4{grid-template-columns:minmax(0,1fr)}}`

4. **Tableaux tronqués sur mobile, sans aucun indice de défilement (terrain, communication, roles, calendrier, budget, tableau).** `.scroll{overflow-x:auto}` cache des colonnes clés : les Quand et les Qui des canaux, la part de Franck Monod et des labels, la description du calendrier, le prix du devis, les cibles du tableau de bord. **Correction :** sous 600 px, passer les tableaux en fiches. Il faut ajouter `data-l` sur chaque `td`, recopié en JS depuis le `th` de sa colonne, puis :
   `@media (max-width:600px){.tbl thead{display:none}.tbl,.tbl tbody,.tbl tr,.tbl td{display:block;width:auto}.tbl tr{padding:10px 0;border-bottom:1px solid var(--line)}.tbl td{border:0;padding:2px 0}.tbl td[data-l]:not(:first-child)::before{content:attr(data-l)" : ";font-weight:700;color:var(--muted)}}`

5. **Mode sombre : des titres en rouge très foncé sur fond sombre sont illisibles.** C'est le cas de « Faire grandir les ventes de Dolin » dans strategie (`.hobj b{color:var(--band)}`) et dans objectifs (`.bizh h2{color:var(--band)}`), ainsi que de `.hob b`. Le cadre `.biz` (`border:2px solid var(--band)`) disparaît presque. **Correction :** remplacer `color:var(--band)` par `color:var(--hi)` dans `.hobj b`, `.bizh h2` et `.hob b`, et ajouter `.biz,.hobj{border-color:var(--hi)}`. En clair, `--hi` (#a82424) reste dans la charte. En sombre, il vaut #ef7a6e, qui est lisible.

6. **Plusieurs grands aplats rouges par vue, alors que la règle client en demande un seul.**
   - Marketing en a 5 : `.pban` et les 4 tuiles `.mtv.word` (sur mobile, cela fait un mur rouge de 4 × 255 px).
   - Objectifs en a 3 : `.obax` Chantier 1, `.obax` Chantier 2 (en terracotta) et `.sued`.
   - Strategie en a 2 : `.hroof` et `.hrow.hmo`.
   - Marque en a 2 : `.pban` et `.bl.bl1`.
   - Turin en a 2 : `.pban` et `.urg.uwide`, plus `.mapband` dans l'accordéon.

   **Corrections :**
   - (a) Marketing : `.mtv.word{background:var(--surface2);border-bottom:3px solid var(--band-hi);aspect-ratio:3/1}`, `.mtv.word span{color:var(--hi)}`.
   - (b) Objectifs : `.obax{background:var(--surface);color:var(--ink);border:1px solid var(--line);border-top:4px solid var(--hi)}`, `.obax span{color:var(--hi)}`, `.a2 .obax{background:var(--surface);border-top-color:var(--band-hi)}` et `.a2 .obax span{color:var(--accent)}`.
   - (c) Strategie : `.hmo{background:var(--surface);border:2px solid var(--hi)}`, `.hmo b{color:var(--ink)}`, `.hmo em{color:var(--hi)}`, `.hmo .hl{color:var(--hi)}`. Le toit `.hroof` reste le seul aplat.
   - (d) Marque et turin : voir le point 7.

7. **En-têtes de vue : la règle n'est pas lisible.**
   - `.pban` (bandeau rouge) sert pour marketing, marque, turin et chambery.
   - `.vh` (en-tête clair) sert pour les 18 autres vues.
   - Strategie n'a aucun en-tête.

   Parmi les trois moyens, marketing a un bandeau, alors que communication et projets ont un en-tête clair. **Règle proposée :** « En-tête clair `.vh` sur toutes les vues sauf l'accueil. Le rouge n'est jamais un en-tête : il est réservé au seul bloc-clé de la vue. » Les blocs-clés rouges seraient : accueil `.hero`, vision `.mapband`, objectifs `.sued`, strategie `.hroof`, projets `.mot`, marque `.bl1` et turin `.urg.uwide`. Les autres vues n'ont pas d'aplat.

   **Vues à changer :**
   - Marketing, marque, turin et chambery : remplacer `<div class="pban"><div class="in">…` par `<header class="vh"><div>…</div></header>`, en gardant le même `ey`, le même `h1` et le même `lead`.
   - Strategie : ajouter avant `.house`
     `<header class="vh"><div><p class="ey">Stratégie · La stratégie globale</p><h1>Une vision, <em>deux chantiers, trois moyens</em></h1></div></header>`.

8. **decisions : l'aplat `.band.end` « Chambéry, à nouveau ville du vermouth. » est la troisième occurrence du même grand aplat.** Il reprend celui de l'accueil (`.hero`) et le toit de strategie (`.hroof`). C'est un doublon, et il prend 540 px. **Correction :** supprimer `<section class="band end" aria-label="Conclusion">…</section>` de la vue decisions.

### P2 : important

9. **Vert hors charte en fond.** `--accent-soft:#e6ede0` (en sombre `#243024`) teinte :
   - `.thread` : moyens (×3), objectifs, decisions et accompagnement ;
   - les lignes `.tbl tr.us td` : terrain, communication, calendrier, budget, roles et tableau ;
   - les pastilles `.idea i` et `.lv i`.

   **Correction dans dolin-tokens.css :** `--accent-soft:#f5ead6` en clair, `#2c2219` dans les deux blocs sombres. Pour les lignes mises en avant :
   `.tbl tr.us td{background:color-mix(in srgb,var(--band-hi) 16%,var(--surface))}.tbl tr.us td:first-child{box-shadow:inset 3px 0 0 var(--hi)}`

10. **Codes d'acteurs et pastilles : vert, olive et terracotta hors charte, et sept styles de pastille.**
    - Les couleurs fautives sont :
      - `.qx.ils`, `.ro.ils` et `.cv.ils` en `--c-nature` (vert), sur turin, chambery et roles ;
      - `.tag.eng` « En cours » en `--ok` (vert), sur projets ;
      - l'avatar « CS » en `--pc:var(--c-nature)`, sur terrain ;
      - `.a2 .obax` en `--terra`.
    - Les sept styles sont `.tag`, `.tbd`, `.obr .o0/.o1`, `.mv`, `.qx`, `.mv.k` et `.ntag`.

    **Règle proposée :** une pastille pleine désigne un moyen (`.mv`), une pastille en contour désigne un acteur (`.qx`), une pastille en pointillé désigne ce qui est à fixer (`.tbd`, `.obr .o0`).

    **Corrections :**
    - Tokens : `--c-nature:var(--accent)`.
    - `.qx.ils{background:var(--surface);border:1px dashed var(--accent);color:var(--accent)}`
    - `.qx.us{background:color-mix(in srgb,var(--band-hi) 35%,var(--surface));border-color:var(--band-hi);color:var(--ink)}`
    - `.ro.ils,.cv.ils{--rc:var(--band-hi)}`
    - `.tag.eng{color:var(--hi)}`
    - Dans le HTML de terrain, les `--pc` des avatars `.pp i` se limitent à `var(--hi)`, `var(--band)`, `var(--accent)` et `var(--ink2)`. On retire `--c-nature`, `--c-bouger` et `--warn`.

11. **diagnostic : la grille SWOT utilise quatre couleurs, dont deux rouges presque identiques.**
    - Forces sont en vert (#5c7a4a, l. 109) et Faiblesses en ocre.
    - Opportunités (`--hi` #a82424) et Menaces (`--crit` #b8322a) ne se distinguent pas l'une de l'autre.

    **Correction :** supprimer `.sw.f{--sc:#5c7a4a}` (l. 109), puis écrire `.sw.f{--sc:var(--hi)}.sw.w{--sc:var(--ink2)}.sw.o{--sc:var(--band-hi)}.sw.t{--sc:var(--band)}` et `.sw h3{color:var(--ink)}`. Seule la barre du haut porte la couleur.

12. **Encadrés : cinq composants pour la même fonction « à retenir ».**
    - `.luc` : filet rouge à gauche, 12 occurrences.
    - `.thread` : fond vert (Le cap, Le fil rouge, Méthode, Le socle, Ensuite).
    - `.bgov` : filet noir au-dessus, sur marque.
    - `.rule` : carte avec filet ocre posé en ligne (`style="--rc:var(--warn)"`), sur marketing et communication.
    - `.lbl` : carte avec filet or.

    **Règle proposée :**
    - `.luc` sert une seule fois par vue, en bas, pour la conclusion.
    - `.thread` sert aux principes transverses, sur le fond ivoire-or du point 9.
    - `.bgov` est remplacé par `.thread`.
    - `.rule` et `.lbl` prennent le même filet : `.rule{border-left-color:var(--band-hi)}`, et on supprime les `style="--rc:var(--warn)"` en ligne.

    **Vues à reprendre :**
    - Vision : deux `.luc` empilés. On garde « De la vision aux objectifs ».
    - Moyens : trois `.thread` d'affilée (Le cap, Le fil rouge, Méthode). On garde « Le fil rouge » en `.thread` ; les deux autres deviennent une ligne `.note`.

13. **Numérotation : quatre manières différentes.**
    - Chiffres Playfair rouges : decisions, jalons, moyens, `.steps4`.
    - Ronds pleins olive : `.hw .st0 i` sur accompagnement, cartes « Les expériences » de marketing.
    - Ronds verdâtres à lettres : `.idea i`.
    - Texte « Message 1 » : `.ord3`.

    **Correction :**
    - `.hw .st0 i{background:var(--hi)}` ; même chose pour les ronds de marketing. Le rond n° 1 rouge d'accompagnement (`.hw.first`) n'est alors plus seul de sa couleur.
    - `.idea i{background:color-mix(in srgb,var(--band-hi) 30%,var(--surface));color:var(--ink)}`

14. **Doublons visuels et de titre.**
    - Accompagnement reprend à l'identique « Deux labels » (`.lbls`, mêmes cartes que dans moyens) et « Le fil rouge » (`.thread`, idem). **Correction :** supprimer ces deux blocs d'accompagnement et les remplacer par `<p class="note">Les deux labels et le fil rouge : <button type="button" class="link" data-view="moyens">Les moyens →</button></p>`.
    - Le h1 de pilotage, « Qui fait quoi, <em>et quand</em> », double l'entrée de menu « Qui fait quoi » (roles) et le bloc `.cm2` de turin, « Qui fait quoi, et quand ? ». **Remplacer** « Qui fait quoi, <em>et quand</em> » **par** « Le suivi <em>des actions</em> ».

15. **turin : photo `.urg.uwide`.**
    - Le texte est posé sur une foule et sur les enseignes d'autres maisons (« TRINCHIERI », « ZOPPI »), alors que Dolin doit rester au centre.
    - Sur mobile, le titre « Turin, janvier 2027 » percute l'enseigne.
    - La mention de validation des photos du Salone par Laura Carello est absente de cette vue.

    **Correction :**
    - `.urg.uwide .ubg{object-position:15% 35%}` pour sortir les enseignes du cadre. À défaut, prendre une photo sans marque.
    - Sur mobile : `.urg.uwide::after{background:color-mix(in srgb,var(--band) 92%,transparent)}`.
    - Légende : **remplacer** « Le Salone 2026, au Palazzo Carignano. Photo Salone del Vermouth » **par** « Le Salone 2026, au Palazzo Carignano. Photo Salone del Vermouth, à faire valider par Laura Carello ».

16. **objectifs, terrain : photos mal cadrées.**
    - Objectifs : `.suph img` (Suédois) coupe la bouteille au bord gauche. On lit « OIS IN », et l'étiquette du produit mis en avant est illisible. **Correction :** `.suph img{object-position:8% 50%}` et, sur mobile, `.suph{min-height:340px}`.
    - Terrain : l'affiche 2027 est en `object-fit:cover` (`.gal img`, l. 331). Les marges sont rognées sur bureau, et sur mobile la ligne de dates disparaît. **Correction :** ajouter une classe à l'affiche, puis `.gal img.poster{object-fit:contain;background:var(--surface)}`.

17. **vision : le visuel « deux gâteaux » contredit son message.**
    - (a) À l'impression, dans les captures ou sans JS, les deux disques ont la même taille. `.cake4 .gbig{transform:scale(.45)}` ne s'annule qu'avec la classe `.go`, alors que la légende dit « un marché plus grand ».
    - (b) Il y a environ 120 px de vide au-dessus des disques.
    - (c) Les légendes sont décalées : « Aujourd'hui » est 9 px plus haut que « 2030 ».
    - (d) Sur mobile, les libellés font environ 6 px. Il en va de même pour les villes de la carte `.vmmap`.

    **Correction :**
    - État final par défaut : `.cake4 .gbig{transform:none;opacity:1}`. L'animation passe dans un `@keyframes` (de `scale(.45)` à `none`), déclenché seulement sous `html.anim .cake4.go`.
    - `.cake4 svg{max-height:260px}`.
    - Les deux légendes passent en HTML sous les disques, sur une grille de deux colonnes alignées.
    - Sous 600 px, sur la carte, on masque les villes secondaires et on garde seulement « Chambéry ».

18. **Vues trop chargées en texte.**
    - Vision : le `.luc` « Ce que dit le marketing » fait cinq lignes, avec Kotler, Brandenburger et Nalebuff. Le passer dans un `<details class="card acc">` fermé, sous le titre « Ce que dit le marketing ».
    - Roles : 4 cartes `.ro` denses, un tableau, deux conventions `.cv` et une liste d'actions. Les deux `.cv` passent dans un accordéon fermé, « Les deux conventions ».
    - Projets : 8 cartes `.pj` de trois ou quatre lignes chacune. On garde le titre et la ligne « Porté par… » ; le paragraphe `p` passe dans un `details`.

### P3 : finition

19. **Vues sans visuel où un visuel simple aiderait.**
    - Calendrier : c'est un tableau seul. Proposer une frise de novembre à mai sur deux couloirs (Chantier 1, Chantier 2), avec un losange or sur le Salone, en réutilisant `.tl3` ou `.dcal`.
    - Chambery : c'est le pendant de turin, qui a sa photo, mais la vue n'a aucune image. Proposer une petite carte de Savoie (celle de vision, en `.vmmap` réduite, fond `--surface2`) avec les jalons 4 à 6 placés dessus. Pas de nouvel aplat rouge.

20. **marketing : les noms « Punt e Mes » et « Chazalettes » sont coupés par le bord de la tuile à 1280 px.** `.mtv.word span{font-size:clamp(30px,3.4vw,44px)}` est trop grand pour des colonnes d'environ 180 px. **Correction :** `.mtv.word span{font-size:clamp(22px,2.3vw,32px);padding:0 10px;text-align:center;overflow-wrap:anywhere}`.

21. **tableau : colonnes trop étroites.** « À / mesurer », « 5 % / (2020) » et « En / hausse » se cassent sur deux lignes, et les quatre tableaux n'ont ni les mêmes colonnes ni les mêmes largeurs, ce qui casse l'alignement d'un tableau à l'autre. **Correction :**
    - `#v-tableau .tbl td:not(:first-child){white-space:nowrap}`
    - Un `<colgroup>` commun aux quatre tableaux : Indicateur 38 %, Objectif 8 %, Départ 13 %, Cible 11 %, Quand 14 %, Qui 16 %. La colonne Objectif reste vide pour « L'objectif » et « Le socle ».

22. **Toutes les vues (mobile) : les boutons « ← précédent » et « Suivant » se posent sur deux lignes décalées.** **Correction :** `@media (max-width:600px){.pager{flex-direction:column-reverse}.pager button{width:100%}}`.

23. **Accueil (mobile) : le paragraphe du `.hero` touche le filet intérieur droit.** **Correction :** donner au contenu de `.hero` un `padding-inline` d'au moins 24 px sous 600 px.

24. **pilotage : formulaire hors charte française.**
    - La date s'affiche « mm/dd/yyyy ».
    - Le menu Étape est tronqué : « Décembre · Lancer ».
    - Sur mobile, le filtre « Les deux » passe à la ligne.

    **Correction :** ajouter `lang="fr"` sur `<html>` (ou sur `#f-due`), puis `#f-phase{min-width:200px}` et `.seg{flex-wrap:nowrap;overflow-x:auto}`.

25. **Fils d'Ariane incohérents avec le menu.**
    - Vision : **remplacer** « Vision et objectifs · La vision » **par** « Vision et objectif · La vision » (c'est le libellé du menu).
    - Marque : le menu range la vue sous « Les moyens », mais le fil d'Ariane dit « Les outils · Le socle ». **Remplacer** « Les outils · Le socle » **par** « Les moyens · Le socle ».
