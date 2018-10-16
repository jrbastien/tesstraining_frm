# tesstrain_frm

Entraînement de Tesseract 3-04, 3-05 pour la reconnaissance du moyen français avec des polices basées sur le Romain du Roi. A été optimisé spécifiquement pour l’Art du Menuisier de Roubo (1761). Pourrait être utilisé pour faire l'OCR de tout ouvrage de la Description des Arts et Métiers.

## Prérequis

- Tesseract 3.04 ou 3.05
- Votre propre police basée sur le Romain du Roi

## Préparation

### Polices

Il faut des polices de style Grandjean et Fournier italique pour réaliser les images contenant le texte de référence.

Remarque: les polices de petites capitales doivent être exclues de l’entraînement, car elles confondent l'OCR qui ne parvient plus à distinguer les vraies majuscules.

Il y a aussi 3 variations d’esperluette. C’est pourquoi on doit faire 2 variations des italiques avec un symbole d'esperluette différent dans chacune.

### Jeux de caractères Unicode

Le fichier Latin.unicharset a été modifié pour inclure les ligatures non supportées présentement par la norme Unicode. La valeur Unicode de ces ligatures a été déterminée à partir du standard fourni par le "[Medieval Unicode Font Initiative](https://folk.uib.no/hnooh/mufi/)". Vous pouvez les changer pour celle de votre propre police.

Voici toutes les ligatures et caractère anciens utilisés dans cet OCR:

| Car. | Sans lig. | Description| Valeur |
|---|----|------------|--------|
| Œ	| OE | E dans l'O | U+0152 |
| œ	| oe | e dans l'o | U+0153 |
| ſ | s  | s long     |	U+017F |
| ﬀ	| ff | f - f      |	U+FB00 |
| ﬁ	| fi | f - i      |	U+FB01 |
| ﬂ	| fl | f - l      | U+FB02 |
| ﬃ| ffi |f - f - i   |	U+FB03 |
| ﬄ| ffl |f - f - l   |	U+FB04 |
| ﬅ | st | s long - t |	U+FB05 |

Non-unicode:

| Car. | Sans lig. | Description| Valeur |
|---|----|------------|--------|
|  |si | s long - i | U+EBA2 |
| | ss	| s long - s long | U+EBA6 |
| | ssi | s long - s long - i | U+EBA7|
| |ct |	c - t	|			U+EEC5|


### Hauteur d’X

La hauteur d’X de vos polices doit être ajoutée au fichier Latin.xheights. La hauteur d’X est simplement le compte de pixels verticaux d’un x minuscule de 10 pt à 300 dpi. Vous pouvez la mesurer en utilisant un texte en PDF et en l’affichant dans un éditeur d’image comme GIMP.

### Propriétés de la police

Vos polices doivent être ajoutées au fichier font_properties.

Chaque ligne du fichier font_properties est formatée comme suit: 

    fontname italic bold fixed serif fraktur

où nom de la police est une chaîne nommant la police (aucun espace n’est autorisé!) et les propriétés nommées sont déterminées par soit la valeur 0 ou 1.

Exemple:

    timesitalic 1 0 0 1 0

### Numérotation et ponctuation

Les fichiers frm.numbers et frm.punc devraient déjà contenir tous les formats de numérotations et de ponctuation utilisés dans l’ouvrage. Éditez au besoin.

### Texte d'entraînement

Le fichier frm.training_text doit contenir tous les caractères utilisés dans l’ouvrage.

### Bigrammes

Le fichier frm.training_text.bigram_freqs donne la fréquence des lettres par rapport aux autres et est ordonné du bigramme le plus fréquent à celui qui est le moins. Pour le réaliser à l'aide du fichier d’entraînement:

    ~$ python tessngram.py training_text.txt

    Enter size of n-gram (int): 2

### Unigrammes

Le fichier frm.training_text.unigram_freqs donne la fréquence des lettres uniques et est ordonné de l'unigramme le plus fréquent à celui qui est le moins. Pour le réaliser à l'aide du fichier d’entraînement:

    ~$ python tessngram.py training_text.txt

    Enter size of n-gram (int): 1

### Désambiguïsation

Le ficher frm.unicharambigs permet d'éviter certaines ambiguïtés lors de la reconnaissance. Par exemple, Tesseract pourrait lire **Frg.** au lieu de **Fig.**, la présence d'une ligne lui disant de plutôt utiliser **Fig.** permettra que **Frg.** soit toujours changé en **Fig.**

Pour plus de détails sur le format de ce fichier, vous référer à la documentation offficelle [ici](https://github.com/tesseract-ocr/tesseract/blob/master/doc/unicharambigs.5.asc).

Remarque: l'OCR gagnerait à ce que ce fichier soit amélioré pour inclure toutes les instances ou un ſ long peut être pris pour un f et vice-versa. Il en est de même pour les ligatures. Je ferai ces améliorations, si j’ai un autre document de la Description des Arts et Métiers à digitaliser.

### Bigrammes de mots

Comme avec les bigrammes de lettres, le fichier frm.word.bigrams définit la fréquence d'un mot par rapport à un autre. Il est aussi ordonné du bigramme le plus fréquent à celui qui est le moins.

Idéalement, il devrait être fait à partir de tout l’ouvrage, mais à défaut il peut être réalisé à partir de quelques chapitres. Utilisez un outil en ligne comme [Online NGram Analyzer](http://guidetodatamining.com/ngramAnalyzer/)  

### Liste de mots

On doit fournir à tesseract la liste des mots possibles à reconnaître: frm.wordlist. La présente liste a été obtenu en combinant les mots spéciaux trouvés dans l’Art du Menuisier et ceux de la liste fournie par l'équipe de Tesseract sur Github. Pour ordonner la liste par fréquence, créer un fichier avec tous les mots appelé complet.xt et exécutez:

    ~$ python tesswordlist.py

## Compilation des fichiers d'entraînement de Tesseract

Il ne reste plus qu’à créer les fichiers d’entraînement de Tesseract à partir du script en exécutant:

~$ sudo ./tesstrain.sh --lang frm --langdata_dir ~/Documents/Roubo/Training2/langdata --tessdata_dir /usr/share/tesseract-ocr/tessdata/ --fonts_dir ~/.local/share/fonts --fontlist 'Caslon Roubo Regular' 'Fournier Roubo Italic' 'Fournier Roubo Alternate Italic' 'Fournier Roubo Alternate2 Italic' --output_dir /usr/share/tesseract-ocr/tessdata/ --overwrite >training_result.txt

## Tester le résultat:

Vérifier le fichier training_result.txt. Il ne devrait contenir d'autres erreurs que "Couldn't find a matching blob". Cette erreur est plutôt commune car Tesseract procède par boîtes carrées et la forme des italiques a tendance à chevaucher celle des lettres régulières. Idéalement cela devrait être évité mais s’il y a peu de ces mauvais blobs par rapport au total trouvé, cela ne causera pas trop de problèmes.

Pour tester le résultat, exécuter la commande suivante sur une image contenant le texte:

    ~$ tesseract page100.png page100 -l frm

## Encore plus d’outils

Une fois le fichier d’entraînement réalisé, vous pouvez procéder à l’OCR en utilisant les outils de mon autre repo : [ocrhelper](https://github.com/jrbastien/ocrhelper)

## En conclusion
Si vous désirez seulement utiliser le fichier d’entraînement déjà réalisé, le télécharger [ici](https://github.com/jrbastien/tesstraining_frm/blob/master/frm.traineddata) et le copier dans /usr/share/tesseract-ocr/tessdata.

Si vous trouvez ces outils ou ces informations utiles, n’hésitez pas à me le dire. J’aimerais aussi connaître vos suggestions d’amélioration.
