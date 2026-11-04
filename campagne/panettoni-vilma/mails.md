# Mails de la campagne *Panettoni Vilma* — commerces de Savoie et de Haute-Savoie

> Brouillons à relire. **Rien ne part tout seul** : Franck relit, envoie les tests, puis active lui-même
> le scénario dans le Brevo de Cultura Sabauda. Montage : `sequence-brevo.md`.
> Modèle suivi : la campagne *Diccionèro de fata* de l'Institut de la Langue Savoyarde
> (dépôt `Enstitut`, `campagne/diccionero-de-fata/`), adaptée.

## Le principe (décisions de Franck, 04/11/2026)

- **L'association présente, Vilma vend.** Les commerces répondent à Franck ; l'Universitât Sabauda
  des sciences gastronomiques les **met en relation** avec Vilma e Elio (Corinne), qui fixe les prix,
  prend la commande et livre. Aucun mail ne donne de prix ni de conditions tant que Corinne ne les a
  pas envoyés : on écrit « tarifs et conditions sur simple réponse ».
- **Un seul expéditeur** : franck.monod@culturasabauda.eu. Les mails 1 et 3 (formels) portent le nom
  de l'association ; les mails 2 et 4 (courts) sont signés Franck.
- **Lancement dès que possible**, calendrier serré avant Noël (§ Calendrier).

## Avant tout envoi

**À compléter** (un mail qui garde une de ces marques ne part pas) :

- `[DATE LIMITE]` : dernier jour pour se manifester et être livré avant les fêtes, à fixer **avec Corinne**
  (délai de fabrication et de livraison depuis le Piémont). Proposé : jeudi 26 novembre 2026.
- Photos : reprises du catalogue de Vilma & Elio (`visuels/`), droits à confirmer avec Corinne.
- Prix revendeur et conditions : le catalogue 2025 dit seulement « tarifs dégressifs » ; les prix 2026 sont à
  demander à Corinne.

**Faits employés** (et seulement eux) :
- **Catalogue « Panettoni d'autore 2025 » de Vilma & Elio** (PDF transmis par Franck le 04/11/2026,
  Drive « Panettoni d'autore 2025.pdf ») : 11 recettes en 5 lignes, formats 500 g, 750 g et 1 kg
  (Selezione Limitata : 500 g et 750 g), tarifs dégressifs selon la quantité, commandes au +39 347 171 7706.
  - Linea Classica : *Panettone Classico* (recette milanaise, levain naturel vivant, écorces d'orange et de cédrat
    confites) ; *Panettone Cioccolato* (pépites de chocolat noir).
  - Linea Gourmet : *Cereali e frutti di bosco* ; *Pere e cioccolato*.
  - Selezione Limitata : *Persi Pien* (« il panettone cuore del Piemonte » : cacao, gouttes de pêche, amandes,
    glaçage chocolat, éclats d'amaretti) ; *Pistacchio* ; *Sacher*.
  - Speciale della Casa : *Pumaté* (Villar Perosa, pomme et cannelle) ; *Cubolì* (« il nostro panettone più
    amato » : gelée d'abricot déshydratée).
  - Linea Monte Granero : *Monte Granero* (leur pandoro artisanal) ; *Monte Granero al cacao*.
  - Christmas Mistery Box M, L, XL : 50, 75, 100 € (prix public).
- **Échantillons** : Corinne propose d'envoyer quelques échantillons aux commerces intéressés (04/11/2026).
- **Réunion du 28/10/2026 chez Vilma e Elio** : l'abricot est sans raisins secs ni fruits confits ; nouveauté 2026,
  une version sans lactose.
- **Projet** (message de Franck du 04/11/2026) : Franck a fondé l'Universitât Sabauda ; l'association participe au
  projet SavoiaExperience (Interreg ALCOTRA), chargée de la recherche gastronomique et du repas de clôture avec des
  traiteurs partenaires. 
- **Histoire de Modane** (vérifiée le 04/11/2026) : le percement du tunnel du Fréjus commence en 1857, quand la
  Savoie dépend encore du royaume de Piémont-Sardaigne ; le tunnel ouvre en 1871 (et non 1872) — tunnels-ferroviaires.org,
  Britannica. Une seule source (madeinmarseille.net) dit que les ouvriers du tunnel aimaient un pain sucré aux raisins,
  ancêtre du pain de Modane, « entre la brioche des rois et le panettone » ; **aucune source ne dit que des Piémontais
  ont apporté le panettone à Modane** : on l'écrit donc comme un récit (« on raconte que »), jamais comme un fait.
- **Photos et couleurs** : reprises du catalogue de Vilma & Elio à la demande de Franck (04/11/2026), découpées dans
  `visuels/produits/`. `[À CONFIRMER avec Corinne]` : que Vilma e Elio peut utiliser ces photos (droits).

**Règles** (reprises de la campagne du dictionnaire) :
- chaque mail dit **d'où vient l'adresse** et permet de **refuser** (« non merci » + lien de désinscription) ;
- **quatre mails au plus** par commerce, puis éventuellement un appel ; **un « non » est définitif** ;
- **on arrête dès qu'un commerce répond**, même pour dire « plus tard » : la réponse se reporte le jour même
  dans Brevo (`STATUT_CAMPAGNE`), sinon la relance part quand même ;
- on ne promet rien au nom de Vilma (prix, délais, échantillons) sans l'accord de Corinne.

**Champs Brevo employés** : `{{ contact.ORIGINE_CONTACT }}` (pied de mail), `{{ contact.PANETTONE_EN_RAYON }}`
(« oui » si le commerce vend déjà des panettoni : une phrase change dans le mail 1), `{{ unsubscribe }}`.
`ORGANISME`, `COMMUNE`, `TYPE_COMMERCE` servent aux listes et au suivi.

### Pied de mail (mails 1 et 3)

```
Universitât Sabauda des sciences gastronomiques, association qui fait connaître la gastronomie
sabaude, de la Savoie au Piémont.
franck.monod@culturasabauda.eu · Siège : Maison des associations, 67 rue Saint-François-de-Sales, 73000 Chambéry
Origine de votre adresse : {{ contact.ORIGINE_CONTACT }}. Si vous ne souhaitez plus recevoir nos
messages, répondez simplement « non merci ».
Se désinscrire : {{ unsubscribe }}
```

### Signature de Franck (mails 2 et 4) + pied court

```
Franck Monod
Président, Universitât Sabauda des sciences gastronomiques
Tél. : 00 33 (0)6 31 19 42 49 · franck.monod@culturasabauda.eu

Universitât Sabauda des sciences gastronomiques · Siège : Maison des associations, 67 rue Saint-François-de-Sales, 73000 Chambéry.
Origine de votre adresse : {{ contact.ORIGINE_CONTACT }}. Répondez « non merci » et je ne vous écrirai plus.
Se désinscrire : {{ unsubscribe }}
```

---

## Calendrier (proposé le 04/11/2026)

| Date | Mail | Expéditeur affiché | Attente avant le suivant |
|---|---|---|---|
| mar. 10 nov. | 1, présentation (formel) | Universitât Sabauda | 6 jours |
| lun. 16 nov. | 2, relance courte | Franck Monod | 4 jours |
| ven. 20 nov. | 3, date limite (formel) | Universitât Sabauda | 6 jours |
| jeu. 26 nov. | 4, dernier mail court | Franck Monod | puis appel si rien |

Les dates sont écrites dans les mails 2, 3 et 4 : si le lancement glisse, les corriger avant d'activer.

---

## Mail 1 — présentation (mar. 10 nov.)

**Expéditeur** : Universitât Sabauda <franck.monod@culturasabauda.eu> · **Réponse à** : franck.monod@culturasabauda.eu
**Objet** : Des panettoni artisanaux du Piémont pour votre commerce, avant Noël
**Pré-en-tête** : Les panettoni de Vilma e Elio : de la Savoie au Piémont, une même histoire
**Modèle Brevo** : #58 · HTML : `modeles/1-presentation.html`

```
[Bandeau image] PANETTONI d'autore · Vilma & Elio · Piémont

Madame, Monsieur,

L'Universitât Sabauda des sciences gastronomiques fait connaître la gastronomie sabaude, de la Savoie au
Piémont. Pour le projet européen SavoiaExperience (Interreg ALCOTRA), nous menons la recherche gastronomique
et préparons le repas de clôture avec des traiteurs partenaires de Savoie et du Piémont. Parmi eux, Vilma e
Elio, maison artisanale piémontaise, dont nous aimerions vous faire goûter les panettoni.

[Visuel] drapeau de Savoie · tunnel du Fréjus, 1857-1871 · drapeau du Piémont · « une même histoire »
À Modane, on raconte que les ouvriers du tunnel du Fréjus aimaient un pain sucré aux raisins : l'ancêtre
du pain de Modane, cousin du panettone.

[Trois vignettes] Le Cubolì, à l'abricot, sans fruits confits · Sans lactose, la nouveauté 2026 ·
Échantillons, pour goûter avant de commander

[si PANETTONE_EN_RAYON = oui] Vous proposez déjà des panettoni : ceux-ci peuvent compléter votre rayon avec
des parfums que l'on trouve peu, artisanaux et piémontais.
[sinon] Pour les fêtes, c'est un cadeau gourmand qui change, à côté de vos vins / de vos fromages / de vos
produits bio / de votre épicerie (selon TYPE_COMMERCE).

[Encadré] Intéressé ? Répondez à ce mail : nous vous envoyons les tarifs revendeurs et des échantillons, et
nous vous mettons en relation avec Vilma e Elio, qui prend la commande et livre. Pour Noël, écrivez-nous
avant le [DATE LIMITE].
Boutons : Recevoir les tarifs (réponse par mail) · Voir le catalogue (PDF)

Nous vous prions d'agréer, Madame, Monsieur, nos salutations distinguées.
Universitât Sabauda des sciences gastronomiques
```
*+ pied de mail. Catalogue en lien, pas en pièce jointe (voir `LISEZMOI.md`).*

**Doctrine** (coffre Obsidian, `01-Commun/Lexique sabaud.md` et `Vocabulaire interdit.md`) : « gastronomie sabaude »,
« de la Savoie au Piémont », jamais « versant », « de part et d'autre », « deux côtés » ; gentilés (piémontais), pas de
nationalité ; aucun tiret cadratin dans le texte visible.

## Mail 2 — relance courte de Franck (lun. 16 nov.) · modèle Brevo #59

**Expéditeur** : Franck Monod <franck.monod@culturasabauda.eu>
**Objet** : Les panettoni de Vilma e Elio, en deux mots

```
Bonjour,

Je me permets de revenir vers vous au sujet des panettoni artisanaux de Vilma e Elio, maison artisanale piémontaise,
que nous vous avons présentés le 10 novembre.

Je sais que le temps manque en cette saison, et qu'un e-mail se perd vite : d'où ce petit rappel.

Si cela vous intéresse, un mot en réponse me suffit : je vous envoie les tarifs revendeurs, Corinne, chez
Vilma e Elio, peut vous faire goûter quelques échantillons, et je vous mets en relation avec elle. Si ce n'est pas pour vous, dites-le-moi aussi :
j'arrête les relances.

Bonne journée,
Franck
```
*+ signature de Franck + pied court.*

## Mail 3 — date limite (ven. 20 nov.) · modèle Brevo #60

**Expéditeur** : Universitât Sabauda <franck.monod@culturasabauda.eu>
**Objet** : Panettoni pour Noël : dernière semaine pour commander

```
Madame, Monsieur,

Pour avoir les panettoni de Vilma e Elio en boutique avant les fêtes, il faut nous écrire au plus tard
le [DATE LIMITE] : passé cette date, la livraison avant Noël n'est plus garantie.

Pour rappel : panettoni artisanaux de Vilma e Elio, maison piémontaise et traiteur partenaire de notre
travail sur la gastronomie sabaude : onze recettes, dont le Cubolì à l'abricot, sans raisins ni fruits
confits, et une version sans lactose.

Leur catalogue : Panettoni d'autore (PDF, en italien) [lien]. Répondez simplement à ce mail : nous vous
envoyons les tarifs revendeurs, Vilma e Elio peut vous faire goûter quelques échantillons, et nous vous
mettons en relation avec eux.

Nous vous prions d'agréer, Madame, Monsieur, nos salutations distinguées.

Universitât Sabauda des sciences gastronomiques
```
*+ pied de mail.*

## Mail 4 — dernier mail, court, de Franck (jeu. 26 nov.) · modèle Brevo #61

**Expéditeur** : Franck Monod <franck.monod@culturasabauda.eu>
**Objet** : Dernier mail de ma part au sujet des panettoni

```
Bonjour,

C'est mon dernier mail au sujet des panettoni de Vilma e Elio : aujourd'hui est le dernier jour
conseillé pour une livraison avant les fêtes.

Si l'idée vous plaît pour plus tard (Pâques avec la colomba, ou Noël prochain), répondez-moi
simplement « plus tard » et je reviendrai vers vous le moment venu. Faute de réponse, je vous
appellerai peut-être une minute ; répondez « non merci » et je ne le ferai pas.

Belle fin d'année,
Franck
```
*+ signature de Franck + pied court.*

---

## Après le mail 4 : appel (commerces sans réponse)

Dit à la personne qui décide, pas au standard :

> Bonjour, je suis Franck Monod, de l'Universitât Sabauda des sciences gastronomiques, une association
> de Savoie. Je vous ai écrit au sujet des panettoni artisanaux d'une maison piémontaise, Vilma e Elio.
> Je voulais simplement savoir si mon message vous était bien parvenu. Est-ce que ce serait intéressant
> pour vous, pour cette année ou pour l'an prochain ?

- **Oui** → « Je vous envoie la fiche et les tarifs, et je vous mets en relation avec Corinne, chez
  Vilma e Elio. À quelle adresse ? » (`STATUT_CAMPAGNE = interesse`).
- **Plus tard** → noter la période (`plus_tard`).
- **Non** → « Très bien, je ne vous recontacterai pas. Bonne journée. » (`exclu`, définitif).

## Réponse type à un commerce intéressé (mise en relation)

**Objet** : Panettoni Vilma e Elio — fiche, tarifs et contact

```
Bonjour [PRÉNOM / Madame, Monsieur],

Merci pour votre réponse ! Vous trouverez ci-joint la fiche des panettoni de Vilma e Elio, avec les
tarifs et les conditions.

Je vous mets en copie Corinne, chez Vilma e Elio : c'est avec elle que se passent la commande et la
livraison. Corinne, je te présente [NOM DU COMMERCE], à [COMMUNE], intéressé par [ce qu'ils ont dit].

Je reste disponible si besoin.

Bonne journée,
Franck
```
*Corinne en copie (info@vilmaelio.com). Le mail est en français ; si Corinne préfère, ajouter deux lignes
en italien pour elle sous la signature.*
