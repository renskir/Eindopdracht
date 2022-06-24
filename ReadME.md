# Verslag eindopdracht SET

## Achtergrond

## Het ontwerp van het algoritme, datastructuren en complexiteit
### Ontwerp 
In het bestand set.py staan twee klassen, namelijk de klasse SetKaart en Set. De klasse SetKaart weergeeft een kaart in
het spelletje Set, zowel als numpy array en als tekst, om later de gegeven afbeeldingen makkelijk terug te kunnen vinden, 
met de _str_ methode. De klasse Set weergeeft het spelletje Set, als stapel waar nieuwe kaarten van gepakt kunnen worden,
de kaarten die 'op tafel' liggen en de kaarten die uit het spel zijn, en de scores van de speler en de computer.
Er is een methode om nieuwe kaarten op tafel te leggen als er een set is gevonden (deze set wordt vervangen door de bovenste drie kaarten op de stapel) en 
om nieuwe kaarten op tafel te leggen als er geen kaarten zijn gevonden (de eerste drie kaarten worden vervangen door de bovenste drie kaarten op de stapel).
Ook zijn er methodes om één set te vinden en om alle sets in het spelletje te vinden, zodat er gecontroleerd kan worden of 
er sets te vormen zijn op tafel, als de speler er geen kan vinden. Deze methodes proberen alle mogelijke combinaties van 
drie kaarten uit de twaalf kaarten die op tafel liggen, en controleren of deze drie kaarten een set vormen. De methode 
_vind_set_ stopt als er een set is gevonden, terwijl de methode _vind_alle_sets_ doorgaat tot alle combinaties zijn gecontroleerd.
Ten slotte is er een _static_ methode om te controleren of drie gegeven kaarten een set vormen, wat gedaan wordt door de 
vectoren die de kaarten weergeven componentsgewijs bij elkaar op te tellen en te controleren of alle componenten na deling door drie
geen rest meer hebben. In dat geval weten we voor iedere eigenschap dat deze of gelijk was in alle drie de kaarten, 
of verschilde in alle drie de kaarten.

In het bestand _game.py_ staat 

### Datastructuren


### Complexiteit


## Implementatie en gebruik van de code


## Conclusies en discussie


## Taakverdeling
